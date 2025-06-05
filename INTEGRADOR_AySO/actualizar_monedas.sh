#!/usr/bin/env bash
#
# actualizar_monedas.sh
#
# Consulta las APIs de dólar oficial y euro,
# extrae compra/venta con jq, guarda en un CSV,
# y genera/actualiza un index.html con la última cotización.
#

### CONFIGURACIÓN: ###
# Ruta completa al CSV donde se acumularán los datos
CSV_FILE="/var/www/cotizaciones/historico_monedas.csv"
# Ruta completa al HTML que se va a sobrescribir
HTML_DEST="/var/www/cotizaciones/index.html"

# URLs de las APIs:
API_USD="https://dolarapi.com/v1/dolares/oficial"
API_EUR="https://dolarapi.com/v1/cotizaciones/eur"

# Timestamp actual (YYYY-MM-DD HH:MM:SS)
FECHA_HORA=$(date '+%Y-%m-%d %H:%M:%S')

# -------------------------------------------------------------
# 0) Asegurarnos de que la carpeta donde van CSV y HTML exista
# -------------------------------------------------------------
DIR_BASE=$(dirname "$CSV_FILE")   # debería ser el mismo que dirname "$HTML_DEST"
if [[ ! -d "$DIR_BASE" ]]; then
    mkdir -p "$DIR_BASE"
    if [[ $? -ne 0 ]]; then
        echo "[$FECHA_HORA] ERROR: No se pudo crear directorio $DIR_BASE" >&2
        exit 1
    fi
fi

# -------------------------------------------------------------
# 1) Comprobar si el CSV existe; si no, crear con cabecera
# -------------------------------------------------------------
if [[ ! -f "$CSV_FILE" || ! -s "$CSV_FILE" ]]; then
    echo "FechaHora,USD_Compra,USD_Venta,EUR_Compra,EUR_Venta" > "$CSV_FILE"
    if [[ $? -ne 0 ]]; then
        echo "[$FECHA_HORA] ERROR: No se pudo escribir cabecera en $CSV_FILE" >&2
        exit 1
    fi
fi

# -------------------------------------------------------------
# 2) Consultar la API de USD y extraer campos con jq
# -------------------------------------------------------------
RESP_USD=$(curl -s "$API_USD")
if [[ $? -ne 0 || -z "$RESP_USD" ]]; then
    echo "[$FECHA_HORA] ERROR: No se pudo obtener JSON de USD desde $API_USD" >&2
    exit 1
fi

USD_COMPRA=$(echo "$RESP_USD" | jq -r '.compra')
USD_VENTA=$(echo "$RESP_USD" | jq -r '.venta')
if [[ -z "$USD_COMPRA" || -z "$USD_VENTA" || "$USD_COMPRA" == "null" || "$USD_VENTA" == "null" ]]; then
    echo "[$FECHA_HORA] ERROR: Campos USD no válidos (compra:$USD_COMPRA, venta:$USD_VENTA)" >&2
    exit 1
fi

# -------------------------------------------------------------
# 3) Consultar la API de EUR y extraer campos con jq
# -------------------------------------------------------------
RESP_EUR=$(curl -s "$API_EUR")
if [[ $? -ne 0 || -z "$RESP_EUR" ]]; then
    echo "[$FECHA_HORA] ERROR: No se pudo obtener JSON de EUR desde $API_EUR" >&2
    exit 1
fi

EUR_COMPRA=$(echo "$RESP_EUR" | jq -r '.compra')
EUR_VENTA=$(echo "$RESP_EUR" | jq -r '.venta')
if [[ -z "$EUR_COMPRA" || -z "$EUR_VENTA" || "$EUR_COMPRA" == "null" || "$EUR_VENTA" == "null" ]]; then
    echo "[$FECHA_HORA] ERROR: Campos EUR no válidos (compra:$EUR_COMPRA, venta:$EUR_VENTA)" >&2
    exit 1
fi

# -------------------------------------------------------------
# 4) Añadir la línea al CSV
# -------------------------------------------------------------
echo "${FECHA_HORA},${USD_COMPRA},${USD_VENTA},${EUR_COMPRA},${EUR_VENTA}" >> "$CSV_FILE"
if [[ $? -ne 0 ]]; then
    echo "[$FECHA_HORA] ERROR: No se pudo escribir en $CSV_FILE" >&2
    exit 1
fi

# -------------------------------------------------------------
# 5) Generar/Sobrescribir el index.html con la última cotización
# -------------------------------------------------------------
cat <<EOF > "$HTML_DEST"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Tienda de Divisas</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px;
    }
    h1 {
      color: #333;
      font-size: 2em;
    }
    p {
      font-size: 1.1em;
      margin: 8px 0;
    }
    footer {
      margin-top: 40px;
      font-size: 0.9em;
      color: #666;
    }
  </style>
</head>
<body>
  <h1>Tienda de Divisas</h1>

  <p><strong>Cotización del momento:</strong></p>
  <p><strong>Fecha y Hora:</strong> ${FECHA_HORA}</p>
  <p><strong>Cotización USD:</strong> Compra ${USD_COMPRA} &nbsp;|&nbsp; Venta ${USD_VENTA}</p>
  <p><strong>Cotización EURO:</strong> Compra ${EUR_COMPRA} &nbsp;|&nbsp; Venta ${EUR_VENTA}</p>

  <footer>by Ventura-Visintin.</footer>
</body>
</html>
EOF

if [[ $? -ne 0 ]]; then
    echo "[$FECHA_HORA] ERROR: No se pudo escribir el HTML en $HTML_DEST" >&2
    exit 1
fi

# -------------------------------------------------------------
# 6) Mensaje final por consola
# -------------------------------------------------------------
echo "[$FECHA_HORA] Actualizado: CSV en $CSV_FILE y HTML en $HTML_DEST"
exit 0
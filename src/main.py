import openai

# Conectarse a Ollama
client = openai.Client(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

response = client.chat.completions.create(
    model="deepseek-r1:1.5b",  # Reemplazá 1.5b con la versión elegida
    messages=[{"role": "user", "content": """
       Extract iva, total, subtotal, items and client from this text:
       Base imponible
Base imponible
170,00 €
IVA 10%

el
170,00 €
17,00 €
Total
Total
187,00 €
CHIRONLAFE, S.L.
Avda. Juan Melgarejo I 35 a 39
12500 PUERTO SANTA MARIA
España
Nº identif. fiscal (NIF):
B10786911
Factura

INV/2024/12/0150
Fecha de factura:
Fecha de factura:
17/12/2024
Fecha de vencimiento:
Fecha de vencimiento:
16/01/2025
Fecha de entrega:
Fecha de entrega:
10/12/2024
Origen:
Origen:
S06683
Descripción
Descripción
Cantidad
Cantidad
Precio
Precio
unitario
unitario
Impuestos
Impuestos
Importe
Importe
[100328] JAMÓN DE BELLOTA 100% IBÉRICO
LONCHEADO 100GR (AR)
24/1025
20,00

UD
8,50
IVA 10%
(Bienes)
170,00
 €
[100538] huesos jamón
3,44

UD
0,00
IVA 10%
(Bienes)
0,00
 €
Producto
Producto
Cantidad
Cantidad
NS/NL
NS/NL
[100328] JAMÓN DE
BELLOTA 100% IBÉRICO
LONCHEADO 100GR (AR)
20,00UD
12121081024
Comunicaciones de pago
INV/2024/12/0150
INV/2024/12/0150

en esta cuenta:
ES41 0081 5103 1300 0115 6323 - SABADELL - BSABESBBXXX
ES41 0081 5103 1300 0115 6323 - SABADELL - BSABESBBXXX
QUARENTENA FOOD S.L.
Paseo de las delicias 3 1D
41001 Sevilla
Spain
B01772839
ES41 0081 5103 1300 0115 6323 BSABESBBXXX
Página:
1

de
1
    """}],
    temperature=0.7
)

print(response)
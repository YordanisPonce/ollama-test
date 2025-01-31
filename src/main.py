import openai
import PyPDF2

def leer_pdf(ruta_pdf):
    try:
        with open(ruta_pdf, "rb") as archivo:
            lector = PyPDF2.PdfReader(archivo)
            texto = ""
            for pagina in lector.pages:
                texto += pagina.extract_text()
        return texto
    except Exception as e:
        print(f"Error al leer el PDF: {e}")
        return ""

value = leer_pdf('data/factura-4.pdf')

# Conectarse a Ollama
client = openai.Client(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

response = client.chat.completions.create(
    model="deepseek-r1:1.5b",  # Reemplazá 1.5b con la versión elegida
    messages=[{"role": "user", "content": "Extract : iva, total, subtotal, items and client from this text: {value} in json forma"}],
    temperature=0.7
)

print(response.message)
from openai import OpenAI
from dotenv import load_dotenv
import os

# .env Datei mit dem Key laden
load_dotenv()  

# Key aus Umgebungsvariable lesen
api_key = os.getenv("OPENAI_API_KEY")
# print(f"API_KEY: {api_key!r}")

# Client erstellen
client = OpenAI(api_key=api_key)

# Anfrage senden
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Give me 3 benefits of integration tests."}
    ],
    n =2, # Anzahl der Varianten
    temperature=0.3,
    max_tokens=200
    
)

# Ausgabe anzeigen
for idx, choice in enumerate(response.choices):
    print(f"Antwort {idx + 1}:\n{choice.message.content}\n")
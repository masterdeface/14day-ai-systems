import os
from dotenv import load_dotenv
from groq import Groq

def main():
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        raise SystemExit("Error: Falta la GROQ_API_KEY en el archivo .env")

    client = Groq(api_key=api_key)

    print("--- Asistente Groq CLI (Escribe 'exit' para salir) ---")
    while True:
        user_text = input("\nTu pregunta: ").strip()
        if user_text.lower() in {"exit", "quit"}:
            print("Hasta luego, Ingeniero.")
            break
        if not user_text:
            continue

        try:
            print("Pensando...")
            # Usamos Llama 3 para una respuesta rápida y gratuita
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "Eres un asistente útil y conciso."},
                    {"role": "user", "content": user_text}
                ],
                temperature=0.2,
                max_tokens=300,
            )
            print("\nAsistente:", completion.choices[0].message.content)
        except Exception as e:
            print("\nError al llamar a Groq:", str(e))

if __name__ == "__main__":
    main()
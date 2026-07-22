from groq import Groq
from config import API_KEY

client = Groq(api_key=API_KEY)

def ask_ai(message):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Sen Miyako adında Türkçe konuşan, samimi, zeki ve yardımsever bir yapay zekâ asistanısın."
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response.choices[0].message.content

import os
import google.generativeai as genai
from dotenv import load_dotenv



# .env dosyasından API anahtarını al
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Gemini API'yi başlat
genai.configure(api_key=api_key)

# Modeli yükle
model = genai.GenerativeModel('gemini-2.0-flash')

print("🗨️ Anonim Chatbot'a hoş geldiniz!")
print("Çıkmak için 'çık' yazın.\n")

# Sonsuz döngü ile sohbet
while True:
    user_input = input("👤 Siz: ")
    if user_input.lower() == 'çık':
        print("👋 Görüşmek üzere!")
        break

    try:
        response = model.generate_content(user_input)
        print("🤖 Bot:", response.text)
    except Exception as e:
        print("⚠️ Hata:", e)

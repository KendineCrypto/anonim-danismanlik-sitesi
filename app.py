from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

# API anahtarını al
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Flask uygulaması
app = Flask(__name__)

# Modeli başlat
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat(history=[])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_route():
    user_input = request.json.get("message")
    try:
        response = chat.send_message(user_input)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Hata: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)

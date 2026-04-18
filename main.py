from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ACCESS_TOKEN = "751464993858844862:iiCUxcPvkWhhyqeTFdDNsGpMIYXAxHFbdrYEVuqWqqVxEkwJmCXUmfuCBZXrnRhm"

def send_message(user_id, text):
    url = "https://openapi.zalo.me/v3.0/oa/message/cs"
    
    headers = {
        "access_token": ACCESS_TOKEN,
        "Content-Type": "application/json"
    }

    data = {
        "recipient": {
            "user_id": user_id
        },
        "message": {
            "text": text
        }
    }

    requests.post(url, json=data, headers=headers)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    try:
        msg = data["message"]["text"]
        user_id = data["sender"]["id"]

        print("User:", msg)

        reply = "Tao chưa hiểu 😆"

        if "hello" in msg.lower():
            reply = "Xin chào bro 😎"

        if "giá" in msg.lower():
            reply = "Giá từ 100k - 500k nha 🔥"

        if "ship" in msg.lower():
            reply = "Ship toàn quốc 20k - 40k 📦"

        send_message(user_id, reply)

    except Exception as e:
        print("Lỗi:", e)

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(port=5000)

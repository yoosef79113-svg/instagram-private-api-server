from flask import Flask, request, jsonify
from instagrapi import Client

app = Flask(__name__)

@app.route("/uploadReel", methods=["POST"])
def upload_reel():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    video_url = data.get("videoUrl")
    caption = data.get("caption", "")

    if not all([username, password, video_url]):
        return jsonify({"status": "error", "msg": "Missing fields"}), 400

    try:
        cl = Client()
        cl.login(username, password)
        media = cl.clip_upload(video_url, caption)
        return jsonify({"status": "success", "media_id": media.dict()})
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

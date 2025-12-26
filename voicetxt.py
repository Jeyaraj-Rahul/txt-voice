from flask import Flask, render_template, request, send_file
from PyPDF2 import PdfReader
import pyttsx3
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
AUDIO_FOLDER = "audio"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pdf = request.files["pdf"]
        voice_type = request.form.get("voice")
        speed = int(request.form.get("speed"))

        pdf_path = os.path.join(UPLOAD_FOLDER, pdf.filename)
        pdf.save(pdf_path)

        # Extract text
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        # Text to Speech
        engine = pyttsx3.init()

        # 🔊 Speed control
        engine.setProperty("rate", speed)

        # 👤 Voice selection
        voices = engine.getProperty("voices")
        if voice_type == "female":
            engine.setProperty("voice", voices[1].id)
        else:
            engine.setProperty("voice", voices[0].id)

        audio_path = os.path.join(AUDIO_FOLDER, "output.mp3")
        engine.save_to_file(text, audio_path)
        engine.runAndWait()

        return send_file(audio_path, as_attachment=True)

    return render_template("index.html")

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    app.run(debug=True)
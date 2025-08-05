
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import requests
import os

app = FastAPI()

@app.post("/convert")
async def convert(file: UploadFile = File(...)):
    """Receive WAV file, call model serving and midi2pdf services, and return PDF."""
    input_path = f"/app/sample_data/{file.filename}"
    with open(input_path, "wb") as f:
        f.write(await file.read())

    midi_path = "/app/sample_data/output.mid"
    pdf_path = "/app/sample_data/output.pdf"

    # Call model serving to generate MIDI
    requests.post("http://model_serving:8000/infer", json={"input_path": input_path, "output_path": midi_path})

    # Call midi2pdf to generate PDF
    requests.post("http://midi2pdf:8000/convert", json={"input_path": midi_path, "output_path": pdf_path})

    return FileResponse(pdf_path, media_type="application/pdf", filename="sheet_music.pdf")

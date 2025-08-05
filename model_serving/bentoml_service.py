
from fastapi import FastAPI

app = FastAPI()

@app.post("/infer")
async def infer(input_path: str, output_path: str):
    """Dummy inference service: convert input audio to MIDI file."""
    with open(output_path, "wb") as f:
        f.write(b"MIDI DATA")
    return {"status": "success", "output_path": output_path}

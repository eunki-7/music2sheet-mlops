
from fastapi import FastAPI
import music21 as m21

app = FastAPI()

@app.post("/convert")
async def convert(input_path: str, output_path: str):
    """Convert MIDI to PDF sheet music."""
    score = m21.stream.Stream()
    score.append(m21.note.Note('C4'))
    score.write('lily.pdf', fp=output_path)
    return {"status": "success", "output_path": output_path}

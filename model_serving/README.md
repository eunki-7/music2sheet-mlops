# Model Serving
Hosts the machine learning model (basic-pitch) for converting audio to MIDI using BentoML.

## Contents
- bentoml_service.py: BentoML service definition.
- inference.py: Audio-to-MIDI conversion logic.
- models/basic_pitch.onnx: Pretrained model file.
- requirements.txt: ML dependencies.
- Dockerfile: Containerizes the model service.

## Usage
Deploy with `bentoml serve` or via Docker.

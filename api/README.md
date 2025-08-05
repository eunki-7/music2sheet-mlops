# API Gateway
Acts as the API Gateway for the system, handling file uploads, calling the model service, converting MIDI to PDF, and returning the sheet music.

## Contents
- main.py: FastAPI service implementation.
- requirements.txt: Python dependencies.
- Dockerfile: Containerizes the API Gateway.

## Usage
Run locally with `uvicorn main:app --reload` or via Docker.

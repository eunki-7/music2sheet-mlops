
import streamlit as st
import requests

st.title("Music2Sheet Converter")

# Upload audio file
uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])
if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")
    if st.button("Convert to Sheet Music"):
        files = {"file": uploaded_file.getvalue()}
        # Call backend API
        response = requests.post("http://api:8000/convert", files=files)
        if response.status_code == 200:
            st.success("Conversion complete!")
            st.download_button("Download Sheet Music", data=response.content, file_name="sheet_music.pdf")
        else:
            st.error("Conversion failed, please check logs")

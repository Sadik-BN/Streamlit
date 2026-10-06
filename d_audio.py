import streamlit as st

st.title("Audio")
st.divider()

#Application's Internal Audio
st.header("Application's Internal Audio")

st.audio("audio/emotional-damage-meme.mp3",loop=True)


#Audio upload
st.header("Taking Audio upload from user")
audio_file = st.file_uploader("Select or Drag Your Audio File",
                 type=['mp3','m4a','wav','flac','ogg','wma'],
                 max_upload_size=10)

if audio_file:
    st.audio(audio_file,loop=True)

import streamlit as st

from gtts import gTTS

text="Hello World"

speech= gTTS(text,lang='en',slow=False) #This will convert text to speech

speech.save("speech.mp3") #this will save the speech audio locally

st.audio("speech.mp3") #this will provide audio to ui


#get text to speech audio without locally saving it

import io

text2="Welcome to our country"

speech2= gTTS(text2,lang='en',slow=False)

speech2_audio = io.BytesIO() #this will allocate ram space named speech2_audio

speech2.write_to_fp(speech2_audio) #this will put the speech audio in that space

st.audio(speech2_audio)
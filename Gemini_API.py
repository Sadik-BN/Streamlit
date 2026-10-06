#Setup
#API Key access from environment variables file (.env)
import os

from dotenv import load_dotenv
load_dotenv() #All environment variables loaded

apiKey = os.environ.get("GEMINI_KEY")


#Client ready
from google import genai
client = genai.Client(api_key=apiKey)

#End of setup

#UI
import streamlit as st

st.title("Let's Query With gemini-3.5-flash-lite",anchor=False)

user_text=st.text_input("",placeholder="Enter Your One Time Query Here")

btn = st.button("Submit",type="primary")

if btn:
    if user_text:
        #If user gives texts then get a response based on the text

        ### Getting Response Based on given Contents
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=user_text,
        )
        
        st.subheader("Response: ",anchor=False,divider=True)
        st.markdown(f"***:green[Gemini:]*** {response.text}")
    else:
        st.warning("Please Enter Some Texts")

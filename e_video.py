import streamlit as st

st.title("Video")
st.divider()

#Video upload
st.header("Taking Video upload from user")
video_file = st.file_uploader("Select or Drag Your Video File",
                 type=['mp4','mkv'],
                 max_upload_size=10)

btn_pressed = st.button("Upload")

if btn_pressed:
    if video_file:
        st.success("Video upload sucessfull :white_check_mark:")
        st.video(video_file,width=200)
    else:
        st.error("Didn't upload anything :x:")

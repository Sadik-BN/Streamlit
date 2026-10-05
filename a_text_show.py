import streamlit as st

st.title(":streamlit: My first Streamlit Web App")

st.title("Anchor Removed Title",anchor=False) #Anchor=false removes anchor icon beside the title

st.header("Content-1",anchor=False,divider=True) #divider will draw a line under the header

st.subheader("Content-1 Subheader")

st.text("Hello World")


# Markdown Text we can design these texts

#Bold
st.markdown("**Bold Text**")

#Italic
st.markdown("*Italic Text*")

#Font color
st.markdown(":red[***Colored Font***]") #bold+italic+color

#Text background color
st.markdown(":orange-background[:red[***Hi***], I am Sadik]")


#Emojies
#For adding emojis search in google "streamlit emoji shortcodes"
st.markdown("Prochur programming kortachi :sunglasses:")


#Showing variables
a=10 
b=20
st.write(a,b)
st.markdown("printing 1 to 10 in UI :alien: \:")
for i in range(1,11):
    st.write(i)
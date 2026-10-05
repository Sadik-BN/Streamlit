import streamlit as st

st.title(":streamlit: Taking Inputs")
st.divider() #this will create a horizontal line

#Text input
#input functions returns the inputted values
name = st.text_input("Enter Your Name",placeholder="Type Your Name") #Placeholder will place a text in input box
st.write("Your name is\: ",name)
st.divider()



#password type input + Button Concept
password = st.text_input("Enter Your password (Default:1234)", placeholder="Type your password",type="password")#there are so many types- email, phone,url... etc

isPressed=st.button("Click to confirm",type="primary") #button() returns True if pressed, #There are three types of button design primary,secondary,tertiary

if(isPressed):
    if (password=="1234"):
        st.markdown("Successfull :white_check_mark:")
    else:
        st.markdown("Incorrect :x:")

st.divider()



#Number Input
age = st.number_input("Enter Your Age: ",value=None,placeholder="Type your age") #value=None will prevent default placeholder number and placeholder="" will place a custom placeholder
st.write(f"You  are {age} years old. Or you are", age ,"years old.")
st.divider()
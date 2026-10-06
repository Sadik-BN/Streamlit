import streamlit as st

st.title(":streamlit: Taking Inputs")
st.divider() #this will create a horizontal line

#Text input
#input functions returns the inputted values
name = st.text_input("Enter Your Name",placeholder="Type Your Name") #Placeholder will place a text in input box
st.write("Your name is\: ",name)
st.divider()



#password type input + Button Concept + error handle
password = st.text_input("Enter Your password (Default:1234)", placeholder="Type your password",type="password")#there are so many types- email, phone,url... etc

isPressed=st.button("Click to confirm",type="primary") #button() returns True if pressed, #There are three types of button design primary,secondary,tertiary

if(isPressed):
    if (password=="1234"):
        st.success("Successfull :white_check_mark:")
    else:
        st.error("Incorrect :x:")

st.divider()



#Number Input
age = st.number_input("Enter Your Age: ",value=None,placeholder="Type your age") #value=None will prevent default placeholder number and placeholder="" will place a custom placeholder
st.write(f"You  are {age} years old. Or you are", age ,"years old.")
st.divider()


#Selection input #Returns selected option
professions= ["Student","Employee","Businessman"]
selected = st.selectbox("Choose your profession",
                        professions,index=None,
                        placeholder="Select Your Profession",
                        accept_new_options=True)
#professions can be tupple too 

#index=None keeps selectbox empty with the placeholder, also there will appear an option to clear the box. Else first option will be selected initially

#accept_new_options=True will make user able to add a option by his own. else the only given options will be selectable

#There are other type of select boxes like radiobox, multiple selectbox etc

st.write(f"You selected {selected}")
st.divider()

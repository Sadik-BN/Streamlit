import streamlit as st

st.title("Images")

#Taking Image upload from user
st.subheader("Taking Image upload from user")
image = st.file_uploader("Select or Drag Your Image",
                 type=['jpg','jpeg','png'],
                 max_upload_size=1)
#Image upload box will appear and uploaded image will save to image variable
#type=[] defines which type of files can be uploaded we can add more types upload other files tahn image too
#max upload size is in MB. Maximum 1MB


#Show Image 
if image:
    st.text(f"{image}") #This will print details of image
    st.image(image)
#we need to give it a condition cause initially image stores None till we upload an image. So st.image() will give error. if image is None then this will not execute
st.divider()



#Multiple Uploads
st.subheader("Multiple Uploads")
images = st.file_uploader("Select or Drag Your Images",
                 type=['jpg','jpeg','png','webp'],
                 accept_multiple_files=True)
#accept_multiple_files=True will enable multiple uploads and keep them serially in image variable. If we show them later they will appear serially

#Show in columns
if images:
    col=st.columns(len(images)) #this will create a object named col which size will be the number of images cause len(images) determines the elements inside images.

    #now show each images in each columns
    for i,img in zip(range(len(images)) , images): # this means, for i in range(<number of images>): also for img in images: together.We use zip() to iterate through multiple same sized structure. Another method is "for i,img in enumerate(images):"
        with col[i]:
            st.image(img)
st.divider()



#Application's internal Image show
st.subheader("Application's internal Image show")

st.image("Images/francis.webp")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4W5se-3sXcI-CuvSm5GbPoSk655stnvqEeWyX1M79KA&s=10")

st.divider()


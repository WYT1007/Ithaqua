import streamlit as st
st.title("Ithaqua,my sun")
st.header("Lord of Babel, King of the Tower")
st.subheader("His real name, perhaps the only person in the world who knows it, can no longer call out his voice, and that doesn't matter to him anymore.")
st.text("My dear brother, watch how the ants under your feet break free from their shackles and bring down the sun.")

st.markdown("this is an image:https://b0.bdstatic.com/4b64cc74f52dfa56cde28d7cd8043bb0.jpg@h_1280")

if st.checkbox("Show/Hide"):
    st.text("You checked the box")


status = st.radio("select gender:" ,
                  ('Male',
                   'Female'))
if status == 'Male':
    st.success("Male")
else:
    st.success("Female")

hobbies = st.multiselect("Hobbies:",
               ['Reading',
                'Writing',
                'Coding',
                'Traveling'])
st.write("You selected: ", hobbies)

if st.button("about"):
    st.text("Streamlit is a great tool")

name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write("Hello, ", name)

level = st.slider("Select your level", 1, 5)
st.write("You selected: ", level)

from fastai.vision.all import *
upload_img = st.file_uploader("Upload an image",
                               type=['jpg',
                                      'png'])

if upload_img is not None:
    img = PILImage.create(upload_img)
    st.image(img.to_thumb(256,256), 
             caption="Uploaded Image")

    

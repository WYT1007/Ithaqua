import streamlit as st
st.title("Ithaqua,my sun")
st.header("Lord of Babel, King of the Tower")
st.subheader("His real name, perhaps the only person in the world who knows it, can no longer call out his voice, and that doesn't matter to him anymore.
")
st.text("My dear brother, watch how the ants under your feet break free from their shackles and bring down the sun
")

st.markdown("this is an image:https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E4%BC%8A%E5%A1%94%E5%BA%93%E4%BA%9A&hs=0&pn=1&spn=0&di=7360350738658099201&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&ie=utf-8&oe=utf-8&cl=2&lm=-1&cs=2049723241%2C3858745494&os=4011166354%2C3849134431&simid=3480176788%2C394560162&adpicid=0&lpn=0&ln=30&fr=ala&fm=&sme=&cg=&bdtype=0&oriquery=%E4%BC%8A%E5%A1%94%E5%BA%93%E4%BA%9A&objurl=https%3A%2F%2Fb0.bdstatic.com%2F4b64cc74f52dfa56cde28d7cd8043bb0.jpg%40h_1280&fromurl=ipprf_z2C%24qAzdH3FAzdH3F4k1_z%26e3Bkwt17_z%26e3Bv54AzdH3Fgjofrw2jAzdH3F1wpwAzdH3F1pswg1tg2otfj%3Fgt1%3D1p_ca08b9amdl88mdmnd08%26f576vjF654%3Di54jrw2j&gsm=&islist=&querylist=&dyTabStr=MCwyLDMsMSw2LDQsNSw3LDgsOQ%3D%3D")

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

    

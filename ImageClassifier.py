import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import base64

st.set_page_config(page_title="X-Ray Image Classifier", layout="centered")

# ======== FUNCTION TO ADD BACKGROUND IMAGE ========
def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call it here (use your image path)
add_bg_from_local("C://Users//Admin//OneDrive//Desktop//X-ray_cllassification//X-Ray Image Classification//rangi.jpg")


st.markdown("<h1 style='color: black;'>X-Ray Image Classifier by Breezy_yrn</h1>", unsafe_allow_html=True)
img_size = 100
PRETRAINED_MODEL_PATH = "C://Users//Admin//OneDrive//Desktop//X-ray_cllassification//X-Ray Image Classification//custom_pre_trained_model_mwisho5.h5"
CATEGORIES = ["NORMAL", "PNEUMONIA"]

model = tf.keras.models.load_model(PRETRAINED_MODEL_PATH)
print('Model Loaded')


def load_classifier():
    st.subheader("Upload an X-Ray image to detect if it is Normal or Pneumonia")
    file = st.file_uploader(label=" ", type = ['jpeg'])

    if file!= None:
        img=tf.keras.preprocessing.image.load_img(file, target_size=(img_size,img_size))
        new_array=tf.keras.preprocessing.image.img_to_array(img)
        new_array = new_array.reshape(-1,img_size,img_size,3)
        st.image(file)
        st.write("")
        st.write("")
            
        if st.button("PREDICT"):
            #Making prediction
            preds = "" 
            prediction=model.predict(new_array/255.0)
            print(prediction)
            print(round(prediction[0][0]))
            preds = CATEGORIES[int(round(prediction[0][0]))] + " - " +  str(round(prediction[0][0]*100,2)) + "%"
            st.write(preds)

def main():
    load_classifier()


if __name__ == "__main__":
	main()

    


    
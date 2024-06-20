import streamlit as st
import cv2
import numpy as np
import face_recognition
import pandas as pd

st.set_page_config(
    page_title="Attendance System", page_icon="📊", layout="wide"
)
st.title("Add New Member")
st.write("---")
filled = True
with st.container():

    c1, c2 = st.columns((1, 2))
    with c1:
        name = st.text_input("Enter member name")
        if name == "":
            filled = False
    with c2:
        img_file_buffer = st.camera_input(
            "Take a picture For new member", key="camera")

        if img_file_buffer is not None:
            # To read image file buffer with OpenCV:
            bytes_data = img_file_buffer.getvalue()
            cv2_img = cv2.imdecode(np.frombuffer(
                bytes_data, np.uint8), cv2.IMREAD_COLOR)
            gray = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
            face_cascade = cv2.CascadeClassifier("Attendance-System-Project/haarcascade_frontalface_default.xml")
            #faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5) 
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(cv2_img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            print("Number of Faces Detected: ", len(faces))
            if len(faces) > 1:
                st.write(
                    "There is more than one face in the image, please take another image.")
            elif len(faces) < 1:
                st.write("No face detected")
            else:
                st.write("Image Taken, Please Click Save")

    with c1:
        if st.button("Save Member"):
            if filled:
                path = "Attendance-System-Project/Dataset/"+name+".jpg"
                height, width = cv2_img.shape[:2]
                cv2_resized_img = cv2.resize(
                    cv2_img, (int(width/2), int(height/2)))

                cv2.imwrite(path, cv2_resized_img)
                img = face_recognition.load_image_file(path)
                img_encoding = face_recognition.face_encodings(img)[0]
                df = pd.read_csv("Attendance-System-Project/Encodings/encodings.csv")
                en = df["Encodings"].tolist()
                n = df["Persons"].tolist()
                en.append(img_encoding)
                n.append(name)
                df = pd.DataFrame({"Persons": n, "Encodings": en})
                df.to_csv("Attendance-System-Project/Encodings/encodings.csv", index=False)
                st.write("Member Added")
            else:
                st.warning("Please Enter Member Name")

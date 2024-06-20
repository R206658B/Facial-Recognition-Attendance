import streamlit as st
from datetime import datetime
import pandas as pd

st.set_page_config(
    page_title="Attendance System"
)

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("Attendance-System-Project/coh_logo.png", width=155)

st.header(':rainbow[KANZURU ATTENDANCE SYSTEM!]', divider='rainbow')
st.image("Attendance-System-Project/rowan_martin.jpg")

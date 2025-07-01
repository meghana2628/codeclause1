# app.py
import streamlit as st
import cv2
import numpy as np
from object_detection import detect_objects

st.title("🚁 Autonomous Drone Dashboard")
st.write("Live object detection and decision-making view.")

run = st.checkbox('Start Camera')

FRAME_WINDOW = st.image([])

cap = cv2.VideoCapture(0)

while run:
    ret, frame = cap.read()
    frame = detect_objects(frame)
    FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
cap.release()

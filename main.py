import streamlit as st
import time
from streamlit_gsheets import GSheetsConnection

[connections.gsheets]
spreadsheet = "https://docs.google.com/spreadsheets/d/1fvsxY8b0mWXQbeTJpZ79RJGHhaMPutBEairMeDBB8Ps/edit?usp=drivesdk"

title = "의견이 전송되었습니다."

st.header("1-7 학급 소통함")


input = st.text_input("text", key="text")    

st.write(input)
if st.button("submit"):
    st.header(title)
    time.sleep(1)
    st.session_state["text"] = ""

import streamlit as st
import time

title = "의견이 전송되었습니다."

st.header("1-7 학급 소통함")

user_input = st.text_input("의견을 입력하세요.")
if st.button("submit"):
    st.header(title)
    time.sleep(1)
    title = ""

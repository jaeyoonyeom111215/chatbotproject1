import streamlit as st
import time

title = "의견이 전송되었습니다."

st.header("1-7 학급 소통함")


input = st.text_input("text", key="text")    

st.write(input)
if st.button("submit"):
    st.header(title)
    time.sleep(1)
    st.session_state["text"] = ""

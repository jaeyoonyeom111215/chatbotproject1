import streamlit as st
import time

title = "의견이 전송되었습니다."

st.header("1-7 학급 소통함")

def clear_text():
    st.session_state["text"] = ""

input = st.text_input("text", key="text")    
st.button("clear text input", on_click=clear_text)
st.write(input)
if st.button("submit"):
    st.header(title)
    time.sleep(1)
    title = ""

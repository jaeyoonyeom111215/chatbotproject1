import streamlit as st
import time

title = "고민, 학급 건의사항 등을 적어주십시오."

st.header("1-7 학급 소통함")
st.subheader(title)

    
user_input = st.text_input("의견을 입력하세요.")
if st.button("submit"):
    st.text_input("의견이 전송되었습니다.")
    time.sleep(1)
    st.text_input("")

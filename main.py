import streamlit as st
from google.cloud import firestore

db = firestore.Client.from_service_account_json("streamlit-reddit-e1aba-firebase-adminsdk-1lcvf-10fc77da33.json")

title = "의견이 전송되었습니다."

st.header("1-7 학급 소통함")

input_text = st.text_input("text", key="text")    

st.write(input_text)

if st.button("submit"):

    doc_ref = db.collection("posts").document(title)
    doc_ref.set({
        "title": title,
        "url": input_text
    })

    st.session_state["text"] = ""
    st.text_input("text", key="text", value="")

posts_ref = db.collection("posts")
st.header(title)

try:
    for doc in posts_ref.stream():
        post = doc.to_dict()

except Exception as e:
    st.error("Firestore에서 문서를 가져오는 중 오류가 발생했습니다: {}".format(str(e)))

import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import cv2
from PIL import Image
import numpy as np

# 웹캠 액세스
cam = cv2.VideoCapture(0)

# 이미지 캡처 버튼
capture_image = st.button("Capture Image")

# 캡처된 이미지 저장
if capture_image:
    ret, img = cam.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    st.image(img, channels="RGB")
    pil_img = Image.fromarray(img)
    
    model_id = "vikhyatk/moondream2"
    revision = "2024-03-06"
    
    model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True, revision=revision)
    tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)
    
    # 사용자 질문 입력
    user_question = st.text_input("Enter your question here:")
    
    if user_question:
        enc_image = model.encode_image(pil_img)
        result = model.answer_question(enc_image, user_question, tokenizer)
        st.write(f"Answer: {result}")

# 웹캠 해제
cam.release()
cv2.destroyAllWindows()


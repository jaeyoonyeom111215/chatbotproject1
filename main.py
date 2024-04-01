import streamlit as st
from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer
from PIL import Image
import cv2
import torch

# 모델 및 토크나이저 로드
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTFeatureExtractor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def main():
    st.title("Webcam Image Captioning and Chat")

    # 대화 내용을 저장할 리스트
    conversation = []

    cap = cv2.VideoCapture(0)

    if st.button("Capture Image"):
        ret, frame = cap.read()

        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values
        pixel_values = pixel_values.to(device)
        output_ids = model.generate(pixel_values, max_length=50, num_beams=4, early_stopping=True)
        caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)

        # 캡션을 대화 리스트에 추가
        conversation.append({"user": "User", "message": "Captured Image"})
        conversation.append({"user": "Model", "message": caption})

        st.image(frame, caption=caption, use_column_width=True)

    # 대화 내용을 출력
    for conv in conversation:
        st.text(f"{conv['user']}: {conv['message']}")

    cap.release()

if __name__ == "__main__":
    main()


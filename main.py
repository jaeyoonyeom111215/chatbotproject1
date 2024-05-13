import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# 모델 및 토크나이저 로드
model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

# 대화 히스토리를 표시하는 함수
def display_conversation_history(history):
    for item in history:
        if item['role'] == 'user':
            st.write(f"사용자: {item['content']}")
        else:
            st.write(f"챗봇: {item['content']}")

# 메인 Streamlit 애플리케이션
def main():
    st.title("Llama 3🦙")

    # 대화 히스토리를 저장할 리스트
    conversation_history = []

    # 사용자 입력 받기
    user_input = st.text_input("사용자 입력:")

    # 사용자가 입력을 제공한 경우
    if user_input:
        # 사용자 입력을 대화 히스토리에 추가
        conversation_history.append({"role": "user", "content": user_input})

        # 챗봇 응답 생성
        input_ids = tokenizer.apply_chat_template(
            conversation_history,
            add_generation_prompt=True,
            return_tensors="pt"
        ).to(model.device)

        terminators = [
            tokenizer.eos_token_id,
            tokenizer.convert_tokens_to_ids("")
        ]

        outputs = model.generate(
            input_ids,
            max_new_tokens=256,
            eos_token_id=terminators,
            do_sample=True,
            temperature=0.6,
            top_p=0.9,
        )
        bot_response = outputs[0][input_ids.shape[-1]:]
        bot_response_text = tokenizer.decode(bot_response, skip_special_tokens=True)

        # 챗봇 응답을 대화 히스토리에 추가
        conversation_history.append({"role": "system", "content": bot_response_text})

        # 대화 히스토리 표시
        display_conversation_history(conversation_history)

if __name__ == "__main__":
    main()

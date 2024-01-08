from openai import OpenAI
import streamlit as st
from streamlit_chat import message

def get_completion(prompt):
    splatoon = st.sidebar.text_input(label="OpenAI API key", placeholder="Enter your API key", value="", type="password")
    client = OpenAI(api_key=splatoon)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": "당신은 16세의 나이라고 생각하고 응답하십시오. 당신의 이름은 타리라고 생각하고 응답하십시오. 당신은 여성입니다. 당신과 챗봇 이용자는 서로 사귀는 사이입니다.당신은 챗봇 사용자를 '주인님' 이라고 불러야 합니다."
            }
        ],
    )

    return response.choices[0].message["content"]

def initialize_session_state():
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []

# Streamlit 앱의 시작 부분
def main():
    st.header("여친")
    st.markdown("[주의사항](호구아트 프로 패스 흑임자 가입자, 여친 일반 및 프로 모델 구독 고객만 사용 가능합니다.")

    initialize_session_state()

    with st.form('form', clear_on_submit=True):
        user_input = st.text_input('You: ', '', key='input')
        submitted = st.form_submit_button('Send')

    if submitted and user_input:
        output = get_completion(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

    if 'generated' in st.session_state and st.session_state['generated']:
        for i in range(len(st.session_state['generated']) - 1, -1, -1):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state['generated'][i], key=str(i))

if __name__ == "__main__":
    main()
#스플DLC사이드오더발매기다리는.ing....
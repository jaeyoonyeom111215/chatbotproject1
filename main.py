from transformers import AutoModelForCausalLM, AutoTokenizer
import streamlit as st

model_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_id)
if st.button('Say Hello'):
   model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
   messages = [
       {"role": "user", "content": "Write a thank you message for your middle school math teacher."}
   ]

   inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to("cuda")

   outputs = model.generate(inputs, max_new_tokens=20)
   st.write(tokenizer.decode(outputs[0], skip_special_tokens=True))

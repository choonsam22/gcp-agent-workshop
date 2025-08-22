import streamlit as st
from agent_with_tool import run

st.set_page_config(page_title="AI Agent Demo")
st.title("AI Agent (GCP)")

query = st.text_input("질문을 입력하세요")
if st.button("질문하기"):
    with st.spinner("생각 중..."):
        answer = run(query)
    st.write(answer)

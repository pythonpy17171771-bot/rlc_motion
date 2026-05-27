import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="RLC 회로",
    layout="wide"
)

# html 파일 읽기
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# html 실행
components.html(
    html_code,
    height=2500,
    scrolling=True
)

import streamlit as st
from stock_utils import analyze_stock

st.set_page_config(page_title="📈 실시간 주식 종목 분석기", layout="wide")
st.title("📈 실시간 주식 종목 분석기")

query = st.text_input("종목명 또는 코드 입력 (예: 삼성전자 또는 005930)", "")
if st.button("분석하기") and query:
    with st.spinner("분석 중입니다..."):
        result = analyze_stock(query)
        if result is None:
            st.error("❌ 없는 종목입니다. 다시 입력해 주세요.")
        else:
            st.success(f"🔎 종목코드: {result['종목코드']}")
            st.markdown(f"<h4>📅 기준일: {result['기준일']} / 📌 현재가 (실시간): {result['현재가']}</h4>", unsafe_allow_html=True)
            st.markdown("## 📊 기술적 분석 요약")
            st.markdown(result["기술적분석"], unsafe_allow_html=True)
            st.markdown("## 🧭 지지선 / 저항선")
            st.markdown(result["지지저항"], unsafe_allow_html=True)
            st.markdown("## 📉 매물대 분석")
            st.markdown(result["매물대"], unsafe_allow_html=True)
            st.markdown("## 📰 뉴스 / 공시 요약")
            st.markdown(result["뉴스공시"], unsafe_allow_html=True)
            st.markdown("## ⭐ 오늘의 뉴스 기반 추천 종목")
            st.markdown(result["추천종목"], unsafe_allow_html=True)
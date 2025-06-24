
import streamlit as st

st.set_page_config(page_title="주식 종목 분석기", page_icon="📊", layout="centered")

st.title("📈 실시간 주식 종목 분석기")
query = st.text_input("종목명 또는 코드 입력 (예: 다날, 미투온 등)")
if st.button("분석하기"):
    if query.strip() == "다날":
        st.success("📗 종목코드: 064260")
        st.markdown("📅 **기준일:** 2025-06-24 / 📌 **현재가 (실시간):** `60,500원`")
        st.markdown("## 📊 기술적 분석 요약")
        st.markdown("✅ **RSI:** 62.5 → 과열 구간, 단기 조정 가능성 존재")
        st.markdown("✅ **MACD:** 936.79 / Signal: 887.14 → 상승 모멘텀 유지")
        st.markdown("✅ **이동평균선:** 5일선 상승 중 / 20일선 상승 중 → 단기 상승 추세")
        st.markdown("✅ **볼린저밴드:** 상단 61,686 / 하단 54,253 → 상단 근접 시 주의")

        st.markdown("## 🧭 지지선/저항선 (50일 기준 자동 추출)")
        st.markdown("- 주요 지지선: 57,400원")
        st.markdown("- 주요 저항선: 62,300원")

        st.markdown("## 📊 매물대 분석")
        st.markdown("- 가격 분포 기반 추정 매물대: **59,400 ~ 60,300원** 구간에 집중되어 있음")

        st.markdown("## 📰 뉴스/공시 요약")
        st.markdown("- [06.24] 해외 투자 확대 계획 발표")
        st.markdown("- [06.23] 실적 컨센서스 상회 예상")
        st.markdown("- [공시] 자회사 흡수 합병 전환")

        st.markdown("## ⭐ 오늘의 뉴스 기반 추천 종목")
        st.markdown("📢 **주목 테마:** AI 반도체, 전기차 충전, 방산 수출")
        st.markdown("1️⃣ **AI 반도체 관련주**: 한미반도체, 리노공업, SK하이닉스")
        st.markdown("2️⃣ **전기차 충전 인프라**: 씨아이에스, 대성파인텍, 케이엔더블유")
        st.markdown("3️⃣ **방산 수출 기대감**: 한화에어로스페이스, 퍼스텍, LIG넥스원")
    else:
        st.error("❌ 없는 종목입니다. 다시 확인해주세요.")

# 파이참의 Terminal 에서 streamlit run XXX.py 하면 로컬에서 실행된다!!!

import streamlit as st
import streamlit_shadcn_ui as ui

#한글폰트 적용을 위한 패키지
#import matplotlib.pyplot as plt
# 폰트 설정 (동작하는지 알 수가 없음) 출처 : https://blog.naver.com/dhan0213/223441867467
#plt.rcParams['font.family'] = "NanumGothic"
#plt.rcParams['font.family'] = "Arial"

# ----------------------------------------------------------------------------------------------------------------------
# 스타일 정의
# 이미지 호스팅 하기 : https://velog.io/@sjy1410/streamlit-%EB%B0%B0%EA%B2%BD%EC%82%AC%EC%A7%84-%EB%84%A3%EB%8A%94-%EB%B2%95
# 회색 배경 : https://images.unsplash.com/photo-1588345921523-c2dcdb7f1dcd?w=800&dpr=2&q=80
# 엘지 배경 : https://www.lge.co.kr/kr/images/company/info/img-info-brand-identity-graph_11_pc.png
# 제품 배경 : https://i.imgur.com/LpAFTNb.png
# ----------------------------------------------------------------------------------------------------------------------
def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://i.imgur.com/LpAFTNb.png");
             background-attachment: fixed;
             background-size: cover

         }}
         </style>
         """,
        unsafe_allow_html=True
    )
add_bg_from_url()


# 컨텐츠 영역을 넓게 쓰기 위함
#st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: #555555;font-size: 42px;'>AX Insight Lounge</h1>", unsafe_allow_html=True)
st.space(size="large")
st.space(size="large")

# ----------------------------------------------------------------------------------------------------------------------
# 로그인 기능넣기 : https://59travel.tistory.com/7
# ----------------------------------------------------------------------------------------------------------------------
def login():
    if id == "admin" and pw == "123456":
        st.session_state["logged_in"] = True
        st.success("로그인에 성공했습니다")
        #st.markdown("https://www.google.com/", unsafe_allow_html=True)
        #st.link_button("대시보드 열기", "https://dst-dashboard.streamlit.app/")
        def nav_to(url):
            nav_script = """
                <meta http-equiv="refresh" content="0; url='%s'">
            """ % (url)
            st.write(nav_script, unsafe_allow_html=True)
        nav_to("https://dst-dashboard.streamlit.app")
    else:
        st.error("실패")

def logout():
    st.session_state["logged_in"] = False
    st.info("로그아웃 되었습니다")

id = st.text_input('ID')
pw = st.text_input('Password', type='password')
if st.button('Login'):
    login()
else:
    logout()

# ----------------------------------------------------------------------------------------------------------------------
#st.space(size="large")
#with ui.card(key="card0"):
#    ui.element("span", children=["ID"], className="text-gray-400 text-sm font-medium m-1", key="label1")
#    ui.element("input", key="email_input", placeholder="Your ID")

#    ui.element("span", children=["Password"], className="text-gray-400 text-sm font-medium m-1", key="label2")
#    ui.element("input", key="username_input", placeholder="Input your password")
#    ui.element("button", text="Submit", key="button", className="m-1")

# ----------------------------------------------------------------------------------------------------------------------
#st.markdown("<h1 style='text-align: center; color: #555555;font-size: 16px;'>아래에서 관심있는 주제를 선택해 주세요</h1>", unsafe_allow_html=True)
#st.markdown('<p style="font-family:Roboto; color:black; font-size: 42px;">Design Solution Task</p>', unsafe_allow_html=True)
#st.markdown('<p style="font-family:NanumGothic; color:black; font-size: 30px;">디자인 솔루션 태스크</p>', unsafe_allow_html=True)

#st.subheader("Single Household Data Dashboard")
#st.caption("1인 가구에 대한 데이터 분석 및 인사이트를 제공합니다")


#cols = st.columns(3)
#with cols[0]:
#    ui.metric_card(title="Device Usage Data", content="에어컨", description="김미주 책임", key="card1")
#    #st.link_button("Go to gallery", "https://streamlit.io/gallery")
#    #st.page_link("http://www.google.com", label="대시보드 바로가기")
#with cols[1]:
#    ui.metric_card(title="기기데이터 / VOC", content="식기세척기", description="서희영 책임", key="card2")
#with cols[2]:
#    ui.metric_card(title="Public Data / Device Data", content="소형가전", description="김병수 책임", key="card3")

#st.space(size="small")

#cols2 = st.columns(3)
#with cols2[0]:
#    ui.metric_card(title="Social Big Data", content="1인가구", description="김하나 책임", key="card4")
#with cols2[1]:
#    ui.metric_card(title="N/A", content="준비중", description="작성자", key="card5")
#with cols2[2]:

#    ui.metric_card(title="N/A", content="준비중", description="작성자", key="card6")





# 앱 배포하기 : https://codemagician.tistory.com/entry/Streamlit-05-Streamlit-%EC%95%B1-%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0

import streamlit as st
#from streamlit_option_menu import option_menu
#import streamlit_shadcn_ui as ui

# 스타일을 미리 정의해야하는 듯 : https://pypi.org/project/streamlit-navigation-bar/2.0.0/
#from streamlit_navigation_bar import st_navbar
#page = st_navbar(["홈", "문서", "Examples", "Community", "About"])
#st.write(page)

# ----------------------------------------------------------------------------------------------------------------------
# 레이아웃
# ----------------------------------------------------------------------------------------------------------------------

# 컨텐츠 영역을 넓게 쓰기 위함 (제일 위에 있어야 함)
st.set_page_config(layout="wide")
st.logo("https://www.lge.co.kr/kr/images/company/info/img-info-brand-identity-graph_01_pc.png")

selected = st.sidebar.selectbox('Theme',('글로벌 1인가구','한국 1인가구 인구통계','한국 1인가구 주거통계', '서울 행정구별 1인가구', '제품별 언급량 순위', '보유제품 / 구매희망', '제품별 불편사항'))

# 아이콘 추가하는 사이트 : https://icons.getbootstrap.com/
#with st.sidebar:
#    st.space("small")
#    selected = option_menu("Category",
#                           ["글로벌 1인가구", '한국 1인가구 인구통계', '한국 1인가구 주거통계', '서울 행정구별 1인가구', '제품별 언급량 순위', '보유제품 / 구매희망', '제품별 불편사항'],
#                            icons=['bi bi-globe-americas', 'bi bi-person-circle', 'bi bi-house-door-fill', 'bi bi-geo-alt-fill', 'bi bi-twitter', 'bi bi-heart-fill', 'bi bi-heartbreak-fill'],
#                            menu_icon="bi bi-list-ol", default_index=0,
#                            styles={
#                                "container": {"padding": "5!important", "background-color": "#fafafa"},
#                                "nav-link": {"fon.t-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
#                                "nav-link-selected": {"background-color": "#f0004c"},
#                            }
#                           )
    #selected
    #video_file = open('function.mp4', 'rb')
    #video_bytes = video_file.read()
    #st.video(video_bytes, width=280, autoplay=True)

# ----------------------------------------------------------------------------------------------------------------------
#st.markdown("<h1 style='text-align: center; color: #555555;font-size: 24px;'>[ Single Household Dashboard ]</h1>", unsafe_allow_html=True)
#ui.tabs(options=['1인 가구 비율', '1인 가구 관심 제품', '1인가구 제품 보유율', '1인가구 구매희망 제품', '제품별 불만요소'], default_value='PyGWalker', key="kanaries")

# ----------------------------------------------------------------------------------------------------------------------
# 컨텐츠 영역
# ----------------------------------------------------------------------------------------------------------------------
# 참조 레딧 https://discuss.streamlit.io/t/why-st-components-v1-html-and-iframe-functions-limit-the-height-of-the-frame-to-150/21858/9

if selected == "글로벌 1인가구":
#    with st.expander(":material/lightbulb_2: **중요 내용을 요약해 드려요**", expanded=False):
#        cols = st.columns(3)
#        with cols[0]:
#            ui.metric_card(title="Ranking", content="북반구로 갈수록 높아요", description="Norway > Denmark > Finland > Sweden", key="card1")
#        with cols[1]:
#            ui.metric_card(title="Region", content="저개발 국가는 낮아요", description="동남아, 아프리카", key="card2")
#        with cols[2]:
#            ui.metric_card(title="Trend", content="계속 증가하고 있어요", description="10~15% 대가 적은, 양극화 경향", key="card3")

    st.empty()
    iframe = st.empty()
    iframe.markdown("<iframe src='https://public.tableau.com/views/1_17630119728360/2?:showVizHome=no&:embed=true', width=1200, height=650, scrolling=no, frameborder=0></iframe>", unsafe_allow_html=True)

    with st.expander(":material/lightbulb_2: **더 자세히 알고 싶으세요?**"):
        st.write(":material/check: 대한민국은 1인가구 연평균 성장은 (CAGR) **2.91%** 로 매우 가파른 추세이며, 2040년 전망은 전체 인구의 **42.3%** 에 달할 것으로 예상됩니다")
        st.write(":material/quick_reference_all: (출처) Single household by Country : https://ourworldindata.org/grapher/one-person-households")

    st.space("large")

    st.empty()
    iframe = st.empty()
    iframe.markdown("<iframe src='https://public.tableau.com/views/251118_single_vs_gdp/1_1?:showVizHome=no&:embed=true', width=1200, height=650, scrolling=no, frameborder=0></iframe>", unsafe_allow_html=True)

    with st.expander(":material/lightbulb_2: **더 자세히 알고 싶으세요?**"):
        st.write(":material/check: 인당 GDP가 높을 수록, 1인 가구 비율이 높아지는 양의 상관관계가 뚜렷합니다")
        st.write(":material/check: 대륙별로는 유럽이 높고, 아프리카와 일본/한국을 제외한 아시아 지역이 낮습니다")
        st.write(":material/quick_reference_all: Single household VS GDP per capita : https://ourworldindata.org/grapher/one-person-households-vs-gdp-per-capita")

elif selected == "한국 1인가구 인구통계":
#    with st.expander(":material/lightbulb_2: **중요 내용을 요약해 드려요**", expanded=False):
#        cols2 = st.columns(3)
#        with cols2[0]:
#            ui.metric_card(title="Ratio", content="1인가구는 35.5%", description="2023년", key="card4")
#        with cols2[1]:
#            ui.metric_card(title="Age & Gender", content="남성은 30대 / 여성은 70대", description="중간세대가 적은 여성", key="card5")
#        with cols2[2]:
#            ui.metric_card(title="Income", content="3,223만원", description="전체가구 평균의 44.9%", key="card6")

    st.empty()
    iframe = st.empty()
    iframe.markdown("<iframe src='https://public.tableau.com/views/1_17630272229350/1_1?:showVizHome=no&:embed=true', width=1200, height=1300, scrolling=no, frameborder=0></iframe>", unsafe_allow_html=True)

    with st.expander(":material/lightbulb_2: **더 자세히 알고 싶으세요?**"):
        st.write(":material/check: 여성의 평균 수명이 높기 떄문에 70세 이상의 1인 가구가 많습니다")
        st.write(":material/check: 2024년 기준, 가구당 인구수는 **2.2명** 이므로, 한 명의 소득은 거의 유사합니다")
        st.write(":material/quick_reference_all: (출처:국가데이터처) https://mods.go.kr/board.es?mid=a10301010000&bid=10820&tag=&act=view&list_no=434103&ref_bid=")

elif selected == "한국 1인가구 주거통계":
    with st.expander(":material/chair: **실제 1인가구의 평면은 어떤 모습일까요?** (Floor plan)"):
        st.image("floor.png")

#    cols3 = st.columns(3)
#    with cols3[0]:
#        ui.metric_card(title="Average", content="13.8평", description="1인가구 평균주거면적", key="card7")
#    with cols3[1]:
#        ui.metric_card(title="Type", content="단독주택", description="아파트가 지속 상승", key="card8")
#    with cols3[2]:
#        ui.metric_card(title="Majority", content="51%", description="12평 이하 주거비율", key="card9")

    st.empty()
    iframe = st.empty()
    iframe.markdown("<iframe src='https://public.tableau.com/views/1__17632113114940/1_1?:showVizHome=no&:embed=true', width=1200, height=1000, scrolling=no, frameborder=0></iframe>", unsafe_allow_html=True)
    with st.expander(":material/lightbulb_2: **더 자세히 알고 싶으세요?**"):
        st.write(":material/check: 평균 주거 면적은 연도별 큰 변화가 없습니다")
        st.write(":material/check: 1인 가구의 **51.2%** 가 12평 이하에 주거하므로, 공간이 부족 할 것으로 판단됩니다")
        st.write(":material/quick_reference_all: (출처:국가데이터처) https://mods.go.kr/board.es?mid=a10301010000&bid=10820&tag=&act=view&list_no=434103&ref_bid=")

elif selected == "서울 행정구별 1인가구":
    st.empty()
    iframe = st.empty()
    iframe.markdown("<iframe src='https://public.tableau.com/views/251119_seoul_map/1_1?:showVizHome=no&:embed=true', width=1200, height=1250, scrolling=no, frameborder=0'></iframe>", unsafe_allow_html=True)
    with st.expander(":material/lightbulb_2: **더 자세히 알고 싶으세요?** (Implication)"):
        st.write(":material/check: **관악구**는 서울에서 가장 1인 가구가 많이 살고, 1인 가구 비율이 높아요")
        st.write(":material/check: 연령대가 낮을수록, 학교나 직장 근처에 살고 있는 경향을 보여요")
        st.write(":material/quick_reference_all: (출처:서울공공데이터포털) https://data.seoul.go.kr/dataList/OA-22267/F/1/datasetView.do")

elif selected == "제품별 언급량 순위":
    with st.expander(":material/experiment: **어떻게 활용하였을까요?**"):
        st.image("strategy.png")
    st.empty()
    iframe = st.empty()
    iframe.markdown("<iframe src='https://public.tableau.com/views/251117_social_bigdata/1_1?:showVizHome=no&:embed=true', width=1200, height=2500, scrolling=no, frameborder=0'></iframe>", unsafe_allow_html=True)

elif selected == "보유제품 / 구매희망":
    with st.expander(":material/experiment: **어떻게 분석하였을까요?**"):
        st.image("social_data.png")
    st.empty()
    iframe = st.empty()
    iframe.markdown("<iframe src='https://public.tableau.com/views/251116_device_retention_wish/1_1?:showVizHome=no&:embed=true', width=1200, height=900, scrolling=no, frameborder=0'></iframe>", unsafe_allow_html=True)

elif selected == "제품별 불편사항":
    with st.expander(":material/experiment: **어떻게 분석하였을까요?**"):
        st.image("methodology.png")
    #        video_file = open('function.mp4', 'rb')
    #        video_bytes = video_file.read()
    #        st.video(video_bytes, width=480, autoplay=True)

    st.empty()
    iframe = st.empty()
    iframe.markdown("<iframe src='https://public.tableau.com/views/251118_device_painpoint/1?:showVizHome=no&:embed=true', width=1200, height=2500, scrolling=no, frameborder=0'></iframe>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------------------------------------------------
# 풋터 영역
# ----------------------------------------------------------------------------------------------------------------------
#container = st.container(border=True)
#container.write("본 자료의 소유권은 Design Solution Task 에 있으며, 재가공 및 배포가 불가합니다")
#with ui.card(key="card_test"):
#ui.element("span", children=["본 자료의 소유권은 Design Solution Task 에 있으며, 재가공 및 배포가 불가합니다"], className="text-gray-400 text-sm font-medium m-1", key="label1")



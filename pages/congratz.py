import streamlit as st
from uility import set_page, cheering_sound
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page

set_page()

def congratz_page():
    language = st.session_state['language']
    st.image("https://animatedimagepic.com/image/congratulations/congratulations-4308.gif")
    if st.session_state['scores'] == 2:
        if language == 'english':
            st.header("You have full scores!! ")
            st.header("Well Done!!")
        elif language == 'chinese':
            st.header("恭喜您拿到满分！！")
    elif st.session_state['scores'] == 1:
        if language == 'english':
            st.header(f"You have scored {st.session_state['scores']}")
            st.header("Keep up the good work!!")
        elif language == 'chinese':
            st.header(f"恭喜！您的总分是{st.session_state['scores']}分")
    elif st.session_state['scores'] == 0:
        if language == 'english':
            st.header("You have not scored any points")
            st.header("Don't Worry! Keep Trying!!")
            st.header("You can approach any of our Digital Ambassador to learn more")
        elif language == 'chinese':
            st.header("抱歉！您没有得分")
            st.header("没关系!继续努力!")
            st.header("您可以联系我们的数字大使以了解更多信息")
    st.balloons()
    cheering_sound()
    if language == 'english':
        st.subheader("Book an appointment with us to learn more digital skills")
        st.success("Geylang East Public Library - Hotline: 89401782 - 1pm to 6pm")
        st.success("Macpherson Community Centre - Hotline: 89401662 - 10am to 6pm")
        st.success("Kembangan Community Centre - Hotline: 91392414")
    elif language == 'chinese':
        st.subheader("欢迎与我们预约以了解更多数字技能")
        st.success("亚龙图书馆(Geylang East Library) - 热线: 89401782 - 下午1点到6点 ")
        st.success("麦波申社区中心(Macpherson CC) - 热线: 89401662 - 早上10点到下午6点")
        st.success("景万岸社区中心(Kembangan CC) - 热线: 91392414")
    submit_qns = st.button("RESET")
    if submit_qns:
        del st.session_state['scores']
        del st.session_state['correctness']
        del st.session_state['df']
        del st.session_state['scam_question_list']
        del st.session_state['general_question_list']
        del st.session_state['scam_operation']
        del st.session_state['general_operation']
        switch_page("home")


congratz_page()


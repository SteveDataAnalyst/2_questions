import streamlit as st
from uility import set_page
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page

set_page()
placeholder = st.empty()
with placeholder.container():
    if "select_language_page" not in st.session_state:
        st.session_state["select_language_page"] = False
    st.image("https://www.imda.gov.sg/-/media/Imda/Images/Content/For-Community/Digital-for-Life/DfL-logo.jpg")
    colored_header(
        label="Select the language/请选择您要的语言",
        description="",
        color_name="violet-70")

    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

    with col1:
        english = st.button("English")
    with col2:
        chinese = st.button("中文")

    if english:
        if 'language' not in st.session_state:
            st.session_state['language'] = 'english'
            placeholder.empty()
            del st.session_state["select_language_page"]
            switch_page("home")
    elif chinese:
        if 'language' not in st.session_state:
            st.session_state['language'] = 'chinese'
            placeholder.empty()
            del st.session_state["select_language_page"]
            switch_page("home")





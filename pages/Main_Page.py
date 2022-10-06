import streamlit as st


def set_page():
    st.set_page_config(initial_sidebar_state="collapsed",
                       layout="wide",
                       page_title="Marine Parade Team Quiz",
                       page_icon="🏆🏆🏆")

    st.markdown(""" <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: visible;}
    footer:after {content:'Copyright @2022: Steven Production';
                  display:block;
                  position:relative;
                  color:tomato;
                  padding:5px;
                  top:3px;

    }
    </style> """, unsafe_allow_html=True)

set_page()

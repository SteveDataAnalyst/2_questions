from data import english_scam_question_data
from chinese_data import chinese_scam_question_data
from uility import set_page
from question_model import Question
import streamlit as st
from datetime import datetime
from random import randint
from streamlit_extras.switch_page_button import switch_page

now = datetime.now()
date_now = now.strftime("%d/%m/%Y")


def main_page():
    placeholder1 = st.empty()
    with placeholder1.container():
        language = st.session_state['language']
        if language == 'english':
            st.title("Quiz for Prize (Marine Parade)")
            st.image(
                "https://raw.githubusercontent.com/SteveDataAnalyst/SDO/898829ba435d8b66ece06b1e4d2c815436d239bc/Banner1.JPG")
            string_1 = '<p style="font-family:sans-serif; font-size: 35px;">We have 2 questions to test ' \
                       'your awareness on cybersecurity and cyber hygiene practices.</p> '
            string_2 = '<p style="font-family:sans-serif; font-size: 35px;">Try our quiz to find out if you ' \
                       'are cyber safe ready!</p> '
            st.markdown(string_1, unsafe_allow_html=True)
            st.markdown(string_2, unsafe_allow_html=True)
            st.write("")
            st.write("")
            st.image(
                "https://www.csa.gov.sg/images/default-source/our-programmes/unseen-enemy/unseen-enemy-baner-2023.jpg")
            submitted = st.button("Let's go!")
        elif language == 'chinese':
            st.title("有奖问答题 (马林百列)")
            st.image(
                "https://raw.githubusercontent.com/SteveDataAnalyst/SDO/898829ba435d8b66ece06b1e4d2c815436d239bc/Banner1.JPG")
            string_1 = '<p style="font-family:sans-serif; font-size: 35px;">我们将有2个问题要测试您对网络安全认识</p> '
            string_2 = '<p style="font-family:sans-serif; font-size: 35px;">试试看看你是否对网络安全准备充实！</p> '
            st.markdown(string_1, unsafe_allow_html=True)
            st.markdown(string_2, unsafe_allow_html=True)
            st.write("")
            st.write("")
            st.image(
                "https://www.csa.gov.sg/-/media/Csa/Images/Programmes/SG-Cyber-Safe-Seniors/How-Cyber-Safe-Are"
                "-You-Quiz-Banner_600px.jpg")
            submitted = st.button("开始！！")

    if submitted:
        if 'scores' and 'correctness' and 'df' not in st.session_state:
            st.session_state['scores'] = 0
            st.session_state['correctness'] = False
            st.session_state['df'] = []
        placeholder1.empty()
        switch_page("question 1")


def random_generated_numbers(max_numbers, number_of_questions):
    not_end_of_list = True
    numbers = [randint(0, max_numbers - 1)]
    while not_end_of_list:
        can = True
        number = randint(0, max_numbers - 1)
        for i in numbers:
            if i == number:
                can = False
        if can:
            numbers.append(number)
        if len(numbers) == number_of_questions:
            not_end_of_list = False
    return numbers


def scam_question_initialize(language):
    question_bank = []
    if language == 'english':
        questions = english_scam_question_data
    elif language == 'chinese':
        questions = chinese_scam_question_data
    for question in questions:
        question_image = question["image"]
        question_text = question["text"]
        questioning = question["question"]
        question_selection = question["selection"]
        question_answer = question["answer"]
        new_question = Question(question_image, question_text, questioning, question_selection, question_answer)
        question_bank.append(new_question)
    return question_bank


class Operations:

    def __init__(self, q_list):
        self.question_list = q_list

    def return_values(self, question_no):
        image = self.question_list[question_no].image
        text = self.question_list[question_no].text
        ask = self.question_list[question_no].question
        select = self.question_list[question_no].selection
        answer = self.question_list[question_no].answer
        return image, text, ask, select, answer


if __name__ == "__main__":
    set_page()
    placeholder = st.empty()
    with placeholder.container():
        scam_question_list = random_generated_numbers(len(english_scam_question_data), 7)
        if 'scam_question_list' not in st.session_state:
            st.session_state['scam_question_list'] = scam_question_list
        language = st.session_state['language']
        scam_operation = Operations(scam_question_initialize(language))
        if 'scam_operation' not in st.session_state:
            st.session_state['scam_operation'] = scam_operation

    main_page()

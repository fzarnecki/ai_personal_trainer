# basic streamlit app, 'outsource' code to other files as much as possible
# run app, take input from user, display results of processing
# logging?
import streamlit as st
from typing import Dict, Any
from utils.streamlit_setup import load_graphics, prep_sidebar, prep_title
from utils.utils import (
    form_prompt_workout_plan_simple, 
    send_openai_chat_completion_request, 
    parse_openai_chat_completion_res_simple, 
    load_openai_api_key,
)


def prep_questionnaire_get_input() -> Dict[str, Any]:
    """ Display fields and gather data from the user in the main app screen. """
    st.markdown("Fill out the questionnaire below and get your workout plan!")
    gathered_data = dict()
    gathered_data["height"] = st.slider("Your height:", 0, 250, 170)
    gathered_data["weight"] = st.slider("Your weight:", 0, 250, 70)
    gathered_data["age"] = st.slider("Your age:", 0, 120, 30)
    disciplines = [
        "Calisthenics",
        "Parkour",
        "Tricking",
        "Street Workout",
        "Bodybuilding",
        "Weightlifting",
        "Running",
    ]
    gathered_data["discipline"] = st.selectbox("Pick your discipline:", disciplines)
    goals = [
        "Learn new skills",
        "Build strength",
        "Build muscle",
        "Build endurance",
        "Lose weight",
        "Gain weight",
        "Build discipline",
    ]
    gathered_data["goals"] = st.multiselect("What's your goal? (max 3)", goals, max_selections=3)
    gathered_data["additional_info"] = st.text_area("Anything you want to add? (100 chars)", "I like cats:)", height=50, max_chars=100)
    return gathered_data


def manage_request_send(gathered_data: Dict[str, Any]):
    """ Provides possibility to send filled form and obtain ai generated response. """
    submit = st.button("Submit!")
    if submit:
        prompt = form_prompt_workout_plan_simple(gathered_data)
        res = send_openai_chat_completion_request(
            prompt=prompt,
            system_prompt="You are a personal trainer. You provide a detailed workout plan according to provided details."
        )
        res = parse_openai_chat_completion_res_simple(res)
        return res
    

def main():
    load_graphics()
    prep_sidebar()
    prep_title()
    load_openai_api_key()

    gathered_data: Dict[str, Any] = prep_questionnaire_get_input()
    workout_plan: str = manage_request_send(gathered_data=gathered_data)
    
    if workout_plan:
        st.markdown(workout_plan)

if __name__=="__main__":
    main()
    exit(0)
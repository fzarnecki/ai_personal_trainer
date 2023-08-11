import streamlit as st
from PIL import Image


def load_graphics(
        logo_path: str = "data/images/logo.png", 
        banner_path: str = "data/images/banner.png", 
        verbose: bool = False
    ):
    """ Load and put necessary images in proper places. """
    
    if logo_path:
        try:
            logo = Image.open(logo_path)
            st.sidebar.image(logo, width=150)
        except Exception as e:
            if verbose:
                print(f"Failed to load logo image, with error: {e}")
    if banner_path:
        try:
            banner = Image.open(banner_path)
            _, col, _ = st.columns([1,1,1]) # centering the image
            with col:
                st.image(banner)
        except Exception as e:
            if verbose:
                print(f"Failed to load banner image, with error: {e}")
    
    return


def prep_sidebar():
    """ Customise the left side of the app. """
    with st.sidebar.expander("Your AI Personal Trainer", expanded=False):
        st.write("Exploit the power of AI and get in the best shape of your life today! Fill out questionnaire and get a personalised workout plan on a matter of minutes, everything tailored to your needs.")
    return
    

def prep_title():
    """ Customise the top center, main screen, of the app. """
    st.markdown(""" <style> .font { font-size:30px; color: #ffcc00; } </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">AiPT - AI Personal Trainer</p>', unsafe_allow_html=True)
    return


def adjust_slider_colors(sl: st.slider = None):
    """ Modifying the default colors to custom ones. """
    if not sl:
        return
    
    ColorMinMax = st.markdown(''' <style> div.stSlider > div[data-baseweb = "slider"] > div[data-testid="stTickBar"] > div {
    background: rgb(1 1 1 / 0%); } </style>''', unsafe_allow_html = True)

    Slider_Cursor = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{
        background-color: rgb(14, 38, 74); box-shadow: rgb(14 38 74 / 20%) 0px 0px 0px 0.2rem;} </style>''', unsafe_allow_html = True)

    Slider_Number = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div > div
                                    { color: #ffffff; } </style>''', unsafe_allow_html = True)
    
    col = f''' <style> div.stSlider > div[data-baseweb = "slider"] > div > div {{
    background: linear-gradient(to right, #ffcc00 0%, 
                                #ffcc00 {sl}%, 
                                rgba(0,0,0,0.25) {sl}%, 
                                rgba(0,0,0,0.25) 100%); }} </style>'''

    _ = st.markdown(col, unsafe_allow_html = True)
    return

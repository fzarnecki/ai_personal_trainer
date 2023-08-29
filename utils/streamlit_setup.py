import streamlit as st
from PIL import Image


def load_graphics(
        logo_path: str = "/data/images/logo.png", 
        banner_path: str = "/data/images/banner.png", 
        verbose: bool = True
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

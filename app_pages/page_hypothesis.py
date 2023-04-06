import streamlit as st

def project_hypothesis_page():
    """ 
    Contents of hypothesis page.
    """
    st.title("Hypothesis and Validation")

    st.markdown("1. We believe that mildew containing cherry leaves"
                " can be detected by the white specks covering"
                " the leaf's surface.")
    
    st.success("Using average image and image variability plots"
               " we were able to confirm this. White specks on"
               " on the surface of the leaf is the distinguishing"
               " feature between healthy and powdery mildew containing"
               " cherry leaves.")

    st.markdown("2. We believe a model can be trained"
                " to determine whether a given cherry leaf is"
                " healthy or contains powdery mildew with a"
                " degree of 97% accuracy.")
    
    st.success("A model has been successfully trained using CNN"
               " to class a given image (of a cherry leaf) as being"
               " healthy or containing mildew with a degree of accuracy"
               " above 99%.")


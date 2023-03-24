import streamlit as st 
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

def cherry_leaves_visualisation_page():
    """
    Visualisation page content.
    Average Image and Image Variability 
    plots imported from outputs.
    """
    st.title("Visualisation")

    st.markdown("This section will answer business requirement 1:"
                " The client is interested in visualising the differences"
                " between healthy cherry leaves and those containing powdery mildew.")


    st.header("Average Image and Image Variability")

    file_path = "outputs/v1"

    if st.button("Healthy"):
        mean_std_healthy = plt.imread(f"{file_path}/mean_std_healthy.png")
        st.image(mean_std_healthy, caption="Mean and variability of healthy leaves")

        st.success("The average image displays the general patterns of images beloning"
                   " to that label. For the healthy leaf this pattern is a typical"
                   " green leafy shape. For variability, the lighter shades indicate"
                   " the most variability. For the healthy leaves, the center of the"
                   " image (the darkest part) has the most similarity across the set."
                   " The outer regions, the leaf shape and orientation most likely, have"
                   " the highest variability.")

    if st.button("Powdery Mildew"):
        mean_std_mildew = plt.imread(f"{file_path}/mean_std_powdery_mildew.png")
        st.image(mean_std_mildew, caption="Mean and variability of powdery mildew leaves")

        st.success("The average image displays the general patterns of images beloning"
                   " to that label. For the powdery mildew containing leaf this pattern"
                   " is notable white specks on the surface of the leaf. For variability,"
                   " the lighter shades indicate the most variability. For the leaves"
                   " containing powdery mildew, the light patches indicate there is some"
                   " variability in where the white specks on the leaf are located.")
     
    if st.button("Differences Between Labels"):
        differences = plt.imread(f"{file_path}/differences_healthy_powdery_mildew.png")
        st.image(differences, caption="Differences in average image and variability between the labels")

        st.info("While it is not entirely reliable to decipher the differences between the"
                " labels from sight alone, there are notable differences in the center of the images."
                " The powdery mildew image shows there are white specks on the leaves. In the variability"
                " plot, the light patches show that the variability between the images is highest where"
                " the specks of mildew would be.")
     
    

    
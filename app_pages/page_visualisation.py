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

    file_path = "outputs/v1"

    mean_std_healthy = plt.imread(f"{file_path}/mean_std_healthy.png")
    mean_std_mildew = plt.imread(f"{file_path}/mean_std_powdery_mildew.png")

    
    
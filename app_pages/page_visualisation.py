import streamlit as st 
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import random
import itertools

def cherry_leaves_visualisation_page():
    """
    Visualisation page content.
    Average Image and Image Variability 
    plots imported from outputs.
    """
    st.title("Visualisation")

    st.markdown("This section will fulfill Business Requirement 1:"
                " The client is interested in visualising the differences"
                " between healthy cherry leaves and those containing powdery mildew.")
    
    st.markdown("Click on the buttons to view the plots.")

    file_path = "outputs/v1"
    
    st.header("Image Dimensions")
 
    if st.button("Dimensions Scatterplot"):
        dimensions = plt.imread(f"{file_path}/height_width_plot.jpg")
        st.image(dimensions, caption="Height vs Width (px)")

    st.info("Every image in the data set has a height and width of 256 px.")

    st.header("Average Image and Image Variability")

    if st.button("Healthy"):
        mean_std_healthy = plt.imread(f"{file_path}/mean_std_healthy.jpg")
        st.image(mean_std_healthy, caption="Mean and variability of healthy leaves")

        st.success("The average image displays the general patterns of images beloning"
                   " to that label. For the healthy leaf this pattern is a typical"
                   " green leafy shape. For variability, the lighter shades indicate"
                   " the most variability. For the healthy leaves, the center of the"
                   " image (the darkest part) has the most similarity across the set."
                   " The outer regions, the leaf shape and orientation most likely, have"
                   " the highest variability.")

    if st.button("Powdery Mildew"):
        mean_std_mildew = plt.imread(f"{file_path}/mean_std_powdery_mildew.jpg")
        st.image(mean_std_mildew, caption="Mean and variability of powdery mildew leaves")

        st.success("The average image displays the general patterns of images beloning"
                   " to that label. For the powdery mildew containing leaf this pattern"
                   " is notable white specks on the surface of the leaf. For variability,"
                   " the lighter shades indicate the most variability. For the leaves"
                   " containing powdery mildew, the light patches indicate there is some"
                   " variability in where the white specks on the leaf are located.")
     
    if st.button("Differences Between Labels"):
        differences = plt.imread(f"{file_path}/differences_healthy_powdery_mildew.jpg")
        st.image(differences, caption="Differences in average image and variability between the labels")

        st.info("While it is not entirely reliable to decipher the differences between the"
                " labels from sight alone, there are notable differences in the center of the images."
                " The powdery mildew image shows there are white specks on the leaves. In the variability"
                " plot, the light patches show that the variability between the images is highest where"
                " the specks of mildew would be.")

    st.header("Image Montage")
    
    st.markdown("Click on the 'Image Montage' button to view/refresh the image montage.")

    data_dir = "inputs/cherry_leaves_dataset/cherry_leaves"
    labels_folder = os.listdir(data_dir + "/validation")
    label = st.selectbox(label="Choose label", options=labels_folder, index=0)

    if st.button("Image Montage"):
        image_montage_data(dir_path=data_dir + "/validation",
                           label=label, 
                           nrows=10, ncols=3)


def image_montage_data(dir_path, label, nrows, ncols, figsize=(15, 30)):
    """
    Function to check if label is in the folder, check if grid space is greater
    than the image list length and display the images. 
    """
    sns.set_style("white")
    labels = os.listdir(dir_path)
    if label in labels:
        image_list = os.listdir(dir_path + "/" + label)
        if nrows * ncols < len(image_list):
            image_index = random.sample(image_list, nrows * ncols)
        else: 
            print(f"The montage space {nrows * ncols} is greater than the subset.")
            print(f"Reduce the nrows and ncols.")
            return
        
        list_of_rows = range(0, nrows)
        list_of_cols = range(0, ncols)
        ax_indices = list(itertools.product(list_of_rows, list_of_cols))

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for i in range(0, nrows * ncols):
            file = imread(dir_path + "/" + label + "/" + image_index[i])
            img_shape = file.shape
            axes[ax_indices[i][0], ax_indices[i][1]].set_title(f"Height: {img_shape[0]}px Width: {img_shape[1]}px")
            axes[ax_indices[i][0], ax_indices[i][1]].imshow(file)
            # Set the tick locations of x axis
            axes[ax_indices[i][0], ax_indices[i][1]].set_xticks([])
            # Set the tick locations of y axis
            axes[ax_indices[i][0], ax_indices[i][1]].set_yticks([])
        plt.tight_layout()
        st.pyplot(fig=fig)
    else:
        print(f"Choose from the labels: {labels}")
     
    

    
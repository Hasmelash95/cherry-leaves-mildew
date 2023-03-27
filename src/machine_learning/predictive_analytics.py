import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file

class_indices = load_pkl_file(file_path=f"outputs/v2/train_set_class_indices.pkl")


def prediction_probablities_plot(probability, pred_class):
    """ 
    Plot prediction results in a graph.
    """
    
    prob_per_class = pd.DataFrame(
                                 data=[0, 0],
                                 index=class_indices.keys(),
                                 columns=["Probability"]
                                 )
    prob_per_class.loc[pred_class] = probability
    for i in prob_per_class.index.to_list():
        if i not in pred_class:
            prob_per_class.loc[i] = 1 - probability 
    prob_per_class = prob_per_class.round(3)
    prob_per_class["Label"] = prob_per_class.index

    fig = px.bar(
                prob_per_class,
                x="Label",
                y=prob_per_class["Probability"],
                range_y=[0, 1],
                width=600, height=300, template='seaborn'
                )
    st.plotly_chart(fig)


def resize_image(img, version):
    """ 
    Resize the input image to average image size.
    """
    
    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape_embed.pkl")
    image_resized = img.resize((image_shape[1], image_shape[0]), Image.ANTIALIAS)
    input_image = np.expand_dims(image_resized, axis=0)/255

    return input_image


def load_model_to_predict_image(input_image, version):
    """
    Load model used to predict which class the input data belongs to.
    """
    model = load_model(filepath=f"outputs/{version}/mildew_detector.h5")

    probability = model.predict(input_image)[0, 0]

    target_map = {value: key for key, value in class_indices.items()}
    pred_class = target_map[probability > 0.5]
    if pred_class == target_map[0]:
        probability = 1 - probability 
    
    st.write(f"The predictive analysis indicates the sample cherry leaf"
              " belongs to the {pred_class} label.")

    return probability, pred_class
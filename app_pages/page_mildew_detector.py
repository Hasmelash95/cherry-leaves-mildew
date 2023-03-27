import streamlit as st 
from PIL import Image
import numpy as np
import pandas as pd
from src.data_management import download_df_as_csv
from src.machine_learning.predictive_analytics import (
                                                      load_model_to_predict_image,
                                                      resize_image,
                                                      prediction_probablities_plot
                                                      )


def mildew_detector_page():
    """
    Content for mildew detector page. 
    Users can upload an image of a cherry leaf and 
    they will get a prediction (along with a plot)
    that will tell them which label the image belongs to.
    """
    st.title("Mildew Detector")

    st.write("This section will fulfill Business Requirement 2:"
                " The client is interested in predicting whether a"
                " given cherry leaf is healthy or contains powdery mildew.")
    
    st.info("You can download a cherry leaf dataset containing images of"
                " both healthy and mildew-containing cherry leaves:"
                " [Dataset Link](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)")
    
    st.markdown("---")

    uploaded_image = st.file_uploader("Upload cherry leaf images. You can select multiple.",
                                      type="jpg", accept_multiple_files=True)
    
    if uploaded_image is not None:
        df_cherry_leaves = pd.DataFrame([])
        for file in uploaded_image:

            image_pil = (Image.open(file))
            st.info(f"Cherry Leaf Image: {file.name}")
            image_array = np.array(image_pil)
            st.image(image_pil, caption=f"Image Size: {image_array.shape[1]}px width x"
                                        f" {image_array.shape[0]}px height")

            resized_image = resize_image(img=image_pil, version="v1")
            probability, pred_class = load_model_to_predict_image(input_image=resized_image,
                                                                  version="v2")
            prediction_probablities_plot(probability=probability, pred_class=pred_class)
            df_cherry_leaves = df_cherry_leaves.append({"Name": {file.name},
                                                        "Result": pred_class},
                                                       ignore_index=True)

        if not df_cherry_leaves.empty:
            st.success("Analysis Report")
            st.table(df_cherry_leaves)
            st.markdown(download_df_as_csv(df_cherry_leaves), unsafe_allow_html=True)
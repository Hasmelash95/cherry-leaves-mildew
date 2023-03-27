import numpy as np
import pandas as pd
import os
import base64
from datetime import datetime
import joblib

def download_df_as_csv(df):
    """
    Function to download a dataframe as a 
    csv file.
    """
    present_date = datetime.now().strftime("%d%m%Y_%Hh%Mmin%Ss")
    csv = df.to_csv().encode()
    b64 = base64.b64encode(csv).decode()
    href = (
        f'<a href="data:file/csv;base64,{b64}" download="Report {present_date}.csv" '
        f'target="_blank">Download Report</a>'
    )

    return href

def load_pkl_file(file_path):
    return joblib.load(filename=file_path)
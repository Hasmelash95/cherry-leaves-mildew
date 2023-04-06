import streamlit as st
from src.data_management import load_pkl_file


def load_evaluate_pkl(version):
    """ 
    Calls the load pkl file to load the evaluate pkl
    """
    return load_pkl_file(file_path=f"outputs/{version}/test_evaluation.pkl")
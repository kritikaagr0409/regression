import streamlit as st
import pickle

# Load the Pickled model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

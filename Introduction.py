# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:39:59 2022

@author: bzmow
"""

import streamlit as st
import pandas as pd

# Setting the page layout
st.set_page_config(layout="wide")

# Defining custom CSS styles
st.markdown("""
    <style>
    .font1 {
        font-size: 45px;
        font-family: 'Copper Black';
        color: #FF9633;
    }
    .font2 {
        font-size: 30px;
        font-family: 'Copper Black';
        color: #FF9633;
    }
    .p { 
        color: #FF0000;
    }
    </style>
""", unsafe_allow_html=True)
    
###############################################################################
################################# FUNCTIONS ###################################
###############################################################################

@st.cache_data
def

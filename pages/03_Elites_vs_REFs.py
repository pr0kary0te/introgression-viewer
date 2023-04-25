# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:39:59 2022

@author: bzmow
"""
import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")

st.markdown(""" <style> .font1 {
    font-size: 45px; font-family: 'Copper Black'; color: #FF9633}
    </style> """, unsafe_allow_html=True)

st.markdown(""" <style> .font2 {
    font-size: 30px; font-family: 'Copper Black'; color: #FF9633}
    </style> """, unsafe_allow_html=True)
    
st.markdown(""" <style> .font2b {
    font-size: 30px; font-family: 'Copper Black'; color: #1F77B4}
    </style> """, unsafe_allow_html=True)    

st.markdown(""" <style> .font2o {
    font-size: 30px; font-family: 'Copper Black'; color: #FF7F0E}
    </style> """, unsafe_allow_html=True)
    
st.markdown(""" <style> .red { color: #FF0000} </style> """, unsafe_allow_html=True)


st.write('Hello, this page works')

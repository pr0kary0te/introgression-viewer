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


################################# FUNCTIONS ###################################


@st.cache_data(show_spinner='Fetching large data file ...')
def getData(filePath):
    df = pd.read_csv(filePath)
     
    return df


def change_index(df):
    bin_list = list(range(1,(len(df) + 1)))
    dfNew = df.assign(AdjustedBin=bin_list)
    
    return dfNew
    

###############################################################################

with st.sidebar:
    
    refGenome = st.selectbox(
        label='Select Reference Genome:',
        options=('Arina', 'Chinese Spring', 'Jagger',
                 'Julius', 'Lancer', 'Landmark', 'Mace',
                 'Norin61', 'Spelt', 'Stanley', 'Mattis'),
        index=0,
        key='ref')
    

    refFiles = {'Arina': ['https://www.cerealsdb.uk.net/ibspy_data/arina1_4.csv', '_WhAri'],
              'Chinese Spring': ['https://www.cerealsdb.uk.net/ibspy_data/chinese_springSortedElites.csv', ''],
              'Jagger': ['https://www.cerealsdb.uk.net/ibspy_data/jaggerSortedElites.csv', '_WhJag'],
              'Julius': ['https://www.cerealsdb.uk.net/ibspy_data/juliusSortedElites.csv', '_Whjul'],
              'Lancer': ['https://www.cerealsdb.uk.net/ibspy_data/lancerSortedElites.csv', '_Whlan'], 
              'Landmark': ['https://www.cerealsdb.uk.net/ibspy_data/landmarkSortedElites.csv', '_WhLan'],
              'Mace': ['https://www.cerealsdb.uk.net/ibspy_data/maceSortedElites.csv', '_Whmac'],
              'Norin61': ['https://www.cerealsdb.uk.net/ibspy_data/norin61SortedElites.csv', '_WhNor'],
              'Spelt': ['https://www.cerealsdb.uk.net/ibspy_data/speltaSortedElites.csv', '_Whspe'],
              'Stanley': ['https://www.cerealsdb.uk.net/ibspy_data/stanleySortedElites.csv', '_WhSta'],
              'Mattis': ['https://www.cerealsdb.uk.net/ibspy_data/sy_mattisSortedElites.csv', '_WhSYM']
              }

        
    filePath = refFiles[refGenome][0]    

    dfWhole = getData(filePath)
        
    dfWhole.rename(columns={'timopheevii10558_nuq.jf': 'timopheevii10558_nuq_jf',
                       'timopheevii14352_nuq.jf': 'timopheevii14352_nuq_jf',
                       'timopheevii15832_nuq.jf': 'timopheevii15832_nuq_jf',
                       'timopheevii22438_nuq.jf': 'timopheevii22438_nuq_jf',
                       'timopheevii3708_nuq.jf': 'timopheevii3708_nuq_jf'},
                         inplace=True)

    chrm = st.selectbox(
        label='Select chromosome:',
        options=('1A', '2A', '3A', '4A', '5A', '6A', '7A',
                 '1B', '2B', '3B', '4B', '5B', '6B', '7B',
                '1D', '2D', '3D', '4D', '5D', '6D', '7D'),
        index=0,
        key='chrm')


   
st.markdown('<h1 class="font1">Introgression in Elites varieties</h1>', unsafe_allow_html=True)    
st.markdown("""
 
            ---
                
            """)
            

# From the large dataframe (dfWhole), which contains the data for all 21 chromosomes,
# create a smaller dataframe (dfChromosome) containing just the data for the selected
# chromosome.
dfChromosome = dfWhole[dfWhole['seqname'] == 'chr' + chrm + refFiles[refGenome][1]]

# Adjust the bin number so that it begins at zero (1) for each chromosome.  This
# is carried out by a function which is defined at the top of this script.
dfChromosome = change_index(dfChromosome)

col1, col2 = st.columns([1,4], gap='large')

with col1:
    
    st.write('')
    
with col2:

    slider_range = st.slider(
        'Using the slider below, select the range (bin numbers) over which to search:',
        value=[0, len(dfChromosome)])    
    
 

# From the large dataframe (dfChromosome), which contains all the data for the
# selected chromosome, create a smaller dataframe (dfChrm_slide) containing just
# the data for the selected region of the chromosome.
dfChrm_slide = dfChromosome.iloc[slider_range[0]:slider_range[1]]
selected_range = len(dfChrm_slide)


# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:39:59 2022

@author: bzmow
"""
import streamlit as st
import pandas as pd
import seaborn as sns


st.set_page_config(layout="wide")

st.markdown(""" <style> .font1 {
    font-size: 45px; font-family: 'Copper Black'; color: #FF9633}
    </style> """, unsafe_allow_html=True)

st.markdown(""" <style> .font2 {
    font-size: 30px; font-family: 'Copper Black'; color: #FF9633}
    </style> """, unsafe_allow_html=True)


################################# FUNCTIONS ###################################


@st.cache_data
def getData(filePath):
    df = pd.read_csv(filePath)
     
    return df


def dropREF(refGenome, dfChr):
    
    if refGenome == 'Arina':
        dfChrNew = dfChr.drop(['arina-pg'], axis = 1)
    if refGenome == 'Chinese Spring':
        dfChrNew = dfChr.drop(['chinese-pg'], axis = 1)    
    if refGenome == 'Jagger':
        dfChrNew = dfChr.drop(['jagger-pg'], axis = 1)    
    if refGenome == 'Julius':
        dfChrNew = dfChr.drop(['julius-pg'], axis = 1)    
    if refGenome == 'Lancer':
        dfChrNew = dfChr.drop(['lancer-pg'], axis = 1)    
    if refGenome == 'Landmark':
        dfChrNew = dfChr.drop(['landmark-pg'], axis = 1)
    if refGenome == 'Mace':
        dfChrNew = dfChr.drop(['mace-pg'], axis = 1)
    if refGenome == 'Mattis':
        dfChrNew = dfChr.drop(['mattis-pg'], axis = 1)    
    if refGenome == 'Norin61':
        dfChrNew = dfChr.drop(['norin61-pg'], axis = 1)    
    if refGenome == 'Spelt':
        dfChrNew = dfChr.drop(['spelt-pg'], axis = 1)    
    elif refGenome == 'Stanley':
        dfChrNew = dfChr.drop(['stanley-pg'], axis = 1)
        
    return dfChrNew


def changeColNames(df):
    
    dfChrNew = df.rename(columns={'ENT336': 'Ae. tauschii (ENT336)',
                'BW_01011': 'Ae. tauschii (BW_01011)',
                'BW_01022': 'Ae. tauschii (BW_01022)',
                'BW_01014': 'Ae. tauschii (BW_01014)',
                'BW_01024': 'Ae. tauschii (BW_01024)',
                'BW_01026': 'Ae. tauschii (BW_01026)',
                'BW_01028': 'Ae. tauschii (BW_01028)',
                'dicoccoides-10x_nuq': 'T. dicoccoides',
                'elongathum-10x_nuq': 'Th. elongatum',
                'Lo7_nuq': 'Secale cereale',
                'ponticumG37_nuq': 'Th. ponticum (37)',
                'ponticumG38_nuq': 'Th. ponticum (38)',
                'ponticumG39-10x_nuq': 'Th. ponticum (39)',
                'speltoides-10x_nuq': 'Ae. speltoides',
                'svevo-10x_nuq': 'T. durum (Svevo)',
                'timopheevi10827-10x_nuq': 'T. timopheevii (10827)',
                'timopheevi33255-10x_nuq': 'T. timopheevii (33255)',
                'timopheevii10558_nuq.jf': 'T. timopheevii (10558)',
                'timopheevii10827-10x-all_all': 'T. timopheevii (10827_all)',
                'timopheevii14352_nuq.jf': 'T. timopheevii (14352)',
                'timopheevii15832_nuq.jf': 'T. timopheevii (15832)',
                'timopheevii17024-10x_all': 'T. timopheevii (17024)',
                'timopheevii22438_nuq.jf': 'T. timopheevii (22438)',
                'timopheevii3708_nuq.jf': 'T. timopheevii (3708)',
                'urartu-10x_nuq': 'T. urartu',
                'ventricosa-10x_nuq': 'Ae. ventricosa',
                'ventricosa2067-10x_nuq': 'Ae. ventricosa (2067)',
                'ventricosa2181': 'Ae. ventricosa (2181)',
                'ventricosa2181-10x_nuq': 'Ae. ventricosa (2181 10x)',
                'ventricosa2210-10x_all': 'Ae. ventricosa (2210)',
                'ventricosa2211-10x_nuq': 'Ae. ventricosa (2211)',
                'ventricosa2234-10x_all': 'Ae. ventricosa (2234)',
                'arina-pg': 'Arina',
                'chinese-pg': 'Chinese Spring',
                'jagger-pg': 'Jagger',
                'julius-pg': 'Julius',
                'lancer-pg': 'Lancer',
                'landmark-pg': 'Landmark',
                'mace-pg': 'Mace',
                'mattis-pg': 'Mattis',
                'norin61-pg': 'Norin 61',
                'spelt-pg': 'Spelt',
                'stanley-pg': 'Stanley'
                })
    
    return(dfChrNew)
    

###############################################################################

dfWildSpeciesList = pd.read_csv('./data/wild_relatives_introduction.csv')

st.markdown('<h1 class="font1">Clustering of Wild Relatives</h1>', unsafe_allow_html=True)
st.markdown("""
            
            ---
            
            """)

col1, col2 = st.columns([3,1], gap='large')

with col1:

    st.markdown("""
                        
            The heatmap and associated dendrogram show the similarity of the
            various wild species to the selected reference genome.
            
            Please note:
                
            Some of the alien species are represented by several samples.  Please
            be aware that these are not necessarily identical to each other.  Indeed,
            some samples bearing the same species name are quite distinct one from
            another (e.g., *T. timopheevii* 10827-10x-all_all and *T. timopheevii* 33255-10x_nuq).
            These differences, which will be apparent in the heatmaps, may genuinely
            represent the variation to be found in those species, or might reflect
            errors in naming.
                
            1. Plots and tables can be expanded by clicking on the arrows to their top right.  Hover over the relevant plot or table to see the arrows.
            2. Plots can be downloaded as png or svg format files by clicking on the ellipsis (...) that appears to their top right once you hover over it.
            3. All plots are are orientated such that chromosome short arms are on the left.
                
            
            REFS    
                
            - '*Multiple wheat genomes reveal global variation in modern breeding*, **Nature** 588: 277 - 283'
            - '*Detecting major introgressions in wheat and their putative origins using coverage analysis*', **Scientific Reports** 12, 1908
            """)

dfTaxonomy = pd.read_csv('./data/wild_relatives.csv')

with col2:    
    refGenome = st.selectbox(
        'Select the reference genome',
        ['Arina', 'Chinese Spring', 'Jagger', 'Julius', 'Lancer', 'Landmark', 
         'Mace', 'Mattis', 'Norin61', 'Spelt', 'Stanley'],
        0
        )

    refFiles = {'Arina': ['https://www.cerealsdb.uk.net/ibspy_data/aliensArina.csv', '_WhAri'],
              'Chinese Spring': ['https://www.cerealsdb.uk.net/ibspy_data/aliensChineseSpring.csv', ''],
              'Jagger': ['https://www.cerealsdb.uk.net/ibspy_data/aliensJagger.csv', '_WhJag'],
              'Julius': ['https://www.cerealsdb.uk.net/ibspy_data/aliensJulius.csv', '_Whjul'],
              'Lancer': ['https://www.cerealsdb.uk.net/ibspy_data/aliensLancer.csv', '_Whlan'], 
              'Landmark': ['https://www.cerealsdb.uk.net/ibspy_data/aliensLandmark.csv', '_WhLan'],
              'Mace': ['https://www.cerealsdb.uk.net/ibspy_data/aliensMace.csv', '_Whmac'],
              'Norin61': ['https://www.cerealsdb.uk.net/ibspy_data/aliensNorin61.csv', '_WhNor'],
              'Spelt': ['https://www.cerealsdb.uk.net/ibspy_data/aliensSpelt.csv', '_Whspe'],
              'Stanley': ['https://www.cerealsdb.uk.net/ibspy_data/aliensStanley.csv', '_WhSta'],
              'Mattis': ['https://www.cerealsdb.uk.net/ibspy_data/aliensMattis.csv', '_WhSYM']
              }


    st.write('Please be patient whilst the reference genome is loaded ...')

    filePath = refFiles[refGenome][0]

    df = getData(filePath)
    
    chrm = st.selectbox(
        'Which chromosome do you wish to view?',
        ['1A', '2A', '3A', '4A', '5A', '6A', '7A',
         '1B', '2B', '3B', '4B', '5B', '6B', '7B',
         '1D', '2D', '3D', '4D', '5D', '6D', '7D'],
        0
        )


st.markdown("""
            
            ---
            
            """)


chromosome = 'chr' + chrm + refFiles[refGenome][1]
dfChr = df[df['seqname'] == chromosome]


dfChrNew = dropREF(refGenome, dfChr)
  
    
col1, col2 = st.columns([5,2], gap='small')

# In column 1 the heatmap is plotted
# Column 2 is initially empty, but there is the possibility to see a dropdown table showing
# the genome constitution of the various alien species used in the study.

with col1:

    st.markdown('<p class="font2">Heatmap and Cluster Plots of Wild Relatives</p>', unsafe_allow_html=True)    

    dfChrNew = changeColNames(dfChrNew)
    
    sns.set(font_scale=0.8)
    ax = sns.clustermap(dfChrNew.iloc[:, 4:47].corr())
    st.pyplot(ax)
    
with col2:
    
    with st.expander("Alien species and their genome designation"):
        st.write("The table below lists the alien species that are available to be checked against the reference species for potential introgressions.")
        st.table(dfWildSpeciesList)


if st.checkbox('Show Similarty Matrix'):

    st.markdown('## Similarity Matrix')
    st.write(dfChrNew.iloc[:, 4:47].corr())

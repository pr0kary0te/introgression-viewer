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
         'Mace', 'Norin61', 'Spelt', 'Stanley', 'Mattis'],
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
    
col1, col2 = st.columns([3,2], gap='small')

with col1:

    st.markdown('<p class="font2">Heatmap and Cluster Plots of Wild Relatives</p>', unsafe_allow_html=True)    

    variety_list = ['ENT336',
                    'BW_01011',
                    'BW_01014',
                    'BW_01022',
                    'BW_01024',
                    'BW_01026',
                    'BW_01028',
                    'dicoccoides-10x_nuq',
                    'elongathum-10x_nuq',
                    'Lo7_nuq',
                    'ponticumG37_nuq',
                    'ponticumG38_nuq',
                    'ponticumG39-10x_nuq',
                    'speltoides-10x_nuq',
                    'svevo-10x_nuq',
                    'timopheevi10827-10x_nuq',
                    'timopheevi33255-10x_nuq',
                    'timopheevii10558_nuq.jf',
                    'timopheevii10827-10x-all_all',
                    'timopheevii14352_nuq.jf',
                    'timopheevii15832_nuq.jf',
                    'timopheevii17024-10x_all',
                    'timopheevii22438_nuq.jf',
                    'timopheevii3708_nuq.jf',
                    'urartu-10x_nuq',
                    'ventricosa-10x_nuq',
                    'ventricosa2067-10x_nuq',
                    'ventricosa2181',
                    'ventricosa2181-10x_nuq',
                    'ventricosa2210-10x_all',
                    'ventricosa2211-10x_nuq',
                    'ventricosa2234-10x_all']
    
    dfChr = dfChr.rename(columns={'ENT336': 'Ae. tauschii (ENT336)',
                                  'BW_01011': 'Ae. tauschii (BW_01011)',
                                  'BW_01022': 'Ae. tauschii (BW_01022)',
                                  'BW_01014': 'Ae. tauschii (BW_01014)',
                                  'BW_01024': 'Ae. tauschii (BW_01024)',
                                  'BW_01026': 'Ae. tauschii (BW_01026)',
                                  'BW_01028': 'Ae. tauschii (BW_01028)',
                                  'elongathum-10x_nuq': 'Th. elongatum',
                                  'Lo7_nuq': 'Secale cereale',
                                  'svevo-10x_nuq': 'T. dicoccum (Svevo)'
                                  })
    ax = sns.clustermap(dfChr.iloc[:, 4:35].corr())
    st.pyplot(ax)
    
with col2:
    
    with st.expander("Alien species and their genome designation"):
        st.write("The table below lists the alien species that are available to be checked against the reference species for potential introgressions.")
        st.table(dfWildSpeciesList)




if st.checkbox('Show Similarty Matrix'):

    st.markdown('## Similarity Matrix')
    st.write(dfChr[variety_list].corr())

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:39:59 2022

@author: bzmow
"""

import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

st.markdown(""" <style> .font1 {
    font-size: 45px; font-family: 'Copper Black'; color: #FF9633}
    </style> """, unsafe_allow_html=True)

st.markdown(""" <style> .font2 {
    font-size: 30px; font-family: 'Copper Black'; color: #FF9633}
    </style> """, unsafe_allow_html=True)

st.markdown(""" <style> .p { color: #FF0000} </style> """, unsafe_allow_html=True)
    
###############################################################################


################################# FUNCTIONS ###################################


@st.cache_data
def getData(filePath):
    df = pd.read_csv(filePath)
     
    return df

###############################################################################

st.markdown('<h1 class="font1">Introgression Viewer</h1>', unsafe_allow_html=True)    
st.markdown("""
                
            Based on data produced by IBSpy (IBSpy: https://github.com/Uauy-Lab/IBSpy)
                
            ---
                
            """
            )

# Load the table from a csv file
dfWildSpeciesList = pd.read_csv('./data/wild_relatives_introduction.csv')

col1, col2 = st.columns(2, gap='medium')

with col1:
        
    st.image('./images/gene_pools.png')
        
        
with col2:
        
    st.markdown("""
                
        This visualisation tool, which is based on data produced by the IBSpy
        program created by Dr. Cristobal Uauy and Dr. Jesus Quiroz-Chavez at
        the JIC (IBSpy: https://github.com/Uauy-Lab/IBSpy), makes it possible
        to identify putative introgressions from a range of wheat wild relatives
        (**see expandable table below**) into the genomes of 11 reference cultivars:  
                
        
            
        ### Reference Genomes    
                    
        - Arina (some uncertaintly whether ArinaLrFor)
        - Chinese Spring
        - Jagger
        - Julius
        - Lancer (syn. LongReach Lancer)
        - Landmark (CDC Landmark)
        - Mace
        - Norin 61
        - Spelt
        - Stanley
        - SY Mattis
        
        
        A brief description of the IBSpy approach is provided at the bottom
        of this page.         
                
        """
        
        
        )


    with st.expander("Alien species and their genome designation"):
        st.write("The table below lists the alien species that are available to be checked against the reference species for potential introgressions.")
        st.table(dfWildSpeciesList)


st.markdown('---')

st.markdown('<h3 class="font2">IBSpy</h3>', unsafe_allow_html=True)         
st.markdown("""
                
            Using 50,000 kbp windows (bins) spanning each chromosome, k-mers from
            the sequence of the reference genomes (ArinaLrFor, Chinese Spring,
            Jagger, Julius, LongReach Lancer, CDC Landmark, Mace, Norin 61, Stanley
            and SY_Mattis) have 
            been compared to those of each query variety and the number of
            failed matches (a set of continuous k-mers (k=31) from the reference
            completely absent in the query) counted for each window (bin). Low
            counts indicate the high similarity between the reference assembly
            and the query sequence, whereas high variation counts indicate lower
            sequence similarity.  On average, those windows with IBSpy scores of
            30 or less have sequence identity of 99.95% when their full genome
            assemblies are compared and, hence, are indicative of identity by descent. 

 
            we consider pairwise comparisons with IBSpy values of ≤ 30 variations per 50-kbp
            as being identical or near-identical by state, both in hexaploid
            wheat and between hexaploid and wild relative comparisons.  Next,
            we used the variations count ≤ 30 criteria to identify continuous
            windows that belong to an introgression block across the A genome
            of the ten wheat genome assemblies. For each 50-kbp window, we
            determined the minimum number of variations in the raw data of the
            218 accessions and the two assemblies of *T. monococcum*. Based on
            this “Einkorn_min” value, we identified 50-kbp windows in which this
            value was equal to or lower than the 30 variations cut-off. These
            windows were considered to be wild relative introgressions into the
            corresponding reference sequence. We next called introgressions
            blocks (Supplementary Table 13) by stitching together 50-kbp windows
            with variations ≤ 30 that were separated by less than ten
            non-introgression windows (i.e., with variations > 30). This was done
            as the "non-introgression" windows often had values just above the
            30 variations cut-off.  For each introgression block, we determined
            the number of T. monococcum accessions belonging to each of the
            six STRUCTURE groups (Figure 4b, Supplementary Note 2, Supplementary Table 13).
            An accession was assigned as having an introgression block if it
            had at least 20% of the 50-kbp windows within the block with variations
            values ≤ 30. For example, if an introgression block has 60 windows,
            an accession would be classified as having the introgression if 12
            or more 50-kbp windows (60×20% = 12 windows) had variation values
            of 30 or less. 
                
            ---
                
            """
                
            )

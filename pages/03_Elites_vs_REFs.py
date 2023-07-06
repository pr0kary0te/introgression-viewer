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
    

    refFiles = {'Arina': ['https://www.cerealsdb.uk.net/ibspy_data/arinaSortedElites.zip', '_WhAri'],
              'Chinese Spring': ['https://www.cerealsdb.uk.net/ibspy_data/chinese_springSortedElites.zip', ''],
              'Jagger': ['https://www.cerealsdb.uk.net/ibspy_data/jaggerSortedElites.zip', '_WhJag'],
              'Julius': ['https://www.cerealsdb.uk.net/ibspy_data/julius1_4.csv', '_Whjul'],
              'Lancer': ['https://www.cerealsdb.uk.net/ibspy_data/lancer1_4.csv', '_Whlan'], 
              'Landmark': ['https://www.cerealsdb.uk.net/ibspy_data/landmark1_4.csv', '_WhLan'],
              'Mace': ['https://www.cerealsdb.uk.net/ibspy_data/mace1_4.csv', '_Whmac'],
              'Mattis': ['https://www.cerealsdb.uk.net/ibspy_data/mattis1_4.csv', '_WhSYM'],
              'Norin61': ['https://www.cerealsdb.uk.net/ibspy_data/norin1_4.csv', '_WhNor'],
              'Spelt': ['https://www.cerealsdb.uk.net/ibspy_data/spelt1_4.csv', '_Whspe'],
              'Stanley': ['https://www.cerealsdb.uk.net/ibspy_data/stanley1_4.csv', '_WhSta']
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

st.markdown("""
            
            ---
                
            """)

names = list(dfChromosome.iloc[:, 3:305])
        
SeriesSum = dfChrm_slide.iloc[:, 4:len(dfChrm_slide)].sum()
SeriesSumSorted = SeriesSum.sort_values(ascending = True)

SeriesSumSorted = SeriesSumSorted.drop(labels = ['AdjustedBin'])

# Convert the pandas Series, SeriesSumSorted, into a dataframe, dfSumSorted
dfSumSorted = SeriesSumSorted.to_frame().reset_index()
dfSumSorted.rename(columns = {'index':'Variety', 0:'Score Sum'},
          inplace = True)


col1, col2 = st.columns([2, 5], gap = 'medium')

with col1:
    
    st.markdown('<p class="font2">Scores</p>', unsafe_allow_html=True)
    st.write('The smaller the score, the great the similarity between the reference and the named elite variety')
    
    st.write(dfSumSorted)
 
    st.markdown("""
                
                ---
                    
                """)
    
with col2:
    
    col2a, col2b = st.columns(2, gap = 'small')
        
    with col2a:
        
        choice1 = st.number_input('Select variety by number', value=2, min_value=0, key='Choice1')
        
    with col2b:

        choice2 = st.number_input('Select variety by number', label_visibility='hidden', value=5, min_value = 0, key = 'Choice2')
 
    var1 = SeriesSumSorted.index[choice1]
    var2 = SeriesSumSorted.index[choice2]

    st.markdown(f'<p><span class="font2b">{var1}</span> vs <span class="font2o">{var2}</span></p>', unsafe_allow_html=True)

    chart1_data = dfChrm_slide
    a = alt.Chart(chart1_data).mark_line(opacity=0.9, color='#1F77B4').encode(
        x='AdjustedBin',
        y=var1)

    chart1_data = dfChrm_slide
    b = alt.Chart(chart1_data).mark_line(opacity=0.5, color='#FF7F0E').encode(
        x='AdjustedBin',
        y=var2)

    c = alt.layer(a, b)

    st.altair_chart(c, use_container_width=True)
    
    col2c, col2d = st.columns(2, gap = 'small')
        
    with col2c:
    
        choice3 = st.number_input('Select variety by number', value=20, min_value=0, key='Choice3')
    
    with col2d:
        
        choice4 = st.number_input('Select variety by number', label_visibility='hidden', value=200, min_value = 0, key = 'Choice4')
    
    var3 = SeriesSumSorted.index[choice3]
    var4 = SeriesSumSorted.index[choice4]

    st.markdown(f'<p><span class="font2b">{var3}</span> vs <span class="font2o">{var4}</span></p>', unsafe_allow_html=True)

    chart1_data = dfChrm_slide
    a = alt.Chart(chart1_data).mark_line(opacity=0.9, color='#1F77B4').encode(
        x='AdjustedBin',
        y=var3)

    chart1_data = dfChrm_slide
    b = alt.Chart(chart1_data).mark_line(opacity=0.5, color='#FF7F0E').encode(
        x='AdjustedBin',
        y=var4)

    c = alt.layer(a, b)

    st.altair_chart(c, use_container_width=True)   

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:39:59 2022

@author: bzmow
"""
import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

st.markdown(""" <style> .font1 {
    font-size: 45px; font-family: 'Copper Black'; color: #FF9633},
    .font2 {
    font-size: 30px; font-family: 'Copper Black'; color: #FF9633}
    </style> """, unsafe_allow_html=True)
    
 
# Load the table from a csv file
dfWildSpeciesList = pd.read_csv('./data/wild_relatives_introduction.csv')


################################# FUNCTIONS ###################################


@st.cache_data
def getData(filePath):
    df = pd.read_csv(filePath)
     
    return df


###############################################################################

st.markdown('<h1 class="font1">Quick Check Aliens vs Reference</h1>', unsafe_allow_html=True)    

col1, col2 =st.columns([4,1], gap='large')

with col1:
    
    st.markdown("""
                
                This page allows one to quickly but crudely compare all alien species in the
                database (see dropdown table below) against the reference genomes (you choose 
                which from the dropdown list to the right) to see whether there are any
                sequences of high similarity; such regions are indicative of there being
                introgression from the former into the latter.
    
                If there are such sequences, then, on the next page, one can visualise these
                regions and look for similar regions in Elite varieties of Watkins lines.
        
                """
                )
    with st.expander("Alien species and their genome designation"):
        st.write("The table below lists the alien species that are available to be checked against the reference species for potential introgressions.")
        st.table(dfWildSpeciesList)

with col2:
    
    refGenome = st.selectbox(
        'Select reference genome',
        ['Arina', 'Chinese Spring', 'Jagger', 'Julius', 'Lancer', 'Landmark', 
         'Mace', 'Norin61', 'Spelt', 'Stanley', 'Mattis'],
        key='ref'
        )

# Define a dictionary in which the keys are the names of the reference genomes
# and the values are tuples containing [0] the path to the respective file and 
# [1] the sample prefix within the file. 
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


    st.write('')    
    score_threshold = st.number_input('Score threshold (integer from 10 - 200):', min_value=10, max_value=200, value=30, key=1)


# with col2:
    
#     percent_similarity = st.number_input('Required similarity (float from 0.01 - 0.99)', min_value=0.01, max_value=0.95, value=0.9, key=2)



    
filePath = refFiles[refGenome][0]

df = getData(filePath)
    
df.rename(columns={'timopheevii10558_nuq.jf': 'timopheevii10558_nuq_jf',
                   'timopheevii14352_nuq.jf': 'timopheevii14352_nuq_jf',
                   'timopheevii15832_nuq.jf': 'timopheevii15832_nuq_jf',
                   'timopheevii22438_nuq.jf': 'timopheevii22438_nuq_jf',
                   'timopheevii3708_nuq.jf': 'timopheevii3708_nuq_jf'},
                    inplace=True)
    

# Define a dictionary in which the keys are the alien species and the values are
# the names given to the samples in the dataframe; e.g., the alien species Aegilops tauschii
# is named ENT336 in the underlying dataframe.      
alien = {'Aegilops tauschii (D genome) - ENT336': 'ENT336',
      'Aegilops speltoides (B or S genome) - speltoides-10x_nuq': 'speltoides-10x_nuq',
      'Aegilops ventricosa (ND genomes - tetraploid) - ventricosa-10x_nuq': 'ventricosa-10x_nuq',
      'Aegilops ventricosa (ND genomes - tetraploid) - ventricosa2067-10x_nuq': 'ventricosa2067-10x_nuq',   
      'Aegilops ventricosa (ND genomes - tetraploid) - ventricosa2181': 'ventricosa2181', 
      'Aegilops ventricosa (ND genomes - tetraploid) - ventricosa2181-10x_nuq': 'ventricosa2181-10x_nuq',      
      'Aegilops ventricosa (ND genomes - tetraploid) - ventricosa2210-10x_all': 'ventricosa2210-10x_all',      
      'Aegilops ventricosa (ND genomes - tetraploid) - ventricosa2211-10x_nuq': 'ventricosa2211-10x_nuq',
      'Aegilops ventricosa (ND genomes - tetraploid) - ventricosa2234-10x_all': 'ventricosa2234-10x_all',     
      'Secale cereale (R genome) - Lo7_nuq': 'Lo7_nuq',
      'Thinopyrum elongatum (E genome - diploid) - elongathum-10x_nuq': 'elongathum-10x_nuq',
      'Thinopyrum ponticum (E genome - decaploid) - ponticumG37_nuq': 'ponticumG37_nuq',
      'Thinopyrum ponticum (E genome - decaploid) - ponticumG38_nuq': 'ponticumG38_nuq',     
      'Thinopyrum ponticum (E genome - decaploid) - ponticumG39-10x_nuq': 'ponticumG39-10x_nuq',
      'Triticum timopheevii (AG genomes - tetraploid) - timopheevi33255-10x_nuq': 'timopheevi33255-10x_nuq',
      'Triticum timopheevii (AG genomes - tetraploid) - timopheevii10558_nuq.jf': 'timopheevii10558_nuq_jf',
      'Triticum timopheevii (AG genomes - tetraploid) - timopheevi10827-10x_nuq':  'timopheevi10827-10x_nuq',    
      'Triticum timopheevii (AG genomes - tetraploid) - timopheevii10827-10x-all_all': 'timopheevii10827-10x-all_all',     
      'Triticum timopheevii (AG genomes - tetraploid) - timopheevii14352_nuq.jf': 'timopheevii14352_nuq_jf',     
      'Triticum timopheevii (AG genomes - tetraploid) - timopheevii15832_nuq.jf': 'timopheevii15832_nuq_jf',
      'Triticum timopheevii (AG genomes - tetraploid) - timopheevii17024-10x_all': 'timopheevii17024-10x_all',
      'Triticum timopheevii (AG genomes - tetraploid) - timopheevii22438_nuq.jf': 'timopheevii22438_nuq_jf',
      'Triticum timopheevii (AG genomes - tetraploid) - timopheevii3708_nuq.jf': 'timopheevii3708_nuq_jf',     
      'Triticum turgidum ssp. dicoccoides (AB genome - tetraploid) - dicoccoides-10x_nuq': 'dicoccoides-10x_nuq',
      'Triticum turgidum ssp. dicoccum (AB genome - tetraploid) - svevo-10x_nuq': 'svevo-10x_nuq',
      'Triticum urartu (A genome) - urartu-10x_nuq': 'urartu-10x_nuq'}
    
    
    
st.markdown("""
                
            ---
                
            """)
            

st.markdown(f'#### Reference genome: {refGenome}')
st.write('Number of bins form aliens with scores less than 30')


chrm = ['1A', '2A', '3A', '4A', '5A', '6A', '7A',
      '1B', '2B', '3B', '4B', '5B', '6B', '7B',
      '1D', '2D', '3D', '4D', '5D', '6D', '7D']

binsBelow = (f'BinsBelow{score_threshold}')   
dfNew = pd.DataFrame(columns = ['Variety', 'Chromosome', 'ChromosomeLength', binsBelow, 'Percent'])            

for j in chrm:
    
    chromosome = 'chr' + j + refFiles[refGenome][1]

    dfChr = df[df['seqname'] == chromosome]

    # Adjust the bin number so that it begins at zero (1) for each chromosome.
    dfChr['Adjusted Bin'] = dfChr['Bin'] - dfChr.iloc[0,0]

    my_list = []
    for i in alien:
        if len(dfChr[dfChr[alien[i]] <= score_threshold]) > (len(dfChr) * 0.01):
            my_list.append(alien[i])
            my_list.append(j)            
            my_list.append(len(dfChr))
            my_list.append(len(dfChr[dfChr[alien[i]] <= score_threshold]))          
            my_list.append(float(f'{((len(dfChr[dfChr[alien[i]] <= score_threshold]) / len(dfChr)) * 100):.2f}'))
               
            dfNew.loc[len(dfNew)] = my_list
            my_list = []

#st.write(dfNew.query("Percent".max())["Variety"])
st.write(dfNew['Percent'].max())
  
st.write(dfNew[dfNew['Percent'] == dfNew['Percent'].max]['Variety'])
      
st.write(dfNew)

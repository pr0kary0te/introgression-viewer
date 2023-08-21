# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 11:34:14 2023

@author: bzmow
"""

import streamlit as st
import pandas as pd
import altair as alt
import plotly.figure_factory as ff
from matplotlib import pyplot
from scipy.stats import spearmanr

st.set_page_config(page_title='TaNG v1.1 Markers', layout="wide")

st.markdown(""" <style> .font1 {
    font-size: 45px; font-family: 'Copper Black'; color: #FF9633}
    </style> """, unsafe_allow_html=True)

st.markdown(""" <style> .font2 {
    font-size: 30px; font-family: 'Copper Black'; color: #FF9633}
    </style> """, unsafe_allow_html=True)

st.markdown(""" <style> .p { color: #FF0000} </style> """, unsafe_allow_html=True)

st.markdown('<h1 class="font1">SNP Markers on the TaNG v 1.1 Array</h1>', unsafe_allow_html=True)
st.markdown('')

################################# FUNCTIONS ###################################

def getChromosome(marker):
    
#    overview = dfRosetta.loc[dfRosetta['TaNG v1.1 AX code'] == marker]
    overview = dfTaNG_Rosetta.loc[dfTaNG_Rosetta['probeset_id'] == marker]
    # Transpose the overview table so that column headers become row labels
    overviewT = overview.T
#    colour = dfTaNG['Traffic Light'].loc[dfTaNG['probeset_id'] == marker]
    colour = dfTaNG_Rosetta['Traffic Light'].loc[dfTaNG_Rosetta['probeset_id'] == marker]
#    chromosome = dfTaNG['Chr'].loc[dfTaNG['probeset_id'] == marker]
    chromosome = dfTaNG_Rosetta['Chr'].loc[dfTaNG_Rosetta['probeset_id'] ==  marker]
    chromosomeClean = chromosome.iloc[0]

    return(overviewT, colour, chromosomeClean)    
    
    

def getChrSpecificMarkers(dfTaNG, chromosomeClean):
    
    # Select all the markers that are on the same chromosome as the selected marker
    # 'chromosome.iloc[0]'.  That is, restrict the dataset to just the chromosome on
    # which the marker is to be found.
#    dfTaNGChr = dfTaNG.loc[(dfTaNG['Chr'] == chromosomeClean)]
    dfTaNGChr = dfTaNG_Rosetta.loc[(dfTaNG_Rosetta['Chr'] == chromosomeClean)]
    # Create a new DataFrame that just contains the listed columns; that is the 
    # columns containing the genotype calls will be dropped
    dfTaNGChr2 = dfTaNGChr[['probeset_id', 'Affx Code', 'Call Rate', 'Conversion Type', 'MAF', 'Chr', 'Pos', 'Traffic Light', '35K Breeders Array', 'Allele A', 'Allele B']]
    # Sort the DataFrame by the 'Pos' column
    dfTaNGChrSorted = dfTaNGChr2.sort_values(by = 'Pos')
    # Add anew column, 'markerScore' to the DataFrame and assign 0 globally
    dfTaNGChrSorted2 = dfTaNGChrSorted.assign(markerScore = 0)
    # Change the value in the 'markerScore' column just created to have values that 
    # reflect the 'Traffic Light' column
    dfTaNGChrSorted2.loc[dfTaNGChrSorted2['Traffic Light'] == 'Red', 'markerScore'] = -0.2
    dfTaNGChrSorted2.loc[dfTaNGChrSorted2['Traffic Light'] == 'Amber', 'markerScore'] = -0.1
    dfTaNGChrSorted2.loc[dfTaNGChrSorted2['Traffic Light'] == 'Green', 'markerScore'] = 0

    return dfTaNGChrSorted2


def getImage(chrm):
    
    chrm_scale = {
        '1A': '1A.png',
        '2A': '2A.png',
        '3A': '3A.png',
        '4A': '4A.png',
        '5A': '5A.png',
        '6A': '6A.png',
        '7A': '7A.png',
        '1B': '1B.png',
        '2B': '2B.png',
        '3B': '3B.png',
        '4B': '4B.png',
        '5B': '5B.png',
        '6B': '6B.png',
        '7B': '7B.png',
        '1D': '1D.png',
        '2D': '2D.png',
        '3D': '3D.png',
        '4D': '4D.png',
        '5D': '5D.png',
        '6D': '6D.png',
        '7D': '7D.png'
        }
            
    st.header(f'Chromosome {chrm}')

    legend1_text = 'Schematic representation of chromosome ' + chrm + ': image length (scale bar) is based on the mean number of 50 Kb bins spanning chromosome ' + chrm + ' in the 11 reference genomes; morphology is based on Gill (2015).  The scale bar is in bin numbers and relates directy to the underlying plots; one can convert length to Mb by multiplying bin number by 50,000.'

    legend1_text_6A = '  Please note, Spelt chromosome '+ chrm + ' is smaller (11,670 bins) than that of the other reference varieties'
    legend1_text_2B = '  Please note, Lancer chromosome ' + chrm + ' is smaller (13,432 bins) than that of the other reference varieties'
    legend1_text_3B = '  Please note, Arina chromosome ' + chrm + ' is larger (17,817 bins) than that of the other reference varieties'
    legend1_text_5B = '  Please note, Arina and SY Mattis carry the chromosome whole arm translocation chromosome 5BS / 7BS rather than 5B.'
    legend1_text_7B = '  Please note, Arina and SY Mattis carry the chromosome whole arm translocation chromosome 5BL / 7BL rather than 7B.'

    if chrm == '6A':
        legend1_text = legend1_text + legend1_text_6A
    elif chrm == '2B':
        legend1_text = legend1_text + legend1_text_2B    
    elif chrm == '3B':
        legend1_text = legend1_text + legend1_text_3B        
    elif chrm == '5B':
        legend1_text = legend1_text + legend1_text_5B 
    elif chrm == '7B':
        legend1_text = legend1_text + legend1_text_7B
    else:
        legend1_text = legend1_text
          
    imagePath = './images/' + chrm_scale[chrm]
            
    return(imagePath, legend1_text)


def getTable(dfTaNG_Rosetta, markerType):
    
    chromo = ['1A', '2A', '3A', '4A', '5A', '6A', '7A',
            '1B', '2B', '3B', '4B', '5B', '6B', '7B',
            '1D', '2D', '3D', '4D', '5D', '6D', '7D']

    Alist = []
    Blist = []
    Dlist =[]
    
    for chromosome in chromo:
        df = dfTaNG_Rosetta.loc[chromosome]
        bool_series = pd.notnull(df[markerType])
        df = df[bool_series]

        if chromosome[1] == 'A':
            Alist.append(df.shape[0])
        elif chromosome[1] =='B':
            Blist.append(df.shape[0])
        elif chromosome[1] == 'D':
            Dlist.append(df.shape[0])
            
    scoresDict = {'A': Alist,
                  'B': Blist,
                  'D': Dlist
                  } 

    df1 = pd.DataFrame(scoresDict)
    index = pd.Index([1,2,3,4,5,6,7])
    df2 = df1.set_index(index)
    
    return(df2)
    
    
###############################################################################
###############################################################################


dfTaNG = pd.read_csv('./data/TaNG1-1.csv')
#dfRosetta = pd.read_csv('./data/RosettaStone.csv')

dfTaNG_Rosetta = pd.read_csv('./data/TaNG-RosettaStone.csv')

# st.write(dfRosetta)
# st.write(dfTaNG)

###############################################################################
# The following lines of script are used to get the column headers, which include
# the names of the varieties that have been genotyped, so that they can be printed

# column_names = list(dfTaNG.columns.values)
# for item in column_names:
#     item_reduced = item[4:]
    #st.write(f'{item_reduced}')

###############################################################################

# Setup a form to input SNP marker AX- codes; this may be either a single marker
# code or a CSV file contianing a list of markers.

col1, col2 = st.columns([4,5], gap='small')

with col1:

    with st.form("my_form", clear_on_submit=True):
        st.markdown('<h2 class="font2">Enter a Single Marker</h1>', unsafe_allow_html=True)
        markerSingle = st.text_input("marker AX Code")
    
        st.markdown('<h2 class="font2">or Upload a CSV File</h1>', unsafe_allow_html=True)
    
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            dataframe = pd.read_csv(uploaded_file)
            markerFromList = dataframe['Marker'][0] 
            #markerList = dataframe['Marker'].tolist()

    # Now add a submit button to the form:
        submit = st.form_submit_button("Submit")
        
with col2:
    
    example = ['Marker',
               'AX_643833569',
               'AX-643869398',
               'AX-95250140'
               ]
    
    exampleTable = pd.Series(example)
    
    
    st.markdown("""
                
        Using this page, one can visual the chromosome position of selected
        markers as well as the distribution of all the TaNG v 1.1
        Array markers on the chromosome (with respect to the Chinese Spring genome).
        
        One can enter a single SNP marker code (e.g., AX-108750802) or upload a
        csv file containing a list on markers from a single chromosome.  The
        format of the csv file should be as follows:
            
        """)
        
    st.write(exampleTable)
        
    st.markdown("""
                
        Upload the file using the 'Browse files' button and then press the
        "submit" button.   
                
        """)
     

    

if submit:
    if not markerSingle and not uploaded_file:
        st.warning("You haven't entered a marker code or uploaded a file containing a list of markers!")
        st.stop()

        
    elif markerSingle is not None and not uploaded_file:
        marker = markerSingle
        
        chromosomeResult = getChromosome(marker)
        
        chromosomeClean = chromosomeResult[2]
        
        colour = chromosomeResult[1]
        
        # overview = dfRosetta.loc[dfRosetta['TaNG v1.1 AX code'] == marker]
        # # Transpose the overview table so that column headers become row labels
        # overviewT = overview.T
        # colour = dfTaNG['Traffic Light'].loc[dfTaNG['probeset_id'] == marker]
        # chromosome = dfTaNG['Chr'].loc[dfTaNG['probeset_id'] == marker]
        # chromosomeClean = chromosome.iloc[0]

        dfTaNGChrSorted2 = getChrSpecificMarkers(dfTaNG, chromosomeClean)

        dfTaNGChrSorted2.loc[dfTaNGChrSorted2['probeset_id'] == marker, 'markerScore'] = 2

#        st.write(dfTaNGChrSorted2)
       
        st.markdown(f'<h1 class="font2">Marker {marker} is on Chromosome {chromosomeResult[2]} ({colour.iloc[0]})</h1>', unsafe_allow_html=True)
  
        bool_seriesA = pd.notnull(dfTaNGChrSorted2['35K Breeders Array'])
#        df35K = dfTaNGChrSorted2.loc[dfTaNGChrSorted2['35K Breeders Array'] != 'Not on 35K Array']
        df35K = dfTaNGChrSorted2[bool_seriesA]


        # Making two lists for
        # values and colors resp.
        dom = ['Green', 'Amber', 'Red']
        rng = ['green', 'orange', 'red']
        
        chrLengths = {'1A': 594, '2A': 781, '3A': 751, '4A': 745, '5A': 710, '6A': 618, '7A': 737,
                      '1B': 690, '2B': 801, '3B': 831, '4B': 674, '5B': 714, '6B': 721, '7B': 751,
                      '1D': 496, '2D': 652, '3D': 616, '4D': 510, '5D': 566, '6D': 474, '7D': 639}
        
        
        xaxis = chrLengths[chromosomeClean]*1000000

        c = alt.Chart(dfTaNGChrSorted2).mark_circle().encode(
            x=alt.X('Pos', scale=alt.Scale(domain=[0, xaxis])), y=alt.Y('markerScore', scale=alt.Scale(domain=[-0.3, 2])), color=alt.Color('Traffic Light', scale=alt.Scale(domain=dom, range=rng)), tooltip=['probeset_id', 'Allele A', 'Allele B'])

        st.altair_chart(c, use_container_width=True)
        
        st.markdown(f'<h1 class="font2">3K Breeders Array Markers on Chromosome {chromosomeResult[2]} ({colour.iloc[0]})</h1>', unsafe_allow_html=True)
        
        c2 = alt.Chart(df35K).mark_circle().encode(
            x=alt.X('Pos', scale=alt.Scale(domain=[0, xaxis])), y=alt.Y('markerScore', scale=alt.Scale(domain=[-0.3, 2])), color=alt.Color('Traffic Light', scale=alt.Scale(domain=dom, range=rng)), tooltip=['probeset_id', 'Allele A', 'Allele B'])

        st.altair_chart(c2, use_container_width=True)       
        
        chrm = chromosomeClean
        
        with st.expander(f'Chromosome {chrm} diagram'):
        
            image = getImage(chrm)
            st.image(image[0], caption=image[1])
            
        st.write(chromosomeResult[0])
        st.write(df35K)            

    elif uploaded_file is not None and not markerSingle:
        marker = markerFromList
        markerList = dataframe['Marker'].tolist()
        
        chromosomeResult = getChromosome(marker)
        
        chromosomeClean = chromosomeResult[2]
        
        dfTaNGChrSorted2 = getChrSpecificMarkers(dfTaNG, chromosomeClean)         

        for item in markerList:
            dfTaNGChrSorted2.loc[dfTaNGChrSorted2['probeset_id'] == item, 'markerScore'] = 2


        st.markdown(f'<h1 class="font2">All Markers on Chromosome {chromosomeClean}</h1>', unsafe_allow_html=True)

#        chart1_data = dfTaNGChrSorted2
        
        bool_seriesA = pd.notnull(dfTaNGChrSorted2['35K Breeders Array'])
#        df35K = dfTaNGChrSorted2.loc[dfTaNGChrSorted2['35K Breeders Array'] != 'Not on 35K Array']
        df35K = dfTaNGChrSorted2[bool_seriesA]

        # Making two lists for
        # values and colors resp.
        dom = ['Green', 'Amber', 'Red']
        rng = ['green', 'orange', 'red']
        
        chrLengths = {'1A': 594, '2A': 781, '3A': 751, '4A': 745, '5A': 710, '6A': 618, '7A': 737,
                      '1B': 690, '2B': 801, '3B': 831, '4B': 674, '5B': 714, '6B': 721, '7B': 751,
                      '1D': 496, '2D': 652, '3D': 616, '4D': 510, '5D': 566, '6D': 474, '7D': 639}
        
        
        xaxis = chrLengths[chromosomeClean]*1000000

        c = alt.Chart(dfTaNGChrSorted2).mark_circle().encode(
            x=alt.X('Pos', scale=alt.Scale(domain=[0, xaxis])), y=alt.Y('markerScore', scale=alt.Scale(domain=[-0.3, 2])), color=alt.Color('Traffic Light', scale=alt.Scale(domain=dom, range=rng)), tooltip=['probeset_id', 'Allele A', 'Allele B'])

        st.altair_chart(c, use_container_width=True)

        dfToWrite = dfTaNGChrSorted2.drop(columns=['markerScore'])

        st.markdown(f'<h1 class="font2">35K Breeders Array Markers on Chromosome {chromosomeClean}</h1>', unsafe_allow_html=True)
        
        c2 = alt.Chart(df35K).mark_circle().encode(
            x=alt.X('Pos', scale=alt.Scale(domain=[0, xaxis])), y=alt.Y('markerScore', scale=alt.Scale(domain=[-0.3, 2])), color=alt.Color('Traffic Light', scale=alt.Scale(domain=dom, range=rng)), tooltip=['probeset_id', 'Allele A', 'Allele B'])

        st.altair_chart(c2, use_container_width=True)

        chrm = chromosomeClean
###############

        x1 = dfTaNGChrSorted2['markerScore']     

        # Group data
        hist_data = [x1]

        group_labels = ['Marker Score']

        # Create distplot with custom bin_size
        fig = ff.create_distplot(
            hist_data, group_labels)
            
        # Plot the density distribution chart
        st.plotly_chart(fig, use_container_width=True)
################       
        with st.expander(f'Chromosome {chrm} diagram'):
        
            image = getImage(chrm)
            st.image(image[0], caption=image[1])
            
        with st.expander(f'Tables showing all TaNG markers on {chrm}'):    
        
            st.write(dfToWrite)
        
        with st.expander('Table showing TaNG Markers that are also on the 35K Breeders Array'):
 
            df35K = df35K.drop(columns=['markerScore'])
            st.write(df35K)

        
###############################################################################
# The following lines of script are used to pull out all the markers between a 
# selected range (Mb) on the chromosome.


    # # st.markdown('<h1 class="font1">Enter start</h1>', unsafe_allow_html=True)
    # # start = st.text_input("Start Position")
    # # end = st.text_input('End Position')
    
    # start = 1000000
    # end = 4000000
    # includedMarkers = dfTaNGChrSorted2.loc[(dfTaNGChrSorted2['Pos'] >= start) & (dfTaNGChrSorted2['Pos'] <= end)]
        
    # st.write(f'There are {len(includedMarkers)} markers in the selected region')
        
    # st.write(includedMarkers)
        
    # # Making two lists for
    # # values and colors resp.
    # dom = ['Green', 'Amber', 'Red']
    # rng = ['green', 'orange', 'red']
        
    # c = alt.Chart(includedMarkers).mark_circle().encode(
    #     x='Pos', y='markerScore', color=alt.Color('Traffic Light', scale=alt.Scale(domain=dom, range=rng)), tooltip=['probeset_id', 'Allele A', 'Allele B'])

    # st.altair_chart(c, use_container_width=False)

###############################################################################
        
else:
    
    st.write('No marker or marker list supplied!')
    

###############################################################################

# The following lines of script uses the data in the dfTaNG dataframe - derived
# from the TaNG-1.csv file - and pulls out summaries based on Amanda's traffic
# light system for giving confidence to the genotype calls for the various
# markers (obviously, these are related to the data set - wheat accessions - studied)


# chrm = ['1A', '2A', '3A', '4A', '5A', '6A', '7A',
#         '1B', '2B', '3B', '4B', '5B', '6B', '7B',
#         '1D', '2D', '3D', '4D', '5D', '6D', '7D']

# for item in chrm:
#     st.write(item)
#     df = dfTaNG.loc[(dfTaNG['Chr'] == item)]
#     red = len(df.loc[(df['Traffic Light'] == 'Red')])
#     redMono = len(df.loc[(df['Traffic Light'] == 'Red') & (df['Conversion Type'] == 'MonoHighResolution') ])
#     amber = len(df.loc[(df['Traffic Light'] == 'Amber')])    
#     green = len(df.loc[(df['Traffic Light'] == 'Green')])
    
#     st.write(f'Chromosome {item}: Red = {red}, Amber = {amber}, Green = {green}')
#     st.write(f'{red / (red + amber + green)}%')
#     st.write(f'{(red + amber) / (red + amber + green)}%')
#     st.write(f'Red and monomorphic {redMono}')
    
#     st.write(len(dfRosetta.loc[dfRosetta['Chr'] == item]))
    
# st.write(len(dfTaNG.loc[dfTaNG['Traffic Light'] == 'Red']))    
# st.write(len(dfTaNG.loc[dfTaNG['Traffic Light'] == 'Amber']))
# st.write(len(dfTaNG.loc[dfTaNG['Traffic Light'] == 'Green']))

###############################################################################

dfTaNG_Rosetta.set_index(['Chr'], inplace=True)

markerTypes = ['probeset_id', '820K HD Array', '35K Breeders Array', 'BA Code', 'BS Code']

counter = 1

st.markdown('<h1 class="font2">Tabular Summary of Markers on TaNG v 1.1 Array</h1>', unsafe_allow_html=True)

for markerType in markerTypes:
    
    df = getTable(dfTaNG_Rosetta, markerType)
    
    counter += 1
    
    if counter == 2:
        df1 = df
    if counter == 3:
        df2 = df
    if counter == 4:
        df3 = df
    if counter == 5:
        df4 = df
    if counter == 6:
        df5 = df       

col3, col4, col5, col6, col7 = st.columns([1,1,1,1,1], gap='small')  

with col3:
    
    st.markdown('#### All TaNG markers', unsafe_allow_html=True)
    st.write(df1)

with col4:
    st.markdown('#### On 820K Array', unsafe_allow_html=True)    
    st.write(df2)
    
with col5:
    st.markdown('#### On 35K Array', unsafe_allow_html=True)    
    st.write(df3)
    
with col6:
    st.markdown('#### Have BA Code', unsafe_allow_html=True)    
    st.write(df4)
    
with col7:
    st.markdown('#### Have BS Code', unsafe_allow_html=True)    
    st.write(df5)
    
    
chrmSize = [594150000,780800000,750850000,744600000,709800000,618100000,736750000,
            689900000,801300000,830850000,673650000,713150000,721000000,750650000,
            495500000,651900000,615600000,509900000,566100000,473600000,638700000
            ]

numMarkers = [2087,2295,2054,2223,2016,1897,2302,
              2343,2425,2428,1883,2230,2027,1890,
              2025,2238,2004,1540,1857,1593,2015
              ]

pyplot.scatter(chrmSize, numMarkers)
pyplot.show()
coef, p = spearmanr(chrmSize, numMarkers)
print('Spearmanscorrelation coefficient: %.3f' % coef)
alpha = 0.05
if p > alpha:
    print('Samples are uncorrelated (Null Hypothesis, HO, can not be rejected: p=%.3f' % p)
else:
    print('Samples are correlated (Null Hypothesis, HO, can be rejected) p=%.3f' % p)
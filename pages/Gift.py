# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 11:34:14 2023

@author: bzmow
"""

import streamlit as st
import pandas as pd
import altair as alt
#import os
import plotly.express as px
from io import StringIO

st.set_page_config(page_title="Gene Positions Along Chromosomes", layout="wide")
#st.write(os.getcwd())
st.markdown(""" <style> .font1 {
    font-size: 45px; font-family: 'Copper Black'; color: #FF9633}
    </style> """, unsafe_allow_html=True)

st.markdown(""" <style> .font2 {
    font-size: 30px; font-family: 'Copper Black'; color: #FF9633}
    </style> """, unsafe_allow_html=True)

st.markdown(""" <style> .p { color: #FF0000} </style> """, unsafe_allow_html=True)

st.markdown('<h1 class="font1">Gene Distribution on Chromosomes</h1>', unsafe_allow_html=True)
st.markdown('')

###############################################################################
################################# FUNCTIONS ###################################
###############################################################################

def makeNegative(resultDown):
    
    chromo = ['1A', '2A', '3A', '4A', '5A', '6A', '7A',
            '1B', '2B', '3B', '4B', '5B', '6B', '7B',
            '1D', '2D', '3D', '4D', '5D', '6D', '7D']

    for i in chromo:
        resultDown[i] = resultDown[i].apply(lambda x: x*-1)
        
    return(resultDown)

###############################################################################

def createBins(n):
    
    chrmLength = {'1A': 594102056, '2A': 780798557, '3A': 750843639, '4A': 744588157, '5A': 709773743, '6A': 618079260, '7A': 736706236,
                  '1B': 689851870, '2B': 801256715, '3B': 830829764, '4B': 673617499, '5B': 713149757, '6B': 720988478, '7B': 750620385,
                  '1D': 495453186, '2D': 651852609, '3D': 615552423, '4D': 509857067, '5D': 566080677, '6D': 473592718, '7D': 638686055
                 } 

    binList = []
    binDict = {}

    for key, value in chrmLength.items():
        binLength = value / n
        for i in range(0,(n+1)):
            endPoint = int(binLength * i)
            binList.append(endPoint)
        binDict.update({key: binList})
        binList = []

    return(binDict)

###############################################################################

def createBinnedData(genesUp, genesDown, binDict, number):
    
    # This function takes in the data for the up- and down-regulated genes (the
    # dataframes 'genesUp' and 'genesDown'), and the dictionary of bin boundaries
    # based on the selected number of bins, and produces two dataframes of the
    # following format:
    #  
    #     1A,  2A,  3A,  4A,  5A,   6A,  ...  7D
    #    139,  63,	19,	  5,   3,	11,  ...  21
    #     97,	4,	 2,	  1,   1,	 4,  ...   2
    #     81,	1,	 1,	  2,   3,	 1,  ...   2
    #     89,	1,	 1,	  5,   1,	 3,  ...   1
    #     58,	0,	 2,	  1,   0,	 0,  ...   2
    #
    # NB. The numbers for the downregulated genes are multiplied by -1 so that
    # they become negative.
    
    fileList = [genesUp, genesDown]
    
    chromo = ['1A', '2A', '3A', '4A', '5A', '6A', '7A',
            '1B', '2B', '3B', '4B', '5B', '6B', '7B',
            '1D', '2D', '3D', '4D', '5D', '6D', '7D']
    
    counter = 0
 
    for fileName in fileList:
        print(fileName)
        df = fileName
        # Declare an empty dictionary into whcih will be collected the counts
        # for each of n bins for each chromosome.
        markerNumDict = {}

        # Loop through the list of chromosome names (chromo)
        # and create a dataframe of the data for that chromosome.
        # Also initiate a list, markerNumList, to contain the
        # number of genes in each bin.
        for item in chromo:
            markerNumList = []
            dfChr = df[df['seqid'] == item]
            # Finally, loop through the dictionary binDict which
            # contains the boundaries for the bins and count how
            # many genes are in each
            for i in range(0,number):
                numMarkers = (len(dfChr[(dfChr['start'] > binDict[item][i]) & (dfChr['start'] < (binDict[item][i + 1]))]))
                # Append the number of markers (basically, the
                # length of the dataframe, dfChr, having that
                # chromosome as 'seqid'
                markerNumList.append(numMarkers)
            # When the script has looped through all 20 bins
            # for the selected chromosome, and counted how many
            # genes there are in each, the list is converted to
            # a dictionary and then a dataframe that can be 
            # written to a csv file    
            markerNumDict[item] = markerNumList
        if counter == 0: 
            dfResultsUp = pd.DataFrame(markerNumDict)
            counter = 1
        elif counter == 1:
            dfResultsDown = pd.DataFrame(markerNumDict)
            dfResultsDown = makeNegative(dfResultsDown)
            counter = 0
            
    return(dfResultsUp, dfResultsDown)

###############################################################################

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

###############################################################################

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

# Read in data from csv files
# This data is used to plot bar charts: each bar represents the number of 
# genes/markers in a bin of a given length (as a fraction of total chromosome length) 
#    
# the following two files are csv files of the form:
#
#   seqid,	source,	type,	   start,	     end, score, strand, phase,  attributes
#    1A,	    IWGSC,	gene,	13346605,	13352572,	.,	   +,	  .,	 ID=gene:TraesCS1A02G028500
#    1A,	    IWGSC,	gene,	13971819,	13976728,	.,	   +,	  .,	 ID=gene:TraesCS1A02G029900
#    1A,	    IWGSC,	gene,	53436194,	53438543,	.,	   +,	  .,	 ID=gene:TraesCS1A02G070500
#    1A,	    IWGSC,	gene,  257987100,  257987438,	.,	   +,	  .,	 ID=gene:TraesCS1A02G150300
#
# This data is used directly to plot the position of genes/markers along
# chromosome arms.  The data is also use in the self defined fuction,
# 'createBinnedData', to plot bar cahrts    


# genesUp = pd.read_csv('./data/a_up.csv')
# genesDown = pd.read_csv('./data/a_down.csv')

with st.form('my_form', clear_on_submit=False):
    
    message = '''Using the four input buttons, select the files containing the
                 list of up- and down-regulated genes, the chromosome you wish
                 to view,and the number of bins for plotting the bar chart.  
                 Once selection has been made, hit the *Submit* button.
              '''
    
    st.markdown(message)
    
    col1, col2, col3, col4 = st.columns([2,2,1,1], gap='small')

    with col4:

        number = st.number_input("Number of bins (value between 10 and 100)", value=20,
                             min_value=10, max_value=100)
    
    with col3:

        chrm = st.selectbox(
            'Select chromosome',
            ['1A', '2A', '3A', '4A', '5A', '6A', '7A',
             '1B', '2B', '3B', '4B', '5B', '6B', '7B',
             '1D', '2D', '3D', '4D', '5D', '6D', '7D'],
            0
            )

    with col1:

        uploaded_file1 = st.file_uploader("Choose a file containing up-regulated genes", key='file1')
        if uploaded_file1 is not None:
            genesUp = pd.read_csv(uploaded_file1)
        else:
            genesUp = pd.read_csv('./data/a_up.csv')

    with col2:

        uploaded_file2 = st.file_uploader("Choose a file containing down-regulated genes", key='file2')
        if uploaded_file2 is not None:
            genesDown = pd.read_csv(uploaded_file2)
        else:
            genesDown = pd.read_csv('./data/a_down.csv')

    submit = st.form_submit_button('Submit')

binDict = createBins(number)
dfBins = pd.DataFrame.from_dict(binDict)

with st.expander('Click to view bin boundaries', expanded = False):
    st.table(binDict)

st.header('Number of Genes in Bins Across on Chromosomes')
st.write(f'Selected chromosome: {chrm}')

# Use the function 'createBinnedData' (see above) to count the number of 
# markers in each of the bins (this number is input by the user)
resultUp, resultDown = createBinnedData(genesUp, genesDown, binDict, number)

# Create a dictionary to hold the data for the up- and down-regulated genes.  This
# dictionary is then used to create a dataframe, df.
upDownData = {
    'Up': resultUp[chrm].tolist(),
    'Down': resultDown[chrm].tolist()
    }

indexLabels = []
for i in range(1, len(resultUp)+1):
    binName = 'Bin ' + str(i)
    indexLabels.append(binName)

df = pd.DataFrame(upDownData, index=indexLabels) 


col1, col2 = st.columns([5,2], gap='large')

with col2:
    
    with st.expander('Click to view data table', expanded = False):
        
        st.table(df)
    
with col1:

    resultUpDown = pd.concat([resultUp, resultDown])
    
    df['Bins'] = indexLabels
    
    groups = df['Bins']
    values = [df['Up'], df['Down']]
    
    fig = px.bar(x=groups, y=(values),
                 title = 'Number of Up and Down Regulated Genes',
                 labels = {'x': 'Bins', 'value': 'Number of Genes'},
                 color_discrete_sequence = ['green', 'red']
#                 color_discrete_map = {'1': 'green', '-1': 'red'}
                )
    fig.update_layout(yaxis_range=[-140, 30])
 
    st.plotly_chart(fig, use_container_width=True)



st.header('Gene Positions on Chromosomes')

genesUp['show'] = '1'
genesDown['show'] = '-1'

genesUpDown = pd.concat([genesUp, genesDown])

chart1_data = genesUpDown[genesUpDown['seqid'] == chrm]


fig = px.scatter(x = chart1_data['start'],
                 y = chart1_data['show'],
                 title = "Up and Down Regulated Genes",
                 labels = {'x': 'Genes', 'y':'Change'},
                 color = chart1_data['show'],
#                 color_discrete_sequence = ['green', 'red'],
                 color_discrete_map = {'1': 'green', '-1': 'red'},
                 symbol = chart1_data['strand'],
                 hover_data = [chart1_data['attributes']],
                 height = 300)
#fig.update_layout(showlegend = False)

st.plotly_chart(fig, use_container_width=True)




# dom = ['increase', 'sdecrease']
# rng = ['green', 'red']
# point_size = [20, 30]

# c = alt.Chart(chart1_data).mark_point().encode(
#         x='start',
#         y='show',
#         color=alt.Color('show', scale=alt.Scale(domain=dom, range=rng)),
#         shape='strand',
# #        size=alt.Size('strand'),
#         tooltip=['attributes'])

# st.altair_chart(c, use_container_width=True)

with st.expander('Click to view data table', expanded = False):

        st.write(chart1_data)

###############################################################################



    
    
    
    
    
    
    
    
    
    
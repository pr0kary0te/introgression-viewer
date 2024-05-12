# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 11:34:14 2023

@author: bzmow
"""

import streamlit as st
import pandas as pd
import plotly.express as px

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

def getGeneName(df):
    
    geneNamesList = []
    proteinNamesList = []
    
    attributes = df['attributes']

    for i in attributes:
        protein = ''
        stringHolder = i.split(';')
        geneName = stringHolder[0].split(':')
        geneNamesList.append(geneName[1])
        for k in stringHolder:
            if 'description' in k:
                protein = k.split('=')
                protein = protein[1]
                proteinNamesList.append(protein)
        if protein == '':
            proteinNamesList.append('No protein desription')
            
    df['gene'] = geneNamesList
    df['protein'] = proteinNamesList

    return(df)

###############################################################################
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
    
    col1, col2, col3 = st.columns([2,2,2], gap='small')

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
    
    with col3:
        
        chrm = st.selectbox(
            'Select chromosome',
            ['1A', '2A', '3A', '4A', '5A', '6A', '7A',
             '1B', '2B', '3B', '4B', '5B', '6B', '7B',
             '1D', '2D', '3D', '4D', '5D', '6D', '7D'],
            0
            )

#    with col4:

        number = st.number_input("Number of bins (value between 10 and 100)", value=20,
                             min_value=10, max_value=100)
    

    submit = st.form_submit_button('Submit')

binDict = createBins(number)
dfBins = pd.DataFrame.from_dict(binDict)

with st.expander('Click to view bin boundaries', expanded = False):
    st.table(binDict)

st.header(f'Number of Genes in {number} Bins Spanning Chromosome {chrm}')

st.markdown('''
                Hover over the bars of the plot to see the number of genes.
                Zoom in and out of the plot using the controls at the top right of the plot.
            '''
           )

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
#                 title = 'Number of Up and Down Regulated Genes',
                 labels = {'x': 'Bins', 'value': 'Number of Genes'},
                 color_discrete_sequence = ['green', 'red']
#                 color_discrete_map = {'1': 'green', '-1': 'red'}
                )
    fig.update_layout(yaxis_range=[-140, 30])
 
    st.plotly_chart(fig, use_container_width=True)



st.header(f'Position of Genes on Chromosome {chrm}')

st.markdown('''
                Hover over the sctter plot to see the names of the genes and, where available, the name of the protein for which they code.
                Zoom in and out of the plot using the controls at the top right of the plot.
            '''
           )


genesUp = getGeneName(genesUp)
genesDown = getGeneName(genesDown)

genesUp['show'] = '1'
genesDown['show'] = '-1'

genesUpDown = pd.concat([genesUp, genesDown])

genesUpDownChr = genesUpDown[genesUpDown['seqid'] == chrm]


fig = px.scatter(x = genesUpDownChr['start'],
                 y = genesUpDownChr['show'],
#                 title = "Up and Down Regulated Genes",
                 labels = {'x': 'Gene Position (bp)', 'y':'Change'},
                 color = genesUpDownChr['show'],
#                 color_discrete_sequence = ['green', 'red'],
                 color_discrete_map = {'1': 'green', '-1': 'red'},
                 symbol = genesUpDownChr['strand'],
                 hover_data = [genesUpDownChr['gene'], genesUpDownChr['protein']],
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
    
        genesUpDownChr.drop(['source', 'type', 'phase', 'attributes'], axis = 1, inplace = True)
        st.write(genesUpDownChr)

###############################################################################
    
    
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:39:59 2022

@author: bzmow
"""
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import altair as alt

st.set_page_config(layout="wide")

st.markdown(""" <style> .font1 {
    font-size: 45px; font-family: 'Copper Black'; color: #FF9633}
    </style> """, unsafe_allow_html=True)

st.markdown(""" <style> .font2 {
    font-size: 30px; font-family: 'Copper Black'; color: #FF9633}
    </style> """, unsafe_allow_html=True)


################################# FUNCTIONS ###################################


def getData(filePath):
    df = pd.read_csv(filePath, compression='gzip', header=0, sep=',')
    return df


def change_index(df):
    bin_list = list(range(1, (len(df) + 1)))
    df['Adjusted Bin'] = bin_list
    # df.set_index('Adjusted Bin', inplace=True)

    return df


def changeColNames(dfChrNew):

    dfChrNew = dfChrNew.rename(columns={'ENT336': 'Ae. tauschii (ENT336)',
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

# for key in st.session_state.keys():
#     del st.session_state[key]

with st.sidebar:

    with st.form('my_form', clear_on_submit=False):

        refGenome = st.selectbox(
            label='Select Reference Genome:',
            options=('Arina', 'Chinese Spring', 'Jagger',
                     'Julius', 'Lancer', 'Landmark', 'Mace',
                     'Norin61', 'Spelt', 'Stanley', 'Mattis'),
            index=4,
            key='ref')

# Update the index. It is used in the selectbox.
    # st.session_state.index = st.session_state.genome.index(st.session_state.ref)

        refFiles = {'Arina': ['https://www.cerealsdb.uk.net/ibspy/aliensArina.csv.gz', '_WhAri'],
                    'Chinese Spring': ['https://www.cerealsdb.uk.net/ibspy/aliensChineseSpring.csv.gz', ''],
                    'Jagger': ['https://www.cerealsdb.uk.net/ibspy/aliensJagger.csv.gz', '_WhJag'],
                    'Julius': ['https://www.cerealsdb.uk.net/ibspy/aliensJulius.csv.gz', '_Whjul'],
                    'Lancer': ['https://www.cerealsdb.uk.net/ibspy/aliensLancer.csv.gz', '_Whlan'],
                    'Landmark': ['https://www.cerealsdb.uk.net/ibspy/aliensLandmark.csv.gz', '_WhLan'],
                    'Mace': ['https://www.cerealsdb.uk.net/ibspy/aliensMace.csv.gz', '_Whmac'],
                    'Norin61': ['https://www.cerealsdb.uk.net/ibspy/aliensNorin61.csv.gz', '_WhNor'],
                    'Spelt': ['https://www.cerealsdb.uk.net/ibspy/aliensSpelta.csv.gz', '_Whspe'],
                    'Stanley': ['https://www.cerealsdb.uk.net/ibspy/aliensStanley.csv.gz', '_WhSta'],
                    'Mattis': ['https://www.cerealsdb.uk.net/ibspy/aliensMattis.csv.gz', '_WhSYM']
                    }

        filePath = refFiles[refGenome][0]

        df = getData(filePath)

        # df.rename(columns={'timopheevii10558_nuq.jf': 'timopheevii10558_nuq_jf',
        #                    'timopheevii14352_nuq.jf': 'timopheevii14352_nuq_jf',
        #                    'timopheevii15832_nuq.jf': 'timopheevii15832_nuq_jf',
        #                    'timopheevii22438_nuq.jf': 'timopheevii22438_nuq_jf',
        #                    'timopheevii3708_nuq.jf': 'timopheevii3708_nuq_jf'},
        #                      inplace=True)

        alienGenomeList = ['Ae. columnaris 38',
                           'Ae. comosa 40',
                           'Ae. comosa 41',
                            'Ae. crassa 20',
                            'Ae. crassa 22',
                            'Ae. cylindrica 24',
                            'Ae. cylindrica 25',
                            'Ae. juvenalis 27',
                            'Ae. juvenalis 29',
                            'Ae. kotschyii 26',
                            'Ae. kotschyii 31',
                            'Ae. longissima 30',
                            'Ae. mutica 52',
                            'Ae. mutica 54',
                            'Ae. ovata 56',
                            'Ae. ovata 57',
                            'Ae. searsii 21',
                            'Ae. searsii 59',
                            'Ae. sharonensis 61',
                            'Ae. sharonensis 63',
                            'Ae. speltoides 58',
                            'Ae. speltoides 60',
                            'Ae. speltoides (10x_nuq)',
                            'Ae. tauschii 50',
                            'Ae. tauschii 68',                            
                            'Ae. tauschii (BW_01011)',
                            'Ae. tauschii (BW_01014)',
                            'Ae. tauschii (BW_01022)',
                            'Ae. tauschii (BW_01024)',
                            'Ae. tauschii (BW_01026)',
                            'Ae. tauschii (BW_01028)',
                            'Ae. tauschii (ENT336)',
                            'Ae. triaristata 70',
                            'Ae. triaristata 72',
                            'Ae. triaristata 73',
                            'Ae. triaristata 95',
                            'Ae. triuncialis 75',
                            'Ae. triuncialis 77',
                            'Ae. umbellulata 74',
                            'Ae. umbellulata 79',
                            'Ae. uniaristata 42',
                            'Ae. uniaristata 47',
                            'Ae. variabilis 44',
                            'Ae. variabilis 46',
                            'Ae. vavilovii 48',
                            'Ae. vavilovii 49',
                            'Ae. ventricosa 51',
                            'Ae. ventricosa 53',
                            'Ae. ventricosa 55',
                            'Ae. ventricosa (10x_nuq)',
                            'Ae. ventricosa (2067)',
                            'Ae. ventricosa (2181)',
                            'Ae. ventricosa (2181)',
                            'Ae. ventricosa (2210)',
                            'Ae. ventricosa (2211)',
                            'Ae. ventricosa (2234)'
                            'S. anatolicum 64',
                            'S. cereale 11',
                            'S. cereale 37',                            
                            'S. cereale (Lo7_nuq)',
                            'S. iranicum 62',
                            'S. segetale 65',
                            'S. strictum 67',
                            'S. vavilovii 69',
                            'T. dicoccoides 12',
                            'T. dicoccoides 76',
                            'T. dicoccoides 83',
                            'T. dicoccoides 90',
                            'T. dicoccoides 94',
                            'T. dicoccoides 97',                            
                            'T. dicoccoides (10x_nuq)',
                            'T. dicoccum 84',
                            'T. durum 81',
                            'T. durum 85',
                            'T. durum 92',
                            'T. durum 93',
                            'T. durum (Svevo 10x_nuq)',
                            'T. ispahanicum 87',
                            'T. macha 86',
                            'T. monococcum 13',
                            'T. monococcum 14',
                            'T. monococcum 15',
                            'T. monococcum 16',
                            'T. monococcum 43',
                            'T. monococcum 45',
                            'T. monococcum 66',
                            'T. monococcum 71',
                            'T. monococcum 89',
                            'T. polonicum 91',
                            'T. sphaerococcum 88',
                            'T. timopheevii 6',
                            'T. timopheevii 8',
                            'T. timopheevii 9',
                            'T. timopheevii (10558)',
                            'T. timopheevii (10827)',
                            'T. timopheevii (10827_all)',
                            'T. timopheevii (14352)',
                            'T. timopheevii (15832)',
                            'T. timopheevii (17024)',
                            'T. timopheevii (22438)',
                            'T. timopheevii (33255)',
                            'T. timopheevii (3708)',
                            'T. turanicum 82',
                            'T. urartu 17',
                            'T. urartu 19',
                            'T. urartu (10x_nuq)',
                            'Th. bessarabicum 78',
                            'Th. bessarabicum 80',
                            'Th. elongatum 18',
                            'Th. elongatum 23',
                            'Th. elongatum (10x_nuq)',
                            'Th. intermedium 1',
                            'Th. intermedium 10',
                            'Th. junceum 3',
                            'Th. ponticum 5',
                            'Th. ponticum 7',
                            'Th. ponticum (G37_nuq)',
                            'Th. ponticum (G38_nuq)',
                            'Th. ponticum (G39_nuq)',
                            'Th. turcicum 2'
                           ]

        alienGenome1 = st.selectbox(
            'Select first alien species ...',
            alienGenomeList,
            index=29,
            key='alien1'
        )

        alienGenome2 = st.selectbox(
            'Select second alien species ...',
            alienGenomeList,
            index=23,
            key='alien2'
        )

        alien = {
            "Th. intermedium 1": 1,
            "Th. turcicum 2": 2,
            "Th. junceum 3": 3,
            "Ae. biuncialis 4": 4,
            "Th. ponticum 5": 5,
            "T. timopheevii 6": 6,
            "Th. ponticum 7": 7,
            "T. timopheevii 8": 8,
            "T. timopheevii 9": 9,
            "Th. intermedium 10": 10,
            "S. cereale 11": 11,
            "T. dicoccoides 12": 12,
            "T. monococcum 13": 13,
            "T. monococcum 14": 14,
            "T. monococcum 15": 15,
            "T. monococcum 16": 16,
            "T. urartu 17": 17,
            "Th. elongatum 18": 18,
            "T. urartu 19": 19,
            "Ae. crassa 20": 20,
            "Ae. searsii 21": 21,
            "Ae. crassa 22": 22,
            "Th. elongatum 23": 23,
            "Ae. cylindrica 24": 24,
            "Ae. cylindrica 25": 25,
            "Ae. kotschyii 26": 26,
            "Ae. juvenalis 27": 27,
            "Ae. longissima 28": 28,
            "Ae. juvenalis 29": 29,
            "Ae. longissima 30": 30,
            "Ae. kotschyii 31": 31,
            "Ae. bicornis 32": 32, 
            "Ae. bicornis 33": 33,
            "Ae. caudata 34": 34,
            "Ae. biuncialis 35": 35,
            "Ae. biuncialis": 36,
            "S. cereale 37": 37,
            "Ae. columnaris 38": 38,
            "Ae. caudata 39": 39,
            "Ae. comosa 40": 40,
            "Ae. comosa 41": 41,
            "Ae. uniaristata 42": 42,
            "T. monococcum 43": 43,
            "Ae. variabilis 44": 44,
            "T. monococcum 45": 45,
            "Ae. variabilis 46": 46,
            "Ae. uniaristata 47": 47,
            "Ae. vavilovii 48": 48,
            "Ae. vavilovii 49": 49,
            "Ae. tauschii 50": 50,
            "Ae. ventricosa 51": 51,
            "Ae. mutica 52": 52,
            "Ae. ventricosa 53": 53,
            "Ae. mutica 54": 54,
            "Ae. ventricosa 55": 55,
            "Ae. ovata 56": 56,
            "Ae. ovata 57": 57,
            "Ae. speltoides 58": 58,
            "Ae. searsii 59": 59,
            "Ae. speltoides 60": 60,
            "Ae. sharonensis 61": 61,
            "S. iranicum 62": 62,
            "Ae. sharonensis 63": 63,
            "S. anatolicum 64": 64,
            "S. segetale 65": 65,
            "T. monococcum 66": 66,
            "S. strictum 67": 67,
            "Ae. tauschii 68": 68,
            "S. vavilovii 69": 69,
            "Ae. triaristata 70": 70,
            "T. monococcum 71": 71,
            "Ae. triaristata 72": 72,
            "Ae. triaristata 73": 73,
            "Ae. umbellulata 74": 74,
            "Ae. triuncialis 75": 75,
            "T. dicoccoides 76": 76,
            "Ae. triuncialis 77": 77,
            "Th. bessarabicum 78": 78,
            "Ae. umbellulata 79": 79,
            "Th. bessarabicum 80": 80,
            "T. durum 81": 81,
            "T. turanicum 82": 82,
            "T. dicoccoides 83": 83,
            "T. dicoccum 84": 84,
            "T. durum 85": 85,
            "T. macha 86": 86,
            "T. ispahanicum 87": 87,
            "T. sphaerococcum 88": 88,
            "T. monococcum 89": 89,
            "T. dicoccoides 90": 90,
            "T. polonicum 91": 91,
            "T. durum 92": 92,
            "T. durum 93": 93,
            "T. dicoccoides 94": 94,
            "Ae. triaristata 95": 95,
            "T. carthlicum 96": 96,
            "T. dicoccoides 97": 97,
            'ENT336': 'Ae. tauschii (ENT336)',
            'Ae. tauschii (BW_01011)':'BW_01011', 
            'Ae. tauschii (BW_01022)':'BW_01022', 
            'Ae. tauschii (BW_01014)':'BW_01014', 
            'Ae. tauschii (BW_01024)':'BW_01024', 
            'Ae. tauschii (BW_01026)':'BW_01026', 
            'Ae. tauschii (BW_01028)':'BW_01028', 
            'T. dicoccoides (10x_nuq)':'dicoccoides-10x_nuq', 
            'Th. elongatum (10x_nuq)':'elongathum-10x_nuq', 
            'S. cereale':'Lo7_nuq', 
            'Th. ponticum (37_nuq)':'ponticumG37_nuq', 
            'Th. ponticum (38_nuq)':'ponticumG38_nuq', 
            'Th. ponticum (39_nuq)':'ponticumG39-10x_nuq', 
            'Ae. speltoides (10x_nuq)':'speltoides-10x_nuq', 
            'T. durum (Svevo 10x_nuq)':'svevo-10x_nuq', 
            'T. timopheevii (10827)':'timopheevi10827-10x_nuq', 
            'T. timopheevii (33255)':'timopheevi33255-10x_nuq', 
            'T. timopheevii (10558)':'timopheevii10558_nuq.jf', 
            'T. timopheevii (10827_all)':'timopheevii10827-10x-all_all', 
            'T. timopheevii (14352)':'timopheevii14352_nuq.jf', 
            'T. timopheevii (15832)':'timopheevii15832_nuq.jf', 
            'T. timopheevii (17024)':'timopheevii17024-10x_all', 
            'T. timopheevii (22438)':'timopheevii22438_nuq.jf', 
            'T. timopheevii (3708)':'timopheevii3708_nuq.jf', 
            'T. urartu (10x_nuq)':'urartu-10x_nuq', 
            'Ae. ventricosa':'ventricosa-10x_nuq', 
            'Ae. ventricosa (2067)':'ventricosa2067-10x_nuq', 
            'Ae. ventricosa (2181)':'ventricosa2181', 
            'Ae. ventricosa (2181 10x)':'ventricosa2181-10x_nuq',
            'Ae. ventricosa (2210)':'ventricosa2210-10x_all',
            'Ae. ventricosa (2211)':'ventricosa2211-10x_nuq', 
            'Ae. ventricosa (2234)': 'ventricosa2234-10x_all'
        }

        # df.rename(columns={'timopheevii10558_nuq.jf': 'timopheevii10558_nuq_jf',
        #                    'timopheevii14352_nuq.jf': 'timopheevii14352_nuq_jf',
        #                    'timopheevii15832_nuq.jf': 'timopheevii15832_nuq_jf',
        #                    'timopheevii22438_nuq.jf': 'timopheevii22438_nuq_jf',
        #                    'timopheevii3708_nuq.jf': 'timopheevii3708_nuq_jf'},
        #                      inplace=True)
        chrm = st.selectbox(
            label='Select chromosome:',
            options=('1A', '2A', '3A', '4A', '5A', '6A', '7A',
                     '1B', '2B', '3B', '4B', '5B', '6B', '7B',
                     '1D', '2D', '3D', '4D', '5D', '6D', '7D'),
            index=8,
            key='chrm')

        submit = st.form_submit_button('Submit')


with st.container():

    st.markdown('<h1 class="font1">Introgression Viewer</h1>',
                unsafe_allow_html=True)

    st.markdown("""
                       
                ---
                    
                """)

    st.markdown("""
                
            To begin exploring potential introgressions, using the dropdown
            menus below, select a reference genome, query genomes (only two
            allowed), and the chromosome you wish to view.

                
            Please note:
                    
            1. Plots and tables can be expanded by clicking on the arrows to their top right.  Hover over the relevant plot or table to see the arrows.
            2. Plots can be downloaded as png or svg format files by clicking on the ellipsis (...) that appears to their top right once you hover over it.
            3. All plots are orientated such that chromosome short arms are on the left.
                
                
            The default plots, below, show the known introgression from *Triticum timopheevii*
            into chromosome 2B of the elite cultivar Lancer (Walkowiak *et al*.
            2020; Keilwagen *et al*., 2022).  This example has been chosen as it
            most clearly illustrates the presence of an introgression.  In the upper
            of the two line plots (*T. timopheevii* hybridised to the reference 
            genome Lancer) the low scores from bin 2,000 to bin 13,000 correspond
            with the known introgression.  By contrast, the plot of *T. dicoccoides* hybridised
            to Lancer shows few or no regions of similarity between the query and the reference genomes.
                
            You may wish to visualise other reported introgressions such as the *Ae. ventricosa*
            introgression on 2AS in the reference genomes Jagger, Mace, SY Mattis and Stanley.


            """)

    with st.expander("Cited articles"):
        st.markdown("""
                                                        
                    - 'Walkowiak *et al*. (2020) *Multiple wheat genomes reveal global variation in modern breeding*, **Nature** 588: 277 - 283'
                    - 'Keilwagen *et al*. (2022).  *Detecting major introgressions in wheat and their putative origins using coverage analysis*', **Scientific Reports** 12, 1908
                    - 'Gill, B.S. (2015). *Wheat Chromosome Analysis* In: Ogihara, Y., Takumi, S., Handa, H. (eds) Advances in Wheat Genetics: From Genome to Field. Springer, Tokyo. https://doi.org/10.1007/978-4-431-55675-6_7

                    
                    """
                    )

    st.markdown("""
                
                ---
                
                """
                )

    chromosome = 'chr' + chrm
    # chromosome = 'chr' + st.session_state['chrm'] + refFiles[st.session_state['ref']][1]

col1, col2 = st.columns([3, 2], gap='small')

with col1:

    chromosome = 'chr' + chrm
    # chromosome = 'chr' + st.session_state['chrm'] + refFiles[st.session_state['ref']][1]

    dfChr = df[df['seqname'] == chromosome]

    # Adjust the bin number so that it begins at zero (1) for each chromosome.
    dfChr = change_index(dfChr)

    var1 = alien[alienGenome1]
    var2 = alien[alienGenome2]
    var1 = str(var1)
    var2 = str(var2)

    st.markdown('<p class="font2">Line Plots of Hybridisation Scores</p>',
                unsafe_allow_html=True)

    # st.write(dfChr.head(10))
    
    figTitle = alienGenome1 + ' vs ' + alienGenome2

    fig = px.line(dfChr,
                  x='Adjusted Bin',
                  y=[var1, var2], color_discrete_map={var1: '#1F77B4', var2: '#FF7F0E'},
                  log_y = True,
                  title = figTitle
                 )
    fig.update_layout(showlegend=False)
    fig.update_traces(opacity=0.5)
    st.plotly_chart(fig, use_container_width=True)

 #   chart1_data = dfChr
 #   a = alt.Chart(chart1_data, title=figTitle).mark_line(color='#1F77B4').encode(
 #       x='Adjusted Bin',
 #       y=alt.Y(
 #           var1,
 #           scale=alt.Scale(type="log")
 #           ),
 #       tooltip=['Adjusted Bin', var1])

 #   chart1_data = dfChr
 #   b = alt.Chart(chart1_data).mark_line(opacity=0.5, color='#FF7F0E').encode(
 #       x='Adjusted Bin',
 #       y=alt.Y(
 #           var2,
 #           scale=alt.Scale(type="log")
 #           ),
 #       tooltip=['Adjusted Bin', var2])

 #   c = alt.layer(a, b)

 #   st.altair_chart(c, use_container_width=True)

    with st.expander(f'Chromosome {chrm} diagram'):

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

        legend1_text = 'Schematic representation of chromosome ' + chrm + ': image length (scale bar) is based on the mean number of 50 Kb bins spanning chromosome ' + chrm + \
            ' in the 11 reference genomes; morphology is based on Gill (2015).  The scale bar is in bin numbers and relates directy to the underlying plots; one can convert length to Mb by multiplying bin number by 50,000.'

        legend1_text_6A = '  Please note, Spelt chromosome ' + chrm + \
            ' is smaller (11,670 bins) than that of the other reference varieties'
        legend1_text_2B = '  Please note, Lancer chromosome ' + chrm + \
            ' is smaller (13,432 bins) than that of the other reference varieties'
        legend1_text_3B = '  Please note, Arina chromosome ' + chrm + \
            ' is larger (17,817 bins) than that of the other reference varieties'
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

        st.image('./images/' + chrm_scale[chrm], caption=legend1_text)


with col2:

    st.markdown('<p class="font2">Density Distribution of Scores</p>',
                unsafe_allow_html=True)

    x1 = dfChr[var1]
    x2 = dfChr[var2]

    # Group data
    hist_data = [x1, x2]

    group_labels = [alienGenome1, alienGenome2]

    # Create distplot with custom bin_size
    fig = ff.create_distplot(
        hist_data, group_labels)

    # Plot the density distribution chart
    st.plotly_chart(fig, use_container_width=True)

dfChr.set_index('Adjusted Bin', inplace=True)
dfChr.drop(columns=['Bin', 'seqname'], inplace=True)
dfChr.rename(columns={
            "1": "Th. intermedium 1",
            "2": "Th. turcicum 2",
            "3": "Th. junceum 3",
            "4": "Ae. biuncialis 4",
            "5": "Th. ponticum 5",
            "6": "T. timopheevii 6",
            "7": "Th. ponticum 7",
            "8": "T. timopheevii 8",
            "9": "T. timopheevii 9",
            "10": "Th. intermedium 10",
            "11": "S. cereale 11",
            "12": "T. dicoccoides 12",
            "13": "T. monococcum 13",
            "14": "T. monococcum 14",
            "15": "T. monococcum 15",
            "16": "T. monococcum 16",
            "17": "T. urartu 17",
            "18": "Th. elongatum 18",
            "19": "T. urartu 19",
            "20": "Ae. crassa 20",
            "21": "Ae. searsii 21",
            "22": "Ae. crassa 22",
            "23": "Th. elongatum 23",
            "24": "Ae. cylindrica 24",
            "25": "Ae. cylindrica 25",
            "26": "Ae. kotschyii 26",
            "27": "Ae. juvenalis 27",
            "28": "Ae. longissima 28",
            "29": "Ae. juvenalis 29",
            "30": "Ae. longissima 30",
            "31": "Ae. kotschyii 31",
            "32": "Ae. bicornis 32", 
            "33": "Ae. bicornis 33",
            "34": "Ae. caudata 34",
            "35": "Ae. biuncialis 35",
            "36": "Ae. biuncialis 36",            
            "37": "S. cereale 37",
            "38": "Ae. columnaris 38",
            "39": "Ae. caudata 39",
            "40": "Ae. comosa 40",
            "41": "Ae. comosa 41",
            "42": "Ae. uniaristata 42",
            "43": "T. monococcum 43",
            "44": "Ae. variabilis 44",
            "45": "T. monococcum 45",
            "46": "Ae. variabilis 46",
            "47": "Ae. uniaristata 47",
            "48": "Ae. vavilovii 48",
            "49": "Ae. vavilovii 49",
            "50": "Ae. tauschii 50",
            "51": "Ae. ventricosa 51",
            "52": "Ae. mutica 52",
            "53": "Ae. ventricosa 53",
            "54": "Ae. mutica 54",
            "55": "Ae. ventricosa 55",
            "56": "Ae. ovata 56",
            "57": "Ae. ovata 57",
            "58": "Ae. speltoides 58",
            "59": "Ae. searsii 59",
            "60": "Ae. speltoides 60",
            "61": "Ae. sharonensis 61",
            "62": "S. iranicum 62",
            "63": "Ae. sharonensis 63",
            "64": "S. anatolicum 64",
            "65": "S. segetale 65",
            "66": "T. monococcum 66",
            "67": "S. strictum 67",
            "68": "Ae. tauschii 68",
            "69": "S. vavilovii 69",
            "70": "Ae. triaristata 70",
            "71": "T. monococcum 71",
            "72": "Ae. triaristata 72",
            "73": "Ae. triaristata 73",
            "74": "Ae. umbellulata 74",
            "75": "Ae. triuncialis 75",
            "76": "T. dicoccoides 76",
            "77": "Ae. triuncialis 77",
            "78": "Th. bessarabicum 78",
            "79": "Ae. umbellulata 79",
            "80": "Th. bessarabicum 80",
            "81": "T. durum 81",
            "82": "T. turanicum 82",
            "83": "T. dicoccoides 83",
            "84": "T. dicoccum 84",
            "85": "T. durum 85",
            "86": "T. macha 86",
            "87": "T. ispahanicum 87",
            "88": "T. spaerococcum 88",
            "89": "T. monococcum 89",
            "90": "T. dicoccoides 90",
            "91": "T. polonicum 91",
            "92": "T. durum 92",
            "93": "T. durum 93",
            "94": "T. dicoccoides 94",
            "95": "Ae. triaristata 95",
            "96": "T. carthlicum 96",
            "97": "T. dicoccoides 97",
            'ENT336': 'Ae. tauschii (ENT336)',
            'BW_01011': 'Ae. tauschii (BW_01011)', 
            'BW_01022': 'Ae. tauschii (BW_01022)', 
            'BW_01014': 'Ae. tauschii (BW_01014)', 
            'BW_01024': 'Ae. tauschii (BW_01024)', 
            'BW_01026': 'Ae. tauschii (BW_01026)', 
            'BW_01028': 'Ae. tauschii (BW_01028)', 
            'dicoccoides-10x_nuq': 'T. dicoccoides (10x_nuq)', 
            'elongathum-10x_nuq': 'Th. elongatum (10x_nuq)', 
            'Lo7_nuq': 'S. cereale', 
            'ponticumG37_nuq': 'Th. ponticum (37_nuq)', 
            'ponticumG38_nuq': 'Th. ponticum (38_nuq)', 
            'ponticumG39-10x_nuq': 'Th. ponticum (39_nuq)', 
            'speltoides-10x_nuq': 'Ae. speltoides (10x_nuq)', 
            'svevo-10x_nuq': 'T. durum (Svevo 10x_nuq)', 
            'timopheevi10827-10x_nuq': 'T. timopheevii (10827a)',
            'timopheevii10827-10x-all_all': 'T. timopheevii (10827b)',            
            'timopheevi33255-10x_nuq': 'T. timopheevii (33255)', 
            'timopheevii10558_nuq.jf':'T. timopheevii (10558)', 
            'T. timopheevii (10827_all)':'timopheevii10827-10x-all_all', 
            'timopheevii14352_nuq.jf': 'T. timopheevii (14352)', 
            'timopheevii15832_nuq.jf': 'T. timopheevii (15832)', 
            'timopheevii17024-10x_all': 'T. timopheevii (17024)', 
            'timopheevii22438_nuq.jf': 'T. timopheevii (22438)', 
            'timopheevii3708_nuq.jf': 'T. timopheevii (3708)', 
            'urartu-10x_nuq': 'T. urartu (10x_nuq)', 
            'ventricosa-10x_nuq': 'Ae. ventricosa', 
            'ventricosa2067-10x_nuq': 'Ae. ventricosa (2067)', 
            'ventricosa2181': 'Ae. ventricosa (2181)', 
            'ventricosa2181-10x_nuq': 'Ae. ventricosa (2181 10x)',
            'ventricosa2210-10x_all': 'Ae. ventricosa (2210)',
            'ventricosa2211-10x_nuq': 'Ae. ventricosa (2211)', 
            'ventricosa2234-10x_all': 'Ae. ventricosa (2234)'
        }, inplace=True)

dfChr = dfChr.sort_index(axis=1)

first_column = dfChr.pop('end')
dfChr.insert(0, 'end', first_column)
first_column = dfChr.pop('start')
dfChr.insert(0, 'start', first_column)

st.write(dfChr)

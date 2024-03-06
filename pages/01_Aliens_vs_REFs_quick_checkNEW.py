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
    
 
# Load the table from a csv file
dfWildSpeciesList = pd.read_csv('./data/wild_relatives_introduction.csv')


################################# FUNCTIONS ###################################


def getData(filePath):
    df = pd.read_csv(filePath, compression='gzip', header=0, sep=',')
     
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
        index=6,
        key='ref',
        )

# Define a dictionary in which the keys are the names of the reference genomes
# and the values are tuples containing [0] the path to the respective file and 
# [1] the sample prefix within the file. 
    refFiles = {'Arina': ['https://www.cerealsdb.uk.net/ibspyNEW/2024-02-26_arinaLrFor_wilds_50000.csv.gz', '_WhAri'],
                'Chinese Spring': ['https://www.cerealsdb.uk.net/ibspyNEW/2024-02-26_chinesespring_wilds_50000.csv.gz', ''],
                'Jagger': ['https://www.cerealsdb.uk.net/ibspyNEW/2024-02-26_jagger_wilds_50000.csv.gz', '_WhJag'],
                'Julius': ['https://www.cerealsdb.uk.net/ibspyNEW/2024-02-26_julius_wilds_50000.csv.gz', '_Whjul'],
                'Lancer': ['https://www.cerealsdb.uk.net/ibspyNEW/2024-02-26_lancer_wilds_50000.csv.gz', '_Whlan'], 
                'Landmark': ['https://www.cerealsdb.uk.net/ibspyNEW/2024-02-26_landmark_wilds_50000.csv.gz', '_WhLan'],
                'Mace': ['https://www.cerealsdb.uk.net/ibspyNEW/2024-02-26_mace_wilds_50000.csv.gz', '_Whmac'],
                'Norin61': ['https://www.cerealsdb.uk.net/ibspyNEW/2024-02-26_norin61_wilds_50000.csv.gz', '_WhNor'],
                'Spelt': ['https://www.cerealsdb.uk.net/ibspyNEW/2024-02-26_spelta.genome_wilds_50000.csv.gz', '_Whspe'],
                'Stanley': ['https://www.cerealsdb.uk.net/ibspyNEW/2024-02-26_stanley_wilds_50000.csv.gz', '_WhSta'],
                'Mattis': ['https://www.cerealsdb.uk.net/ibspyNEW/2024-02-26_symattis_wilds_50000.csv.gz', '_WhSYM']
                }


    st.write('')    
    score_threshold = st.number_input('Score threshold (integer from 10 - 200):', min_value=10, max_value=200, value=30, key=1)

filePath = refFiles[refGenome][0]

df = getData(filePath)
    
# df.rename(columns={'timopheevii10558_nuq.jf': 'timopheevii10558_nuq_jf',
#                    'timopheevii14352_nuq.jf': 'timopheevii14352_nuq_jf',
#                    'timopheevii15832_nuq.jf': 'timopheevii15832_nuq_jf',
#                    'timopheevii22438_nuq.jf': 'timopheevii22438_nuq_jf',
#                    'timopheevii3708_nuq.jf': 'timopheevii3708_nuq_jf'},
#                     inplace=True)
    

# Define a dictionary in which the keys are the alien species and the values are
# the names given to the samples in the dataframe; e.g., the alien species Aegilops tauschii
# is named ENT336 in the underlying dataframe.      
    
# alien = {'Ae. tauschii: BW_01011': 'BW_01011',
#          'Ae. tauschii: BW_01022': 'BW_01022',      
#          'Ae. tauschii: BW_01024': 'BW_01024',      
#          'Ae. tauschii: BW_01026': 'BW_01026',      
#          'Ae. tauschii: BW_01014': 'BW_01014',
#          'Ae. tauschii: BW_01028': 'BW_01028',        
#          'Ae. tauschii: ENT336': 'ENT336',
#          'Ae. speltoides: speltoides-10x_nuq': 'speltoides-10x_nuq',
#          'Ae. ventricosa: ventricosa-10x_nuq': 'ventricosa-10x_nuq',
#          'Ae. ventricosa: ventricosa2067-10x_nuq': 'ventricosa2067-10x_nuq',   
#          'Ae. ventricosa: ventricosa2181': 'ventricosa2181', 
#          'Ae. ventricosa: ventricosa2181-10x_nuq': 'ventricosa2181-10x_nuq',      
#          'Ae. ventricosa: ventricosa2210-10x_all': 'ventricosa2210-10x_all',      
#          'Ae. ventricosa: ventricosa2211-10x_nuq': 'ventricosa2211-10x_nuq',
#          'Ae. ventricosa: ventricosa2234-10x_all': 'ventricosa2234-10x_all',     
#          'Secale cereale: Lo7_nuq': 'Lo7_nuq',
#          'Th. elongatum: elongathum-10x_nuq': 'elongathum-10x_nuq',
#          'Th. ponticum: ponticumG37_nuq': 'ponticumG37_nuq',
#          'Th. ponticum: ponticumG38_nuq': 'ponticumG38_nuq',     
#          'Th. ponticum: ponticumG39-10x_nuq': 'ponticumG39-10x_nuq',
#          'T. timopheevii: timopheevi33255-10x_nuq': 'timopheevi33255-10x_nuq',
#          'T. timopheevii: timopheevii10558_nuq.jf': 'timopheevii10558_nuq_jf',
#          'T. timopheevii: timopheevi10827-10x_nuq':  'timopheevi10827-10x_nuq',    
#          'T. timopheevii: timopheevii10827-10x-all_all': 'timopheevii10827-10x-all_all',     
#          'T. timopheevii: timopheevii14352_nuq.jf': 'timopheevii14352_nuq_jf',     
#          'T. timopheevii: timopheevii15832_nuq.jf': 'timopheevii15832_nuq_jf',
#          'T. timopheevii: timopheevii17024-10x_all': 'timopheevii17024-10x_all',
#          'T. timopheevii: timopheevii22438_nuq.jf': 'timopheevii22438_nuq_jf',
#          'T. timopheevii: timopheevii3708_nuq.jf': 'timopheevii3708_nuq_jf',     
#          'T. turgidum ssp. dicoccoides: dicoccoides-10x_nuq': 'dicoccoides-10x_nuq',
#          'T. turgidum ssp. durum: svevo-10x_nuq': 'svevo-10x_nuq',
#          'T. urartu: urartu-10x_nuq': 'urartu-10x_nuq'
#          }

alien = {
        "Th. intermedium 1": 1,
        "Th. turcicum 2": 2,
        "Th. junceum 3": 3,
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
        "Ae. juvenalis 29": 29,
        "Ae. longissima 30": 30,
        "Ae. kotschyii 31": 31,
        "S. cereale 37": 37,
        "Ae. columnaris 38": 38,
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
        "T. spaerococcum 88": 88,
        "T. monococcum 89": 89,
        "T. dicoccoides 90": 90,
        "T. polonicum 91": 91,
        "T. durum 92": 92,
        "T. durum 93": 93,
        "T. dicoccoides 94": 94,
        "Ae. triaristata 95": 95,
        "T. dicoccoides 97": 97
        }

st.markdown("""
                
            ---
                
            """)
            
st.markdown(f'#### Reference genome: {refGenome}')
st.write(f'##### Threshold similarity for inclusion: {score_threshold}')
st.write('Click on column header to sort by that column.')


chrm = ['1A', '2A', '3A', '4A', '5A', '6A', '7A',
      '1B', '2B', '3B', '4B', '5B', '6B', '7B',
      '1D', '2D', '3D', '4D', '5D', '6D', '7D']

binsBelow = (f'BinsBelow{score_threshold}')   
dfNew = pd.DataFrame(columns = ['Variety', 'Chromosome', 'ChromosomeLength', binsBelow, 'Percent'])            

for j in chrm:
    
    chromosome = 'chr' + j

    dfChr = df[df['seqname'] == chromosome]

    my_list = []
    for i in alien:

        if len(dfChr[dfChr[str(alien[i])] <= score_threshold]) > (len(dfChr) * 0.01):
            my_list.append(i)
            my_list.append(j)            
            my_list.append(len(dfChr))
            my_list.append(len(dfChr[dfChr[str(alien[i])] <= score_threshold]))          
            my_list.append(float(f'{((len(dfChr[dfChr[str(alien[i])] <= score_threshold]) / len(dfChr)) * 100):.2f}'))
               
            dfNew.loc[len(dfNew)] = my_list
            my_list = []

#st.write(dfNew.query("Percent".max())["Variety"])
# st.write(dfNew['Percent'].max())
 

col1, col2 = st.columns([2, 3], gap='medium')

with col1:  
    dfNew.set_index('Chromosome', inplace=True)
    st.write(dfNew)

with col2:
    variable_output = 'The table shows the number of potential introgressions in the selected reference genome (in this case ' + refGenome + ') based on your chosen threshold for inclusion (in this case ' + str(score_threshold) + ').'


#    font_size = 18
    html_str = f"""
    <style>
    p.a
    </style>
    <p class="a">{variable_output}</p>
    """
    # st.write(dfNew[dfNew['Percent'] == dfNew['Percent'].max]['Variety'])
    

                # To be included in the table at minimum of 1% of the scores must 
                # fall below the threshold figure chosen.
                
                # On the basis of you choice, there are {len(dfNew)} potential
                # introgressions shown in the table.'
                # """
                # ) 

    st.markdown(html_str, unsafe_allow_html=True)
    st.markdown("""
                To be included in the table a minimum of 1% of scores across the
                chromosome must fall below the threshold figure chosen.
                """
                )
    st.write(f'On the basis of your choice, there are {len(dfNew)} potential introgression shown in the table.')
# variable_output = st.text_input("Enter some text", value="Streamlit is awesome")
# font_size = st.slider("Enter a font size", 1, 300, value=30)

# html_str = f"""
# <style>
# p.a {{
#   font: bold {font_size}px Courier;
# }}
# </style>
# <p class="a">{variable_output}</p>
# """

# st.markdown(html_str, unsafe_allow_html=True)


# numbersToNames = {
# 1: "Th. intermedium",
# 2: "Th. turcicum",
# 3: "Th. junceum",
# 5: "Th. ponticum",
# 6: "T. timopheevii",
# 7: "Th. ponticum",
# 8: "T. timopheevii",
# 9: "T. timopheevii",
# 10: "Th. intermedium",
# 11: "S. cereale",
# 12: "T. dicoccoides",
# 13: "T. monococcum",
# 14: "T. monococcum",
# 15: "T. monococcum",
# 16: "T. monococcum",
# 17: "T. urartu",
# 18: "Th. elongatum",
# 19: "T. urartu",
# 20: "Ae. crassa",
# 21: "Ae. searsii",
# 22: "Ae. crassa",
# 23: "Th. elongatum",
# 24: "Ae. cylindrica",
# 25: "Ae. cylindrica",
# 26: "Ae. kotschyii",
# 27: "Ae. juvenalis",
# 29: "Ae. juvenalis",
# 30: "Ae. longissima",
# 31: "Ae. kotschyii",
# 37: "S. cereale",
# 38: "Ae. columnaris",
# 40: "Ae. comosa",
# 41: "Ae. comosa",
# 42: "Ae. uniaristata",
# 43: "T. monococcum",
# 44: "Ae. variabilis",
# 45: "T. monococcum",
# 46: "Ae. variabilis",
# 47: "Ae. uniaristata",
# 48: "Ae. vavilovii",
# 49: "Ae. vavilovii",
# 50: "Ae. tauschii",
# 51: "Ae. ventricosa",
# 52: "Ae. mutica",
# 53: "Ae. ventricosa",
# 54: "Ae. mutica",
# 55: "Ae. ventricosa",
# 56: "Ae. ovata",
# 57: "Ae. ovata",
# 58: "Ae. speltoides",
# 59: "Ae. searsii",
# 60: "Ae. speltoides",
# 61: "Ae. sharonensis",
# 62: "S. iranicum",
# 63: "Ae. sharonensis",
# 64: "S. anatolicum",
# 65: "S. segetale",
# 66: "T. monococcum",
# 67: "S. strictum",
# 68: "Ae. tauschii",
# 69: "S. vavilovii",
# 70: "Ae. triaristata",
# 71: "T. monococcum",
# 72: "Ae. triaristata",
# 73: "Ae. triaristata",
# 74: "Ae. umbellulata",
# 75: "Ae. triuncialis",
# 76: "T. dicoccoides",
# 77: "Ae. triuncialis",
# 78: "Th. bessarabicum",
# 79: "Ae. umbellulata",
# 80: "Th. bessarabicum",
# 81: "T. durum",
# 82: "T. turanicum",
# 83: "T. dicoccoides",
# 84: "T. dicoccum",
# 85: "T. durum",
# 86: "T. macha",
# 87: "T. ispahanicum",
# 88: "T. spaerococcum",
# 89: "T. monococcum",
# 90: "T. dicoccoides",
# 91: "T. polonicum",
# 92: "T. durum",
# 93: "T. durum",
# 94: "T. dicoccoides",
# 95: "Ae. triaristata",
# 97: "T. dicoccoides"
# }

# for key, value in numbersToNames.items():
#     print(f'{value} {key}')
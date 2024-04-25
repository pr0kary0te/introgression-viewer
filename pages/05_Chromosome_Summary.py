# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:37:44 2023

@author: bzmow
"""

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.markdown(""" <style> .font1 {
    font-size: 45px; font-family: 'Copper Black'; color: #FF9633},
    .font2 {
    font-size: 30px; font-family: 'Copper Black'; color: #FF9633}
        }
    </style> """, unsafe_allow_html=True)

st.markdown(""" <style> .font2 {
    font-size: 30px; font-family: 'Copper Black'; color: #FF9633}
        }
    </style> """, unsafe_allow_html=True)

st.markdown(""" <style> .p { color: #FF0000} </style> """, unsafe_allow_html=True)

st.markdown('<h1 class="font1">Chromosome Lengths</h1>', unsafe_allow_html=True)
st.markdown('Chromosome lengths are based on the number of bins, each 50,000bp in length, that span them')
st.markdown('')

col1, col2, col3 = st.columns([3,1.2,0.8], gap='Large')

with col3:

    genome_or_group = st.radio(
        "Select view",
        ('A genome', 'B genome', 'D genome', 'Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5', 'Group 6', 'Group 7',),
        key = 1
        )
    bin_or_megabase = st.radio(
        "Select y-axis label",
         ('Bins', 'Megabases'),
         key = 2
         )

with col1:
    
    df_summary = pd.read_csv('./data/chromosome_bin_numbers.csv')
    
    # Calculate the mean for each row (axis=1) and add the values as a new
    # column to the dataframe.  Non-numeric columns (variety name column) will
    # be ignored.
    
    df_summary['Mean'] = df_summary.mean(axis=1, numeric_only=True)
        
    # Transpose the dataframe df_summary so that chromosome become the headers
    # and set the index to the first column.
    
    df_summaryT = df_summary.set_index('Chromosome').T
    df_summaryTMb = df_summaryT.loc[:,'chr1A':'chr7D'].apply(lambda x: x*50,000)

 
    if genome_or_group == 'A genome':
        df = df_summaryT.loc[:, 'chr1A':'chr7A']
        dfMb = df.apply(lambda x: x*50)
        title = "Chromosome Length: A Genome"
        image = "A_Genome.png"
        box_colour = ["#357FC2"]
        group = 'group A'
            
    elif genome_or_group == 'B genome':
        df = df_summaryT.loc[:, 'chr1B':'chr7B']
        dfMb = df.apply(lambda x: x*50,000) 
        title = "Chromosome Length: B Genome"
        image = "B_Genome.png"
        box_colour = ["#B5DE99"]
        group = 'group B'
            
    elif genome_or_group == 'D genome':
        df = df_summaryT.loc[:, 'chr1D':'chr7D']
        dfMb = df.apply(lambda x: x*50,000) 
        title = "Chromosome Length: D Genome"             
        image = "D_Genome.png"
        box_colour = ["#D9A60A"]
        group = 'group D'
            
    elif genome_or_group == 'Group 1':
        df = df_summaryT[['chr1A', 'chr1B', 'chr1D']]
        dfMb = df.apply(lambda x: x*50,000) 
        title = "Chromosome Length: Group 1"
        image = "group-1-chromosomes.png"
        box_colour = ["#357FC2", "#B5DE99", "#D9A60A"]
        group = 'group 1'
                
    elif genome_or_group == 'Group 2':
        df = df_summaryT[['chr2A', 'chr2B', 'chr2D']]
        dfMb = df.apply(lambda x: x*50,000) 
        title = "Chromosome Length: Group 2"
        image = "group-2-chromosomes.png"
        box_colour = ["#357FC2", "#B5DE99", "#D9A60A"]                   
        group = 'group 2'
            
    elif genome_or_group == 'Group 3':
        df = df_summaryT[['chr3A', 'chr3B', 'chr3D']]
        dfMb = df.apply(lambda x: x*50,000) 
        title = "Chromosome Length: Group 3"                             
        image = "group-3-chromosomes.png"
        box_colour = ["#357FC2", "#B5DE99", "#D9A60A"]
        group = 'group 3'
            
    elif genome_or_group == 'Group 4':
        df = df_summaryT[['chr4A', 'chr4B', 'chr4D']]
        dfMb = df.apply(lambda x: x*50,000) 
        title = "Chromosome Length: Group 4"                                 
        image = "group-4-chromosomes.png"
        box_colour = ["#357FC2", "#B5DE99", "#D9A60A"]
        group = 'group 4'
            
    elif genome_or_group == 'Group 5':
        df = df_summaryT[['chr5A', 'chr5B', 'chr5D']]
        dfMb = df.apply(lambda x: x*50,000) 
        title = "Chromosome Length: Group 5"                                     
        image = "group-5-chromosomes.png"
        box_colour = ["#357FC2", "#B5DE99", "#D9A60A"]
        group = 'group 5'
            
    elif genome_or_group == 'Group 6':
        df = df_summaryT[['chr6A', 'chr6B', 'chr6D']]
        dfMb = df.apply(lambda x: x*50,000) 
        title = "Chromosome Length: Group 6"                                         
        image = "group-6-chromosomes.png"
        box_colour = ["#357FC2", "#B5DE99", "#D9A60A"]
        group = 'group 6'
            
    elif genome_or_group == 'Group 7':
        df = df_summaryT[['chr7A', 'chr7B', 'chr7D']]
        dfMb = df.apply(lambda x: x*50,000) 
        title = "Chromosome Length: Group 7" 
        image = "group-7-chromosomes.png"
        box_colour = ["#357FC2", "#B5DE99", "#D9A60A"]
        group = 'group 7'
            
    fig, ax = plt.subplots(figsize=(10,5))

    
    if bin_or_megabase == 'Bins':
        sns.set_palette(box_colour)
        sns.boxplot(df, palette = box_colour)
        
    elif bin_or_megabase == 'Megabases':
        sns.set_palette(box_colour)
        sns.boxplot(dfMb, palette = box_colour) 

    ax.set_title(title)

    st.pyplot(fig)
        
    legend_a = {
        'group A': 'Box and whisker plots of chromosome length of the 11 reference genomes; there is very little variation between the reference genomes with respect to the A genome chromosome.',
        'group B': 'Box and whisker plots of chromosome length of the 11 reference genomes; there is very little variation between the reference genomes with respect to the B genome chromosome.',
        'group D': 'Box and whisker plots of chromosome length of the 11 reference genomes; there is very little variation between the reference genomes with respect to the D genome chromosome.',
        'group 1': 'Box and whisker plots of chromosome length of the 11 reference genomes; there is very little variation between the reference genomes with respect to each of the Group 1 chromosomes.',
        'group 2': 'Box and whisker plots of chromosome length of the 11 reference genomes; although, in general, there is very little variation between the reference genomes with respect to each of the Group 2 chromosomes, Lancer appears to have a relatively small chromosome 2B (outlier).',
        'group 3': 'Box and whisker plots of chromosome length of the 11 reference genomes; although, in general, there is very little variation between the reference genomes with respect to each of the Group 3 chromosomes, Arina appears to have a relatively large chromosome 3B (outlier), and Lancer a large chromosome 3D (outlier).',
        'group 4': 'Box and whisker plots of chromosome length of the 11 reference genomes; there is very little variation between the reference genomes with respect to each of the Group 4 chromosomes.',
        'group 5': 'Box and whisker plots of chromosome length of the 11 reference genomes; although, in general, there is very little variation between the reference genomes with respect to each of the Group 5 chromosomes, both Arina and SY Mattis appear to have a very small chromosome 5B (grey diamonds), and are probably carrying the 7BS/5BS translocation.',
        'group 6': 'Box and whisker plots of chromosome length of the 11 reference genomes; although, generally, there is very little variation between the reference genomes with respect to each of the Group 6 chromosome, Spelt has a relatively small chromosome 6A (outlier).',
        'group 7': 'Box and whisker plots of chromosome length of the 11 reference genomes; although, in general, there is very little variation between the reference genomes with respect to each of the Group 7 chromosomes, both Arina and SY Mattis appear to have a very large chromosome 7B (grey diamonds), and are probably carrying the 5BL/7BL translocation.'
        }
        
    st.write(legend_a[group])


with col2:

    legend_b = {
        'group A': 'Ideogram of A genome chromosomes (redrawn from  Gill (2015)) with relative chromosome lengths based on mean number of 50 kb bins spanning the chromosome in the 11 reference genomes.',
        'group B': 'Ideogram of B genome chromosomes (redrawn from  Gill (2015)) with relative chromosome lengths based on mean number of 50 kb bins spanning the chromosome in the 11 reference genomes.',
        'group D': 'Ideogram of D genome chromosomes (redrawn from  Gill (2015)) with relative chromosome lengths based on mean number of 50 kb bins spanning the chromosome in the 11 reference genomes.',
        'group 1': 'Ideogram of group 1 chromosomes (redrawn from  Gill (2015)) with relative chromosome lengths based on mean number of 50 kb bins spanning the chromosome in the 11 reference genomes.',
        'group 2': 'Ideogram of group 2 chromosomes (redrawn from  Gill (2015)) with relative chromosome lengths based on mean number of 50 kb bins spanning the chromosome in the 11 reference genomes.',
        'group 3': 'Ideogram of group 3 chromosomes (redrawn from  Gill (2015)) with relative chromosome lengths based on mean number of 50 kb bins spanning the chromosome in the 11 reference genomes.',
        'group 4': 'Ideogram of group 4 chromosomes (redrawn from  Gill (2015)) with relative chromosome lengths based on mean number of 50 kb bins spanning the chromosome in the 11 reference genomes.',
        'group 5': 'Ideogram of group 5 chromosomes (redrawn from  Gill (2015)) with relative chromosome lengths based on mean number of 50 kb bins spanning the chromosome in the 11 reference genomes.',
        'group 6': 'Ideogram of group 6 chromosomes (redrawn from  Gill (2015)) with relative chromosome lengths based on mean number of 50 kb bins spanning the chromosome in the 11 reference genomes.',
        'group 7': 'Ideogram of of group 7 chromosomes (redrawn from  Gill (2015)) with relative chromosome lengths based mean number of 50 kb bins spanning the chromosome in the 11 reference genomes.',
        }

    st.image(f'./images/{image}', caption=legend_b[group])

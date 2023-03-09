# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:10:52 2023

@author: bzmow
"""

import pandas as pd
import streamlit as st

st.markdown(""" <style> .font1 {
    font-size: 45px; font-family: 'Copper Black'; color: #FF9633},
    .font2 {
    font-size: 30px; font-family: 'Copper Black'; color: #FF9633}
    </style> """, unsafe_allow_html=True)

    
st.markdown(""" <style> .font3 { color: #FF0000} </style> """, unsafe_allow_html=True)

st.markdown('<h2 class="font1">Elite Varieties in dataset</h2>', unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6 = st.columns(6, gap = 'small')


with col1:
    
    with st.expander('A'):
        
        st.markdown("""
                    
                    - ability
                    - Agron
                    - Alba
                    - Albatross
                    - Alcedo
                    - Alert
                    - Almus
                    - Altria
                    - arina-10x_nuq
                    - ArinaLrFor
                    - arina-pg [REF]
                    - Arminda
                    - Aronde
                    - Avalon
                    - avocet
                    - Aztec
                    
                    """
                    )
        
    with st.expander('G'):
        
        st.markdown("""
                    
                    - Gabo
                    - Galahad
                    - Galant
                    - Garcia
                    - Gawain
                    - Glasgow
                    - Grafton
                    - Granada
        
                    """
                    )
        
    with st.expander('M'):
        
        st.markdown("""
                    
                    - mace
                    - mace-10x_nuq
                    - mace2
                    - mace3
                    - mace-pg  [REF]
                    - Mahndorfer
                    - malacca
                    - Marco
                    - Maris_Dove
                    - Maris_Ranger (Maris_ranger)
                    - Maris_Widgeon
                    - Maris_Huntsman (MarisHuntsman)
                    - mattis-10x_nuq
                    - mattis-12x_nuq
                    - mattis2
                    - mattis3
                    - mattis-pg  [REF]
                    - mendel
                    - mercia
                    - mina
                    - Minister
                    - Mironovska
                    - MISR1
                    - Moisson
                    - Muck
                    - Multiweiss
      
                    """
                    )
        
    with st.expander('S'):   
        
        st.markdown("""
                    - Sacramento
                    - Saki
                    - Savannah
                    - Schweigers_Taca
                    - Scipion
                    - Shamrock
                    - Shango
                    - Sicco
                    - Siskin
                    - Skyfall
                    - Skyscraper
                    - Slejpner
                    - Soissons
                    - Soleil
                    - solstice
                    - Spark
                    - Sperber
                    - Spitfire
                    - Sportsman
                    - Stamm101
                    - stanley
                    - stanley-10x_nuq
                    - stanley-12x_nuq
                    - stanley2
                    - stanley3
                    - stanley-pg  [REF]
                    - Starke2
                    - Stava
                    - Stella
                    - Super152
                    - Svale
                    - SYMattis                   
        
                    """
                    )

with col2:
    
    with st.expander('B'):
        
        st.markdown("""
                    - Banco
                    - Bandit
                    - Banner
                    - Beauchamp
                    - Beaver
                    - Becard_Kachu
                    - Bersee
                    - blitz
                    - Boreonos
                    - borlaug-pg
                    - Bounty
                    - Boxer
                    - Buster
        
                    """
                    )
        
    with st.expander('H'):
        
        st.markdown("""
                    - Haven
                    - Heine7
                    - Hereward
                    - Highbury
                    - Hobbit
                    - Holdfast
                    - holster
                    - hope_kall
                    - Hybrid46
     
                    """
                    )
        
    with st.expander('N'):
        
        st.markdown("""

                    - Nautica
                    - Newhaven
                    - Norda
                    - Norin
                    - norin61-10x_nuq
                    - norin61-pg  [REF]
                    - Norman
     
                    """
                    )
        
    with st.expander('T'):
        
        st.markdown("""
                    - Tadorna
                    - Talent
                    - Tambor
                    - Tandem
                    - Tanker
                    - Taras
                    - Thatcher
                    - Thor
                    - Tibetan-10x_nuq
                    - Titus
                    - Top
                    - torch
                    - Torfrida
                    - Trafalgar
                    - Treasure
                    - Tremie
                    - Triumph_NDL
                    - Tschermaks
        
                    """
                    )

        
with col3:
    
    with st.expander('C'):
        
        st.markdown("""
                    - cadenza
                    - cadenza-10.4x_nuq
                    - cadenza-15x_nuq
                    - cadenza2
                    - Calif
                    - Camp_Remy
                    - Capitiane
                    - Capo
                    - Cappelle_Desprez
                    - Captor
                    - Catamaran
                    - Cezanne
                    - Charger
                    - Chinese_Spring
                    - chinese_Spring-10x_nuq
                    - chinese_Spring2
                    - chinese_Spring3
                    - chinese-pg [REF]
                    - Cimcog3
                    - Cimcog26
                    - cimcog32
                    - Cimcog47
                    - Cimcog49
                    - Cimcog53
                    - Cimcog56
                    - Claire
                    - claire
                    - claire-10x_nuq
                    - claire2
                    - claire3
                    - Consort
                    - Cordiale
                    - Courtot
                    - Crest
                    - Crusoe
                    """
                    )
        
    with st.expander('I'):
        
        st.markdown("""
                    - Ibis
                    - Iena
                    - Ikarus
                    """
                    )
        
    with st.expander('O'):
        
        st.markdown("""
                    - Obelisk
                    - Odeon
                    - Odin
                    - Oenus
                    - Opata
                    - Orlando
                    """
                    )
        
    with st.expander('U'):
        
        st.markdown("""
                    - Urban                    
                    """
                    )


with col4:
    
    with st.expander('D'):
        
        st.markdown("""
                    - david
                    - denver
                    - Diablo
                    - Diplomat
                    - Disponent
                    - Dorby
                    - Drake
                    - Drauhofener_Kolben
                    - Druid  
                    """
                    )
        
    with st.expander('J'):
        
        st.markdown("""
                    - jagger
                    - jagger-10x_nuq
                    - jagger-pg  [REF]
                    - Joss_Cambier
                    - Julius
                    - julius-10x_nuq
                    - julius-pg  [REF]
                    """
                    )
        
    with st.expander('P'):
        
        st.markdown("""
                    - Palur
                    - Pamyat
                    - paragon
                    - paragon-10x_nuq
                    - paragon-12x_nuq
                    - paragon2
                    - paragon3
                    - Pastiche
                    - Pavon76
                    - Pepital
                    - Peragis
                    - Perlo
                    - Pfau
                    - Piko
                    - Pomerelle
                    - Pony
                    - Prof_Marshall
                    - Prophet  
                    """
                    )
        
    with st.expander('V'):
        
        st.markdown("""
                    - Vaguedepis
                    - Veritas
                    - Vilmorin27
                    - Vilmorin53
                    - Virgo
                    - Vocal
                    - Voyage
                    """
                    )

with col5:
    
    with st.expander('E'):
        
        st.markdown("""
                    - eagle
                    - Encore
                    - Epson
                    - Equinox
                    - Ergo
                    - Erland
                    - Eros
                    - Etoile_de_Choisy
                    - Expert
                    - Extase
                    - Extrem
                    """
                    )
        
    with st.expander('K'):
        
        st.markdown("""
                    - Karat
                    - Koga1
                    - Kolben
                    - Kontrast
                    - Kosack
                    - Kranich
                    - KWS_Santiago
                    """
                    )
        
    with st.expander('Q'):
        
        st.markdown("""
                    
        THERE ARE NO VARIETIES IN THE DATABASE
        
        """
        )
        
    with st.expander('W'):
        
        st.markdown("""
                    - Walde
                    - Warrior
                    - wasp
                    - Waxwing
                    - weebil
                    - weebil-10x_nuq
                    - weebil2
                    - weebil3
                    - Werla
                    - Wizard
                    - Wolverine
                    - Wyalkatatchen
                    """
                    )
        

with col6:
    
    with st.expander('F'):
        
        st.markdown("""
                    - Fanal
                    - Felix
                    - festival
                    - fidel
                    - fielder
                    - fielder-10x_all
                    - fielder-10x_nuq
                    - fielder-5x_all
                    - fielder-5x_nuq
                    - fielder-7.5x_all
                    - fielder-7.5x_nuq
                    - Fiorello
                    - Flair
                    - Flame
                    - Flamingo
                    - Florida  
                    """
                    )
        
    with st.expander('L'):
        
        st.markdown("""
                    - Lancelot
                    - lancer
                    - lancer-10x_nuq
                    - lancer-pg  [REF]
                    - landmark
                    - landmark-10x_nuq
                    - landmark-12x_nuq
                    - landmark2
                    - landmark-pg  [REF]
                    - Leda
                    - Legend
                    - Longbow
                    - Lutin  
                    """
                    )
        
    with st.expander('R'):
        
        st.markdown("""
                    - Rabe
                    - Rebel
                    - Recital
                    - Record
                    - Red_Fife
                    - Reedling
                    - Reform
                    - Regent
                    - Renan
                    - Rendezvous
                    - Revelation
                    - Rialto
                    - Riband
                    - Rimpaus_Bastard2
                    - Rimpaus_Braun_known_as_Braun_Rimpau
                    - RitzlhoferNeu
                    - robigus
                    - robigus-10x_nuq
                    - robigus2
                    - robigus3
                    - Rubisko
                    """
                    )
        
    with st.expander('X, Y and Z'):
        
        st.markdown("""                
                    - Xi19

        - Zemon
        - Zentos  
            """
            )



# ## Wild Relatives

#     Ae. tauschii (listed under: ENT336)
    
#     Ae. ventricosa (listed under:
#                                     ventricosa-10x_nuq,
#                                     ventricosa2067-10x_nuq,
#                                     ventricosa2181,
#                                     ventricosa2210-10x_all,
#                                     ventricosa2211-10x_nuq,
#                                     ventricosa2234-10x_all)

#     S. cereale (listed under Lo7_nuq)

#     Th. elongatum (listed under elongatum-10x_nuq)

#     Th. ponticum (listed under:
#                                 ponticumG37_nuq,
#                                 ponticumG38_nuq,
#                                 ponticumG39-10x_nuq)  
    
#     T. dicoccoides (dicoccoides-10x_nuq)

#     T. spelta (listed under:
#                                 spelt,
#                                 spelt-10x_nuq,
#                                 spelt-pg  [REFERENCE GENOME])

#     T. speltoides (speltoides-10x_nuq)

#     T. timopheevii (listed under:
#                                 timopheevii3708_nuq.jf,
#                                 timopheevii10558_nuq.jf,
#                                 timopheevi10827-10x_nuq,
#                                 timopheevii10827-10x-all_all,
#                                 timopheevii15832_nuq.jf
    
#                                 timopheevi33255-10x_nuq
    
#                                 timopheevii14352_nuq.jf
#                                 timopheevii17024-10x_all,
#                                 timopheevii22438_nuq.jf)
                                
#               NB the T. timopheevii samples fall into three distinct groups, one of which appears identical to Ae. ventricosa; the groups are listed separately.

#     T. turgidum (listed under: svevo-10x_nuq)

#     T. urartu (listed under: urartu-10x_nuq))
    
#     """
#     )
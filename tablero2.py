import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

rf_picke= open('random_forest_penguins.pickle','rb')
map_piclke=open('output_penguins.pickle','rb')
rfc=pickle.load(rf_picke)
unique_penguin_mapping=pickle.load(map_piclke)
rf_picke.close()
map_piclke.close()


st.set_page_config(layout='centered', page_title='Talento tech ML', page_icon='aries')

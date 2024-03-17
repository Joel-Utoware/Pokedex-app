import streamlit as st
from streamlit.logger import get_logger
import numpy as np
import requests
import pandas as pd

LOGGER = get_logger(__name__)

def get_details(poke_number):
    ''' Create an entry for our favourite pokemon '''
    try:
        url = f'https://pokeapi.co/api/v2/pokemon/{poke_number}/'
        response = requests.get(url)
        pokemon = response.json()
        return pokemon['name'], pokemon['height'], pokemon['weight'], len(pokemon['moves'])
    except:
        return 'Error', np.NAN, np.NAN, np.NAN 
    

def run():
    st.set_page_config(
        page_title="Pokemon data",
        page_icon="🔴⚪",
    )
    st.title('Pokedex info')
    st.markdown('Enter in the pokedex number of the desired pokemon and relevant information will come up.')
    poke_number = st.text_input('Pokedex number', '1')
    pokedex = pd.DataFrame(columns = ['name', 'height', 'weight', 'move_count'])
    pokedex.loc[poke_number] = get_details(poke_number)
    st.dataframe(pokedex,use_container_width=True)

if __name__ == "__main__":
    run()

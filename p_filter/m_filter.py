import pandas as pd
import json

from p_scrapper.m_scrapper import recipes

# import preferences updates in a separate json file

with open('../practice.json') as f:
    preferences = json.load(f)

# filter recipes as per json preferences into 4 groups:

comidas_semana = recipes[(recipes.Categoria.isin(preferences['comidas_semana']['categoria']))
                         & (recipes.Tiempo.isin(preferences['comidas_semana']['tiempo']))]

cenas_semana = recipes[(recipes.Categoria.isin(preferences['cenas_semana']['categoria']))
                       & (recipes.Tiempo.isin(preferences['cenas_semana']['tiempo']))]

comidas_finde = recipes[(recipes.Categoria.isin(preferences['comidas_finde']['categoria']))
                        & (recipes.Tiempo.isin(preferences['comidas_finde']['tiempo']))]

cenas_finde = recipes[(recipes.Categoria.isin(preferences['cenas_finde']['categoria']))
                      & (recipes.Tiempo.isin(preferences['cenas_finde']['tiempo']))]





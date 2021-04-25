import pandas as pd
import numpy as np
import json
from dotenv import load_dotenv
load_dotenv()
import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

recipes = pd.read_csv('data_exports/recipes_csv').replace('NaN', np.nan).drop(['Unnamed: 0'], axis=1)

with open('practice.json') as f:
    preferences = json.load(f)

comidas_semana = recipes[(recipes.Categoria.isin(preferences['comidas_semana']['categoria']))
                         & (recipes.Tiempo.isin(preferences['comidas_semana']['tiempo']))]

cenas_semana = recipes[(recipes.Categoria.isin(preferences['cenas_semana']['categoria']))
                       & (recipes.Tiempo.isin(preferences['cenas_semana']['tiempo']))]

comidas_finde = recipes[(recipes.Categoria.isin(preferences['comidas_finde']['categoria']))
                        & (recipes.Tiempo.isin(preferences['comidas_finde']['tiempo']))]

cenas_finde = recipes[(recipes.Categoria.isin(preferences['cenas_finde']['categoria']))
                      & (recipes.Tiempo.isin(preferences['cenas_finde']['tiempo']))]


l_comida = comidas_semana.loc[np.random.choice(comidas_semana.index.values, 1)]
m_comida = comidas_semana.loc[np.random.choice(comidas_semana.index.values, 1)]
x_comida = comidas_semana.loc[np.random.choice(comidas_semana.index.values, 1)]
j_comida = comidas_semana.loc[np.random.choice(comidas_semana.index.values, 1)]
v_comida = comidas_semana.loc[np.random.choice(comidas_semana.index.values, 1)]

s_comida = comidas_finde.loc[np.random.choice(comidas_finde.index.values, 1)]
d_comida = comidas_finde.loc[np.random.choice(comidas_finde.index.values, 1)]

l_cena = cenas_semana.loc[np.random.choice(cenas_semana.index.values, 1)]
m_cena = cenas_semana.loc[np.random.choice(cenas_semana.index.values, 1)]
x_cena = cenas_semana.loc[np.random.choice(cenas_semana.index.values, 1)]
j_cena = cenas_semana.loc[np.random.choice(cenas_semana.index.values, 1)]
v_cena = cenas_semana.loc[np.random.choice(cenas_semana.index.values, 1)]

s_cena = cenas_finde.loc[np.random.choice(cenas_finde.index.values, 1)]
d_cena = cenas_finde.loc[np.random.choice(cenas_finde.index.values, 1)]

msg = MIMEMultipart('alternative')
msg['Subject'] = 'Meal plan'
msg['From'] = os.getenv('EMAIL')
msg['To'] = destination = os.getenv('DESTINATION')
pwd = os.getenv('PASSWORD')


text = f"""Hi! Here's your meal plan for this week:"""


html = f"""\
<html>
    <head></head>
    <body>
        <p>Hola!<br>
           Aqui tienes tu seleccion de recetas para esta semana:<br>
           <br>
           LUNES<br>
           - Comida: <a href='{l_comida.iloc[0,0]}'>{l_comida.iloc[0,1]}</a><br>
           - Cena: <a href='{l_cena.iloc[0,0]}'>{l_cena.iloc[0,1]}</a><br>
           <br>
           MARTES<br>
           - Comida: <a href='{m_comida.iloc[0,0]}'>{m_comida.iloc[0,1]}</a><br>
           - Cena: <a href='{m_cena.iloc[0,0]}'>{m_cena.iloc[0,1]}</a><br>
           <br>
           MIERCOLES<br>
           - Comida: <a href='{x_comida.iloc[0,0]}'>{x_comida.iloc[0,1]}</a><br>
           - Cena: <a href='{x_cena.iloc[0,0]}'>{x_cena.iloc[0,1]}</a><br>
           <br>
           JUEVES<br>
           - Comida: <a href='{j_comida.iloc[0,0]}'>{j_comida.iloc[0,1]}</a><br>
           - Cena: <a href='{j_cena.iloc[0,0]}'>{j_cena.iloc[0,1]}</a><br>
           <br>
           VIERNES<br>
           - Comida: <a href='{v_comida.iloc[0,0]}'>{v_comida.iloc[0,1]}</a><br>
           - Cena: <a href='{v_cena.iloc[0,0]}'>{v_cena.iloc[0,1]}</a><br>
           <br>
           SABADO<br>
           - Comida: <a href='{s_comida.iloc[0,0]}'>{s_comida.iloc[0,1]}</a><br>
           - Cena: <a href='{s_cena.iloc[0,0]}'>{s_cena.iloc[0,1]}</a><br>
           <br>
           DOMINGO<br>
           - Comida: <a href='{d_comida.iloc[0,0]}'>{d_comida.iloc[0,1]}</a><br>
           - Cena: <a href='{d_cena.iloc[0,0]}'>{d_cena.iloc[0,1]}</a><br>
           <br>
           <br>
           Necesitas estos ingredientes para tu plan:<br>
           <br>
           LUNES<br>
           - Comida ({l_comida.iloc[0,1]}):<br>
           {l_comida.iloc[0,8]}<br>
           - Cena ({l_cena.iloc[0,1]}):<br>
           {l_cena.iloc[0,8]}<br>
           <br>
           MARTES<br>
           - Comida ({m_comida.iloc[0,1]}):<br>
           {m_comida.iloc[0,8]}<br>
           - Cena ({m_cena.iloc[0,1]}):<br>
           {m_cena.iloc[0,8]}<br>
           <br>
           MIERCOLES<br>
           - Comida ({x_comida.iloc[0,1]}):<br>
           {x_comida.iloc[0,8]}<br>
           - Cena ({x_cena.iloc[0,1]}):<br>
           {x_cena.iloc[0,8]}<br>
           <br>
           JUEVES<br>
           - Comida ({j_comida.iloc[0,1]}):<br>
           {j_comida.iloc[0,8]}<br>
           - Cena ({j_cena.iloc[0,1]}):<br>
           {j_cena.iloc[0,8]}<br>
           <br>
           VIERNES<br>
           - Comida ({v_comida.iloc[0,1]}):<br>
           {v_comida.iloc[0,8]}<br>
           - Cena ({v_cena.iloc[0,1]}):<br>
           {v_cena.iloc[0,8]}<br>
           <br>
           SABADO<br>
           - Comida ({s_comida.iloc[0,1]}):<br>
           {s_comida.iloc[0,8]}<br>
           - Cena ({s_cena.iloc[0,1]}):<br>
           {s_cena.iloc[0,8]}<br>
           <br>
           DOMINGO<br>
           - Comida ({d_comida.iloc[0,1]}):<br>
           {d_comida.iloc[0,8]}<br>
           - Cena ({d_cena.iloc[0,1]}):<br>
           {d_cena.iloc[0,8]}<br>
        </p>
    </body>
</html>        

"""


part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

msg.attach(part1)
msg.attach(part2)

def send_email():
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(msg['From'], pwd)

        smtp.sendmail(msg['From'], msg['To'], msg.as_string())

send_email()
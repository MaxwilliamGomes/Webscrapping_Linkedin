#Importando as bibliotecas

import requests 
from bs4 import BeautifulSoup
import pandas as pd

oportunidade = input("Qual vaga voce deseja? ")

oportunidade_tratada = oportunidade.replace(" ", "%20").lower()

oportunidade_tratada

url =f'''
https://www.linkedin.com/jobs/search?
keywords={oportunidade}
&location=Brasil
&geoId=106057199
&f_TPR=r86400&position=1
&pageNum=0
'''

url = url.replace("\n", "")

response = requests.get(url)

print(response)

response.text

site = BeautifulSoup(response.text, "html.parser")

dados = site.find_all("div",attrs={"class" : "base-search-card__info"})

armazenando_vaga = []
armazenando_empresa = []
armazenando_localizacao = []
armazenando_tempo = []
armazenando_data = []

for palavra in dados:
 
 #Nome da vaga

 nome_vaga = palavra.find_all("h3")[0].text.strip()
 armazenando_vaga.append(nome_vaga)

 #Nome empresa

 nome_empresa = palavra.find_all("h4")[0].text.strip()
 armazenando_empresa.append(nome_empresa)

 #localização

 localizacao = palavra.find_all("span", attrs = {"class": "job-search-card__location"})[0].text.strip()
 armazenando_localizacao.append(localizacao)

 #Tempo disponibilidade da vaga

 tempo_vaga = palavra.find_all("time")[0].text.strip()
 armazenando_tempo.append(tempo_vaga)

 #data
 data = palavra.find_all("time")[0]
 data_trat = data["datetime"]
 armazenando_data.append(data_trat)

 base_vaga = {
"vaga" : armazenando_vaga,
"empresa" : armazenando_empresa,
"localizacao" : armazenando_localizacao,
"Tempo_postada" : armazenando_tempo,
"data_vaga" : armazenando_data
}
 
pd.DataFrame(base_vaga)

 

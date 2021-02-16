# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 18:15:54 2021

@author: vinic
"""

import pandas as pd

dados = pd.read_csv('diretorio do  arquivo CSV')

#dados = dados.rename(columns = {'Group ID': 'ID', 'Filename': 'Filename', 'Folder': 'Folder', 'Size (KB)': 'Size', 'Dimensions': 'Dimensions', 'Match %': 'Match'})

grupo = dados.iloc[:, 0].values
fotos = dados.iloc[:, 1].values

path = dados.iloc[0, 2]

# Pegar Linhas específicas
'''import pandas as pd
base = pd.read_csv('iris.csv')
previsores = base.iloc[:, 0:4].values
classe = base.iloc[:, 4].values'''

# Apagar linhas do dataframe
'''base = pd.read_csv('autos.csv', encoding='ISO-8859-1')  
base = base.drop('dateCrawled', axis = 1)
base = base.drop('dateCreated', axis = 1)'''


import os

pos = 1
arq = '.jpg'

l = os.listdir(path)

# exemplo alterado de  EX_10.5.py para 10_5.py
for nome in range(len(fotos)):
    reinicio = grupo[nome]
    
    if nome > 0:
        if reinicio == reinicio_compara:
            pass
        else:
            pos = 1
    
    # alterar conforme sua necessidade de geração de nomes e layout de arquivos
    novo_nome = str(grupo[nome]) + ' - ' + str(pos) +  arq

    
    try:
            os.rename(path + '/' + fotos[nome], path + '/' + novo_nome )
            pos += 1
    except:
        while novo_nome in l:
            indice = l.index(novo_nome)
            l.pop(indice)
            
            pos += 1
            novo_nome = str(grupo[nome]) + ' - ' + str(pos) +  arq

        os.rename(path + '/' + fotos[nome], path + '/' + novo_nome )
        
    reinicio_compara = grupo[nome]







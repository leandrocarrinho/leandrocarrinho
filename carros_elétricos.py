# -*- coding: utf-8 -*-
"""Carros Elétricos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1omNB2IMuDRmba84f9TU-3TYHZoJZCDpr

Este é um estudo sobre a fonte de dados disponível no Kaggle referente a análise de dados sobre os carros elétricos

###Importando das Bibliotecas
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

from sklearn.preprocessing import OneHotEncoder, LabelEncoder, label_binarize
from sklearn.model_selection import train_test_split
from sklearn import model_selection, tree, preprocessing, metrics, linear_model
from sklearn.svm import LinearSVC
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LinearRegression, LogisticRegression, SGDClassifier
from sklearn.tree import DecisionTreeClassifier
!pip install catboost
import catboost
from catboost import CatBoostClassifier, Pool, cv

from sklearn.model_selection import GridSearchCV

"""###Buscando o Arquivo de Dados"""

dados = pd.read_csv('estacao.csv')

"""###Analisando os dados"""

dados

dados.info()

dados.isnull().sum()

dados.describe()

"""###Tratar Nulos de Distancia"""

distance_mean = dados['distance'].mean()

dados_df = pd.DataFrame(dados)

dados_df

def dados_func(data, column, count = True):
  print(f'Quantidade de valores unicos: {data[column].nunique()}')
  print(f'\nQuais são os valores unicos: {data[column].unique()}')
  print(f'\nQuantidade de valores nulos: {data[column].isnull().sum()}')
  print(f'\nQuantidade por opção: \n{data[column].value_counts()}')

  if count == True:
    sns.countplot(data = data,x = column, hue = 'distance')
  else:
    sns.displot(data[column], kde = True)

dados_func(dados_df, 'distance')

dados_func(dados_df, 'distance')

df = pd.DataFrame()

df['sessionId'] = dados_df['sessionId']
df['kwhTotal'] = dados_df['kwhTotal']
df['dollars'] = dados_df['dollars']
df['created'] = dados_df['created']
df['ended'] = dados_df['ended']
df['startTime'] = dados_df['startTime']
df['endTime'] = dados_df['endTime']
df['chargeTimeHrs'] = dados_df['chargeTimeHrs']
df['platform'] = dados_df['platform']
df['userId'] = dados_df['userId']
df['stationId'] = dados_df['stationId']
df

df['platform'].unique()

df_analise = pd.DataFrame()

df_analise['chargeTimeHrs'] = df['chargeTimeHrs']
df_analise['platform'] = df['platform']
df_analise

sns.countplot(data = df_analise, x = 'platform')

"""Conclusão: Após analise, foi constatado que a maioria dos usuários que carregaram seus veículos elétricos estão utilizando plataforma IOS. """




# -*- coding: utf-8 -*-
"""Exer1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17cR4Ijm3Ng1Pp4PRldeVPLB6yHWM4uM5
"""

import pandas as pd    #pandas
import numpy as np    #numpy
import matplotlib.pyplot as plt #Para graficae


url="https://drive.google.com/uc?export=download&id=1nh2dHGLvYfTt99nG9kZXEjJFyMe5flSL" #leer de internet
#df_Tunja = pd.read_csv(url, sep=';')
df_Tunja = pd.read_csv(url, encoding='latin-1')

Media_tunja = df_Tunja['Temperatura'].mean()
print('Media Tunja: ', Media_tunja)

url1="https://drive.google.com/uc?export=download&id=13P2nVgy3sJ1-VBzMoA6ae0ZcG3hQXGT9" #leer de internet
df_Iris = pd.read_csv(url1, encoding='latin-1')

Moda_especie = df_Iris['Species'].mode()
print('Moda Especie: ', Moda_especie)

#Variable numerica----------------------------------
print('------------------------------------------------------------------------')
print('Cod_Div')
K=df_Tunja['Cod_Div']
plt.boxplot(K)
plt.show()
#La dispersion de los datos es muy poca o no existe
p25 = K.quantile(0.25)
print('Cuartil' , p25)
p50 = K.quantile(0.5)
print('Cuartil' , p50)
p75 = K.quantile(0.75)
print('Cuartil' , p75)
#Todos los datos son iguales
Data = K.std(axis= 0) #Axis=0 por columnas
print("The Standard Deviation is: \n", Data)

print('------------------------------------------------------------------------')

#Variable numerica----------------------------------
print('------------------------------------------------------------------------')
print('Latitud')
K=df_Tunja['Latitud']
plt.boxplot(K)
plt.show()
#La dispersion de los datos es muy poca o no existe
p25 = K.quantile(0.25)
print('Cuartil' , p25)
p50 = K.quantile(0.5)
print('Cuartil' , p50)
p75 = K.quantile(0.75)
print('Cuartil' , p75)
#Todos los datos son muy similares
Data = K.std(axis= 0) #Axis=0 por columnas
print("The Standard Deviation is: \n", Data)
#gg = df_Tunja.scatter(x='Temperatura', y='Hora')
#gg.plot()
#plt.show()
print('------------------------------------------------------------------------')

#Variable numerica----------------------------------
print('------------------------------------------------------------------------')
print('Longitud')
K=df_Tunja['Longitud']
plt.boxplot(K)
plt.show()
#La dispersion de los datos es muy poca o no existe
p25 = K.quantile(0.25)
print('Cuartil' , p25)
p50 = K.quantile(0.5)
print('Cuartil' , p50)
p75 = K.quantile(0.75)
print('Cuartil' , p75)
#Todos los datos son muy similares
Data = K.std(axis= 0) #Axis=0 por columnas
print("The Standard Deviation is: \n", Data)
#gg = df_Tunja.scatter(x='Temperatura', y='Hora')
#gg.plot()
#plt.show()
print('------------------------------------------------------------------------')

#Variable numerica----------------------------------
print('------------------------------------------------------------------------')
print('Velocidad del viento')
K=df_Tunja['Temperatura']
plt.boxplot(K)
plt.show()
#La dispersion es normal
p25 = K.quantile(0.25)
print('Cuartil' , p25)
p50 = K.quantile(0.5)
print('Cuartil' , p50)
p75 = K.quantile(0.75)
print('Cuartil' , p75)
#Todos los datos no son tan similares
Data = K.std(axis= 0) #Axis=0 por columnas
print("The Standard Deviation is: \n", Data)
#gg = df_Tunja.scatter(x='Temperatura', y='Hora')
#gg.plot()
#plt.show()
print('------------------------------------------------------------------------')

#Variable numerica----------------------------------
print('------------------------------------------------------------------------')
print('Velocidad del Viento')
K=df_Tunja['Velocidad del Viento']
plt.boxplot(K)
plt.show()
#La dispersion es normal
p25 = K.quantile(0.25)
print('Cuartil' , p25)
p50 = K.quantile(0.5)
print('Cuartil' , p50)
p75 = K.quantile(0.75)
print('Cuartil' , p75)
#Todos los datos no son tan similares
Data = K.std(axis= 0) #Axis=0 por columnas
print("The Standard Deviation is: \n", Data)
#gg = df_Tunja.scatter(x='Temperatura', y='Hora')
#gg.plot()
#plt.show()
print('------------------------------------------------------------------------')

#Variable numerica----------------------------------
print('------------------------------------------------------------------------')
print('Presión')
K=df_Tunja['Presión']
plt.boxplot(K)
plt.show()
#La dispersion es normal
p25 = K.quantile(0.25)
print('Cuartil' , p25)
p50 = K.quantile(0.5)
print('Cuartil' , p50)
p75 = K.quantile(0.75)
print('Cuartil' , p75)
#Todos los datos no son tan similares
Data = K.std(axis= 0) #Axis=0 por columnas
print("The Standard Deviation is: \n", Data)
#gg = df_Tunja.scatter(x='Presión', y='Presión')
#gg.plot()
#plt.show()
print('------------------------------------------------------------------------')

#Variable numerica----------------------------------
print('------------------------------------------------------------------------')
print('Punto de Rocío')
K=df_Tunja['Punto de Rocío']
plt.boxplot(K)
plt.show()
#La dispersion es normal
p25 = K.quantile(0.25)
print('Cuartil' , p25)
p50 = K.quantile(0.5)
print('Cuartil' , p50)
p75 = K.quantile(0.75)
print('Cuartil' , p75)
#Todos los datos no son tan similares
Data = K.std(axis= 0) #Axis=0 por columnas
print("The Standard Deviation is: \n", Data)
#gg = df_Tunja.scatter(x='Presión', y='Presión')
#gg.plot()
#plt.show()
print('------------------------------------------------------------------------')

#Variable numerica----------------------------------
print('------------------------------------------------------------------------')
print('SepalLengthCm')
F=df_Iris['SepalLengthCm']
plt.boxplot(F)
plt.show()
#La dispersion es normal
print('Analisis: ', F.describe())
print('------------------------------------------------------------------------')

#Variable numerica----------------------------------
print('------------------------------------------------------------------------')
print('SepalWidthCm')
F=df_Iris['SepalWidthCm']
plt.boxplot(F)
plt.show()
#La dispersion es normal
print('Analisis: ', F.describe())
print('------------------------------------------------------------------------')

#Variable numerica----------------------------------
print('------------------------------------------------------------------------')
print('PetalLengthCm')
F=df_Iris['PetalLengthCm']
plt.boxplot(F)
plt.show()
#La dispersion es normal
print('Analisis: ', F.describe())
print('------------------------------------------------------------------------')

#Variable numerica----------------------------------
print('------------------------------------------------------------------------')
print('PetalLengthCm')
F=df_Iris['PetalLengthCm']
plt.boxplot(F)
plt.show()
#La dispersion es normal
print('Analisis: ', F.describe())
print('------------------------------------------------------------------------')
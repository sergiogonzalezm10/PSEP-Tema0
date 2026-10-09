import csv
from collections import namedtuple
Atleta = namedtuple('Atleta','nombre,edad,pais,peso')
#pepe,20,italia,87.3

nombre_fichero = 'atletas.txt'

def leer_fichero(nombre_fichero):
    registros=[]
    with open(nombre_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for linea in lector:
            nombre = linea[0]
            edad = int(linea[1])
            pais = linea[2]
            peso = float(linea[3])
            tupla = Atleta(nombre, edad, pais, peso)
            registros.append(tupla)
            
    return registros;

#Implementa edad_media(registros).Debe devolverla edad media de todos los atletas

def edad_media(registros):
    res = 0.0
    for r in registros:
        res+=r.edad
    return res/len(registros)

def num_atletas_por_pais(registros):
    diccionario = {}
    for e in registros:
        clave = e.pais
        if clave in diccionario:
            diccionario[clave] = diccionario[clave] + 1
        else:
            diccionario[clave] = 1
    return diccionario

def nombre_atletas_por_pais(registros):
    diccionario = {}
    for r in registros:
        if r.pais not in diccionario:
            diccionario[r.pais] = []
        diccionario[r.pais].append(r.nombre)
    return diccionario

def atleta_mayor_peso(registros):
    return max(registros, key=lambda r:r.peso).nombre

def pais_mayor_peso_medio(registros):
    pesos_por_pais = {}
    for r in registros:
        if r.pais not in pesos_por_pais:
            pesos_por_pais[r.pais] = []
        pesos_por_pais[r.pais].append(r.peso)
    
    peso_medio = {pais: sum(pesos) / len(pesos) for pais, pesos in pesos_por_pais.items()}
    return max(peso_medio, key=peso_medio.get)

def metodozip(registros):
    ordenados = sorted(registros, key=lambda r: r.edad)
    diferencias = [b.edad - a.edad for a, b in zip(ordenados, ordenados[1:])]
    return max(diferencias) if diferencias else 0
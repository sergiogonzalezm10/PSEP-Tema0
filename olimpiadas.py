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

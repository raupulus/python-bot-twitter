#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/fryntiz/ # ###
## ##                             ## ##
# ###       www.fryntiz.es        ### #
#######################################

#Esto es una librería de funciones que ayuda a cambiar entre formatos archivos
#de entrada, principalmente de ODS a CSV

import pyexcel as pe
import codecs  #Librería para codificar en UTF-8 (Error al write ñ)
import os  #Importar lib para interactuar con el sistema


columna_inicio = 1  # Empieza en columna B
columna_limite = 1  # Solo lee 1 columna


#Función a la que se pasa un nombre o ruta hacia archivo y devuelve booleano
def existe_archivo(ruta_archivo):
    return os.path.isfile(ruta_archivo)  # Comprobar que existe


#Función para crear un archivo CSV a partir del ODS
#Se usará solo la columna "B" del archivo pasado (por ahora)
def toCSV(ruta_archivo, ruta_destino):
    global columna_inicio, columna_limite
    if existe_archivo(ruta_archivo):
        #Solo extraer la columna "B" de cada hoja
        HOJAS = pe.get_book(
            file_name=ruta_archivo,
            start_column=columna_inicio,
            column_limit=columna_limite)

        #Abrir archivo donde escribir
        SALIDA_CSV = codecs.open(ruta_destino + '/Publicar.csv',
                    'w', encoding='utf8')

        #Pasar cada línea al archivo csv
        for lines in HOJAS:
            for line in lines:
                # Debe tener más de 20 carácteres y menos de 140
                if ((len(line[0]) > 20) and (len(line[0]) <= 140)):
                    SALIDA_CSV.write(line[0].strip() + '\n')

        print('\n[+]Cerrando Script')
        SALIDA_CSV.close()

        return True
    else:
        print('No existe el archivo pasado')
        return False


def toTXT(ruta_archivo):
    print('Creando Publicar.txt (No implementado)')


def toBD(ruta_archivo):
    print('Añadiendo a la BD (No implementado)')
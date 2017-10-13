#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/fryntiz/ # ###
## ##                             ## ##
# ###       www.fryntiz.es        ### #
#######################################

import pyexcel as pe
import codecs  # Librería para codificar en UTF-8 (Error al write ñ)

columna_inicio = 1  # Empieza en columna B
columna_limite = 1  # Solo lee 1 columna


#Función a la que se pasa un nombre o ruta hacia archivo y devuelve booleano
def existe_archivo(ruta_archivo):
    return os.path.isfile(ruta_archivo)  # Comprobar que existe el archivo en el dir


#Función para crear un archivo CSV a partir del ODS
#Se usará solo la columna "B" del archivo pasado (por ahora)
def toCSV(ruta_archivo):
    if existe_archivo(ruta_archivo):
        #Solo extraer la columna "B" de cada hoja
        HOJAS = pe.get_book(file_name=ruta_archivo, start_column=1, column_limit=1)

        #Abrir archivo donde escribir
        SALIDA = codecs.open('Publicar.csv', 'w', encoding='utf8')

        #Pasar cada línea al archivo csv
        for lines in HOJAS:
            for line in lines:
                # Si no está vacía, debe tener más de 20 carácteres y menos de 140
                if ((len(line[0]) > 20) and (len(line[0]) <= 140)):
                    SALIDA.write(line[0].strip() + '\n')

        return True
    else:
        print('No existe el archivo pasado')
        return False


def toBD(ruta_archivo):
    print('Añadiendo a la BD')


def toTXT(ruta_archivo):
    print('Creando Publicar.txt')
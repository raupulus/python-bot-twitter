#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/raupulus/ # ###
## ##                             ## ##
# ###       raupulus.dev        ### #
#######################################

# Esto es una librería de funciones que ayuda a cambiar entre formatos archivos
# de entrada, principalmente de ODS a CSV

import pyexcel as pe
import codecs  # Librería para codificar en UTF-8 (Error al write ñ)
import os  # Importar lib para interactuar con el sistema


# Función a la que se pasa un nombre o ruta hacia archivo y devuelve booleano
def existe_archivo(ruta_archivo):
    return os.path.isfile(ruta_archivo)  # Comprobar que existe

# Función para crear un archivo CSV a partir del ODS
def toCSV(ruta_archivo, ruta_destino):
    columna_inicio = 0  # Empieza en columna A (TITULO;TWITT;LINK;IMAGE)
    columna_limite = 3  # Solo lee 3 columnas

    if existe_archivo(ruta_archivo):
        book = pe.get_book(
            file_name=ruta_archivo,
            start_column=columna_inicio,
            column_limit=columna_limite,
            start_row=1
        )

        # Abrir archivo donde escribir
        SALIDA_CSV = codecs.open(ruta_destino + '/Publicar.csv',
                     'w', encoding='utf8')

        for sheet in book:
            for line in sheet:
                try:
                    titulo = line[0]
                    entrada = line[1]

                    if len(line) == 2:
                        enlace = ''
                    else:
                        enlace = line[2]

                    todo = titulo + entrada + enlace

                    # Debe tener más de 20 carácteres y menos de 280 el conjunto
                    if ((len(todo) > 20) and (len(todo) <= 280)):
                        SALIDA_CSV.write(
                            titulo.strip() + ';' +
                            entrada.strip() + ';' +
                            enlace.strip() + ';' +
                            '\n'
                        )
                except:
                    print('Hay una línea mal formada o sin datos')

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

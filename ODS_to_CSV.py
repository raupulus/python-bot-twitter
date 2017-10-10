#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/fryntiz/ # ###
## ##                             ## ##
# ###       www.fryntiz.es        ### #
#######################################

#Función para crear un archivo CSV a partir del ODS pasado usando solo la columna "B"
def toODS(nombreArchivo):
    import pyexcel as pe
    import codecs #Librería para codificar en UTF-8 (Error al write ñ)

    #Solo extraer la columna "B" de cada hoja
    HOJAS = pe.get_book(file_name=nombreArchivo, start_column=1, column_limit=1)

    #Abrir archivo donde escribir
    SALIDA = codecs.open('Publicar.csv', 'w', encoding='utf8')

    ##TOFIX
    #Pasar cada línea al archivo csv
    for lines in HOJAS:
        for line in lines:
            # Si no está vacía, debe tener más de 20 carácteres y menos de 140
            if ((len(line[0]) > 20) and (len(line[0]) <= 140)):
                SALIDA.write(line[0].strip() + '\n')

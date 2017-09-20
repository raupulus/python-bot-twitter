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
import codecs #Librería para codificar en UTF-8 (Error al write ñ)

#filas --> start_row=X, row_limit=X
#Columnas --> start_column=X, column_limit=X
#Se fija para que solo extraiga la columna "B" así:
sheet = pe.get_book(file_name="test.ods", start_column=1, column_limit=1)

#Abrir archivo donde escribir
salida = codecs.open('test.csv', 'w', encoding='utf8')

#Pasar cada línea al archivo csv
for lines in sheet:
	#Con la siguiente opción se crea un csv por cada hoja existente:
	#print(lines).save_as("Hoja.csv")
	for line in lines:
		print('Escribiendo: ' + line[0])
		salida.write(line[0] + '\n')

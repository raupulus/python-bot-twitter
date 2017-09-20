#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/fryntiz/ # ###
## ##                             ## ##
# ###       www.fryntiz.es        ### #
#######################################

def toODS(nombreArchivo)
	import pyexcel as pe
	import codecs #Librería para codificar en UTF-8 (Error al write ñ)

	#Solo extraer la columna "B" de cada hoja
	sheet = pe.get_book(file_name="publicar.ods", start_column=1, column_limit=1)

	#Abrir archivo donde escribir
	salida = codecs.open('publicar.csv', 'w', encoding='utf8')

	#Pasar cada línea al archivo csv
	for lines in sheet:
		for line in lines:
			print('Escribiendo: ' + line[0])
			salida.write(line[0] + '\n')

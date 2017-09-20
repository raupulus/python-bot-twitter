#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/fryntiz/ # ###
## ##                             ## ##
# ###       www.fryntiz.es        ### #
#######################################

##############################
##    Importar Librerías    ##
##############################

import time #Importamos la libreria time --> time.sleep
import os #Importamos la libreria para comandos de la consola/shell/bash/sistema
import random #Genera números aleatorios --> random.randrange(1,100)
import os.path #Se utilizará para comprobar que existe un archivo --> os.path.isfile(fname) y os.path.islink(fname)
import ODS_to_CSV
from VAR import * #importar todas las variables

##############################
##         Variables        ##
##############################
sleep = time.sleep #variable para usar con más comodidad el control de tiempo


#Función a la que se pasa un nombre o ruta hacia archivo y devuelve booleano
def existe_archivo(nombre):
	return os.path.isfile(nombre)

#Comprobar si existe el archivo Publicar.ods o pedir nombre y ruta a otro ODS
print('Buscando archivo: ' + ARCHIVO_ENTRADA)
if existe_archivo(ARCHIVO_ENTRADA):
	print('Utilizando el Archivo ' + ARCHIVO_ENTRADA + ' de este mismo directorio')
else:
	print('Archivo ' + ARCHIVO_ENTRADA + ' No encontrado')
	ARCHIVO_ENTRADA = raw_input('Introduce la ruta completa hasta el archivo: ')

ODS_to_CSV.toODS(ARCHIVO_ENTRADA)

# Buscar el archivo publicar.ods y si no existe pedir por pantalla la ruta absoluta y nombre del archivo
def buscarODS():
	print('Buscando archivo ODS')

# Probar abrir CSV y si da error volver a la función anterior
def leerCSV():
	print('Leer CSV')
	#if error --> print('No se puede leer el CSV generado') and buscarODS()

# Conectar a la API


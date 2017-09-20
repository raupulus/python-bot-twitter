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
import VAR.lst #importar lista de variables
##############################
##         Variables        ##
##############################
sleep = time.sleep #variable para usar con más comodidad el control de tiempo

#Función a la que se pasa un nombre o ruta hacia archivo y devuelve booleano
def existe_archivo(nombre)
	os.path.isfile(nombre)

print('Buscando archivo \"Publicar.ods\"')
if existe_archivo(Publicar.ods)
	print('Utilizando el Archivo Publicar.ods de este mismo directorio')
else
	ARCHIVO_ENTRADA = raw_input('Introduce la ruta completa hasta el archivo')
	#TODO --> Necesario controlar que existe el archivo: Crear función en bucle hasta comprobar
toODS(PUB_IN)


# Buscar el archivo publicar.ods y si no existe pedir por pantalla la ruta absoluta y nombre del archivo
def buscarODS()
	print('Buscando archivo ODS')

# Probar abrir CSV y si da error volver a la función anterior
def leerCSV()
	#if error --> print('No se puede leer el CSV generado') and buscarODS()

# Conectar a la API

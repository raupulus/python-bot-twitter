#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/fryntiz/ # ###
## ##                             ## ##
# ###       www.fryntiz.es        ### #
#######################################

##TODO
##Comprobar líneas antes de entrar → No puede estar vacía, ir a la siguiente

##############################
##    Importar Librerías    ##
##############################

import time #Importamos la libreria time --> time.sleep
import sys #Importar comandos del sistema, por ejemplo exit
import os #Importamos la libreria para comandos de la consola/shell/bash/sistema
import random #Genera números aleatorios --> random.randrange(1,100)
import ODS_to_CSV #Importa de este directorio el script para convertir a CSV
import API_Twitter #Importa el script en este directorio para conectar con Twitter
from VAR import * #importar todas las variables

##############################
##         Variables        ##
##############################
sleep = time.sleep #variable para usar con más comodidad el control de tiempo


#Función a la que se pasa un nombre o ruta hacia archivo y devuelve booleano
def existe_archivo(nombre):
	return os.path.isfile(nombre) #Comprueba que existe un archivo --> os.path.isfile(fname) y os.path.islink(fname)

#Comprobar si existe el archivo Publicar.ods o pedir nombre y ruta a otro ODS
print('[+]Buscando archivo: ' + ARCHIVO_ENTRADA)
if existe_archivo(ARCHIVO_ENTRADA):
	print('[+]Utilizando el Archivo ' + ARCHIVO_ENTRADA + ' de este mismo directorio')
else:
	print('[~]Archivo ' + ARCHIVO_ENTRADA + ' No encontrado')
	ARCHIVO_ENTRADA = raw_input('Introduce la ruta completa hasta el archivo: ')

#Convertir a CSV el archivo seleccionado
ODS_to_CSV.toODS(ARCHIVO_ENTRADA)

#Comprobar que existe el archivo Publicar.csv donde están las publicaciones
def comprobarCSV():
	print('[+]Comprobando que existe el archivo Publicar.csv')
	if existe_archivo(ARCHIVO_ENTRADA):
		print('[+]El archivo Publicar.csv existe')
	else:
		print('[-]El archivo Publicar.csv NO EXISTE, revisa manualmente este error')
		sys.exit(0) #Salir del script
comprobarCSV()

#Abrir CSV en solo lectura para poder publicar
def leerCSV():
	print('[+]Abriendo el archivo Publicar.csv')
	try:
		PUBLICACIONES = open('Publicar.csv', 'r')
	except:
		print('[-]Error al abrir Publicar.csv')
		print('[-]Comprueba que existe y tienes permisos de lectura')
		sys.exit(0)
	print('[+]Archivo Publicar.csv abierto en modo LECTURA')
leerCSV()

#Conectar a la API de Twitter
def conectar_Twitter():
	print('[+]Conectando con la API de Twitter')
	print('[+]Espera un momento mientras se establece la conexión')

	tmp = 0
	while tmp <= 10:
		try:
			print('[+]Llamar a la función para conectar')
			API_Twitter.conectar()
		except:
			tmp = tmp + 1
			print('[-]No se ha podido conectar a la API de Twitter, reintento ', tmp)
			if tmp < 10:
				print('[~]Se reintentará en 3 segundos')
				sleep(3)
			elif tmp == 10:
				print('[-]Se han realizado 10 intentos de conexión sin éxito')

	print('Se reintentará más tarde')
	tmp = 0 #Reseteando variable local
conectar_Twitter()

#Leer línea según contador
#Calcular total de líneas para saber cuando parar o comenzar a repetir Twitts
#Llevar contador de la línea actual
#Saltar líneas en blanco o con menos de 10 carácteres

#Twittear 1 entrada cada X minutos (2 en total)

#Agregar 1 favorito cada X minutos (3 en total)

#Retwittear 1 twitt cada X minutos (5 en total)

#Estructura para controlar el tiempo total que trabajará el bot (o hasta infinito)

#Preparando para cerrar
ARCHIVO_ENTRADA.close()


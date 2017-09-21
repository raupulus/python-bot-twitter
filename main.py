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
import tweepy #Librería para facilitar uso de API de twitter
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

#Función para contar el total de líneas en el archivo CSV
def contar_lineas():
	print('[+]Contando líneas en Publicar.csv')
	try:
		ARCHIVO_CSV = open('Publicar.csv', 'r')
		TOTAL_LINEAS = len(ARCHIVO_CSV.readlines())
		ARCHIVO_CSV.close()
	except:
		print('[-]Error al abrir Publicar.csv')
		print('[-]Comprueba que existe y tienes permisos de lectura')
		sys.exit(0)
	print('[+]Se han contado en el Archivo ', TOTAL_LINEAS, ' lineas en total')
	sleep(5)
contar_lineas()

#Abrir CSV en solo lectura para poder publicar
def leerCSV():
	print('[+]Abriendo el archivo Publicar.csv')
	try:
		ARCHIVO_CSV = open('Publicar.csv', 'r')
	except:
		print('[-]Error al abrir Publicar.csv')
		print('[-]Comprueba que existe y tienes permisos de lectura')
		sys.exit(0)
	print('[+]Archivo Publicar.csv abierto en modo LECTURA')
leerCSV()

##TOFIX
#Conectar a la API de Twitter
#Integrar excepciones y controles en API_Twitter.py
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

	print('[Se reintentará más tarde')
	tmp = 0 #Reseteando variable local
#conectar_Twitter() #DESCOMENTAR PARA EJECUTAR

#Publicar la cadena pasada a la función y aumentar el contador de línea
def publicar_Twitter(publicacion):
	API_Twitter.publicar(publicacion)
	#Comprobar que se ha realizado correctamente (return true)
	#Al publicar sin errores en todos los intentos = LINEA_ACTUAL + 1 mediante siguiente_linea()

#Función que comprueba que la línea actual cumpla requisitos de publicación
def comprobar_linea(linea_test):
	#Añadir aquí todas las condiciones que deben cumplir las líneas
	if len(linea_test) > 10:
		return true
	else:
		return false

#Función que controla la línea actual
def siguiente_linea():
	linea_incorrecta = False
	#Comprueba variable linea y continua si está bien, sino busca la siguiente
	if not comprobar_linea(LINEA_ACTUAL):
		linea_incorrecta = True
		while linea_incorrecta:
			LINEA_ACTUAL = LINEA_ACTUAL + 1
			if comprobar_linea(linea):
				linea_incorrecta = False
				break
	#Si está en la última línea se vuelve a la primera
	elif LINEA_ACTUAL == TOTAL_LINEAS:
		LINEA_ACTUAL = 0


#Función a la que se pasa el número de línea y la convierte en cadena.
#Debe llegar siempre una línea bien formada, control en siguiente_linea() y comprobar_linea
def linea_to_cadena(linea):
	linea_to_cadena = ''
	print('[+]La línea' + linea + 'se procesa a cadena')
	#Extraer del archivo CSV la cadena correspondiente a la variable "linea"
	#return cadena


#Twittear 1 entrada cada X minutos (2 en total)

#Agregar 1 favorito cada X minutos (3 en total)

#Retwittear 1 twitt cada X minutos (5 en total)

#Estructura para controlar el tiempo total que trabajará el bot (o hasta infinito)

#Preparando para cerrar
#ARCHIVO_CSV.close()


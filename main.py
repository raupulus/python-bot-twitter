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
LINEA_ACTUAL = 0


#Función a la que se pasa un nombre o ruta hacia archivo y devuelve booleano
def existe_archivo(nombre):
    return os.path.isfile(nombre) #Comprueba que existe un archivo --> os.path.isfile(fname) y os.path.islink(fname)

#Convertir a CSV el archivo ODS. Por defecto busca "Publicar.ods"
def convertir_archivo():
    global ARCHIVO_ENTRADA
    print('\n[+]Buscando archivo: ' + ARCHIVO_ENTRADA)
    if existe_archivo(ARCHIVO_ENTRADA):
        print('[+]Utilizando el Archivo ' + ARCHIVO_ENTRADA + ' de este mismo directorio')
        ODS_to_CSV.toODS(ARCHIVO_ENTRADA)
    else:
        print('[~]Archivo ' + ARCHIVO_ENTRADA + ' No encontrado')
        ARCHIVO_ENTRADA = raw_input('Introduce la ruta completa hasta el archivo: ')
convertir_archivo()

#Comprobar que existe el archivo Publicar.csv donde están las publicaciones
def comprobarCSV():
    print('\n[+]Comprobando que existe el archivo Publicar.csv')
    if existe_archivo(ARCHIVO_ENTRADA):
        print('[+]El archivo Publicar.csv existe')
    else:
        print('[-]El archivo Publicar.csv NO EXISTE, revisa manualmente este error')
        sys.exit(0) #Salir del script
comprobarCSV()

#Función para contar el total de líneas en el archivo CSV
def contar_lineas():
    global ARCHIVO_CSV
    global TOTAL_LINEAS
    print('\n[+]Contando líneas en Publicar.csv')
    try:
        ARCHIVO_CSV = open('Publicar.csv', 'r')
        TOTAL_LINEAS = len(ARCHIVO_CSV.readlines())
        ARCHIVO_CSV.close()
    except:
        print('[-]Error al abrir Publicar.csv')
        print('[-]Comprueba que existe y tienes permisos de lectura')
        sys.exit(0)
    print('[+]Se han contado en el Archivo ' + str(TOTAL_LINEAS) + ' lineas en total')
    sleep(5)
contar_lineas()

#Abrir CSV en solo lectura para poder publicar
def leerCSV():
    global ARCHIVO_CSV
    global ARRAY_ENTRADAS
    print('\n[+]Abriendo el archivo Publicar.csv')
    try:
        ARCHIVO_CSV = open('Publicar.csv', 'r')
        ARRAY_ENTRADAS = ARCHIVO_CSV.read().splitlines()
    except:
        print('[-]Error al abrir Publicar.csv')
        print('[-]Comprueba que existe y tienes permisos de lectura')
        sys.exit(0)
    print('[+]Archivo Publicar.csv abierto en modo LECTURA')
leerCSV()

#Conectar a la API de Twitter
def conectar_Twitter():
    print('\n[+]Conectando con la API de Twitter')
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
#conectar_Twitter() #DESCOMENTAR PARA EJECUTAR

# Función que comprueba que la línea actual cumpla requisitos de publicación
def comprobar_linea(linea_test):
    if ((len(linea_test) >= 20) and (len(linea_test) <= 140)):
        return True
    else:
        return False

# Función que controla la línea actual
def siguiente_linea():
    global LINEA_ACTUAL
    linea_incorrecta = False
    if not comprobar_linea(ARRAY_ENTRADAS[LINEA_ACTUAL]):
        linea_incorrecta = True
        while linea_incorrecta:
            LINEA_ACTUAL = LINEA_ACTUAL + 1
            if comprobar_linea(linea):
                linea_incorrecta = False
                break
    # Si está en la última línea se vuelve a la primera
    elif LINEA_ACTUAL == (TOTAL_LINEAS -1):
        LINEA_ACTUAL = 0
    # Si la línea actual es desconocida o errónea se pone a 0
    elif comprobar_linea(ARRAY_ENTRADAS[LINEA_ACTUAL]):
        LINEA_ACTUAL += 1
    else :
        LINEA_ACTUAL = 0





#Función de pruebas 1 → Muestra cada publicación sin publicarla
def test0():
    #Bucle temporal que llama a la función para crear la cadena a publicar a partir de la línea
    while True:
        print ("[+] Entrada " + str(LINEA_ACTUAL) + " → " + ARRAY_ENTRADAS[LINEA_ACTUAL])
        siguiente_linea()
        sleep(5)
test0()


#Función para solo publicar cada 1h mientras se prueba funcionamiento
def test1():
    while True:
        conectar_Twitter()
        API_Twitter.publicar(ARRAY_ENTRADAS[LINEA_ACTUAL])
        siguiente_linea()
        sleep(7200) # 2 Horas entre publicaciones
#test1


#Twittear 1 entrada cada X minutos (2 en total)

#Agregar 1 favorito cada X minutos (3 en total)

#Retwittear 1 twitt cada X minutos (5 en total)

#Estructura para controlar el tiempo total que trabajará el bot (o hasta infinito)

#Preparando para cerrar
print('\n[+]Cerrando Script')
ARCHIVO_CSV.close()

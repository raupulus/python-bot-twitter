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
import time  # Importamos la libreria time --> time.sleep
#import sys  # Importar comandos del sistema, por ejemplo exit
import os  # Importar lib para interactuar con el sistema
#import random  # Genera números aleatorios --> random.randrange(1,100)
import convert_ODS  # Importa script para convertir a CSV
from perfil import perfil
from publicacion import publicacion

##############################
##         Variables        ##
##############################
sleep = time.sleep
PERFILES = []
CANTIDAD_PERFILES = 0
ENTRADAS = []


# Lista con cada objeto perfil (clase perfil)
def crear_perfiles():
    global PERFILES, CANTIDAD_PERFILES
    listar_perfiles = os.listdir("Perfiles")
    contador_id = 0
    ACCESS_KEY = ''
    ACCESS_SECRET = ''
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''

    #Crear un objeto Perfil con los datos de cada subdirectorio "Perfil"
    for perf in listar_perfiles:
        if ((perf != 'Plantilla') and (perf != 'plantilla') and
            (perf != 'Plantillas') and (perf != 'plantillas')):

            #Leer en "Perfiles/" + perfil + "/token.csv" los valores de API
            tmp_token = open('./Perfiles/' + perf + '/token.csv', 'r')
            for line in tmp_token:
                line_clean = line.replace(' ', '').strip().split('=')
                if (line_clean[0].upper() == 'ACCESS_KEY'):
                    print('ACCESS_KEY → ' + line_clean[1])
                    ACCESS_KEY = line_clean[1]
                elif (line_clean[0].upper() == 'ACCESS_SECRET'):
                    print('ACCESS_SECRET → ' + line_clean[1])
                    ACCESS_SECRET = line_clean[1]
                elif (line_clean[0].upper() == 'CONSUMER_KEY'):
                    print('CONSUMER_KEY → ' + line_clean[1])
                    CONSUMER_KEY = line_clean[1]
                elif (line_clean[0].upper() == 'CONSUMER_SECRET'):
                    print('CONSUMER_SECRET → ' + line_clean[1])
                    CONSUMER_SECRET = line_clean[1]

            #Creando entradas para este perfil, se pasa la ruta hacia perfil
            #TODO → Si la siguiente función devuelve false no crear perfil
            #en ese caso sería que no hay entradas¿?¿?
            crear_entradas('./Perfiles/' + perf)

            #Creando objeto "perfil(id,nombre,AK,AS,CK,CS"
            print('Creando perfil: ' + perf + ' id-' + str(contador_id))
            PERFILES.append(perfil(contador_id, perf,
                ACCESS_KEY, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
            contador_id += 1

    #TEMPORAL
    print('\n[+] Cantidad de entradas → ' + str(len(ENTRADAS)))

    #Recuenta la cantidad total de perfiles
    CANTIDAD_PERFILES = len(PERFILES)
    print('\n[+] Cantidad de perfiles → ' + str(CANTIDAD_PERFILES))


# Crea el array de entradas para cada perfil
#TOFIX → Plantear que esto lo haga la clase perfil (perfil - API_TWITTER)
def crear_entradas(ruta_perfil):
    global ENTRADAS
    print('[+] Buscando archivo → ' + ruta_perfil + '/Publicar.ods')

    #TODO → Eliminar entrada y perfil del array principal si no hay CSV

    if existe_archivo(ruta_perfil + '/Publicar.ods'):
        print('[+] Utilizando el Archivo Publicar.ods')
        convert_ODS.toCSV(ruta_perfil + '/Publicar.ods', ruta_perfil)
    elif existe_archivo(ruta_perfil + '/publicar.ods'):
        print('[+] Utilizando el Archivo publicar.ods')
        convert_ODS.toCSV(ruta_perfil + '/publicar.ods', ruta_perfil)
    else:
        print('[~] No encontrado ningún archivo publicar.ods ni Publicar.ods')

    #Se comprueba que el CSV se ha creado antes de intentar crear objetos
    # Array con cada entrada. La posición coincide con posición en PERFILES
    if existe_archivo(ruta_perfil + '/Publicar.csv'):
        ENTRADAS.append(publicacion(ruta_perfil + '/Publicar.csv'))
        #return True
    elif existe_archivo(ruta_perfil + '/publicar.csv'):
        ENTRADAS.append(publicacion(ruta_perfil + '/publicar.csv'))
        #return True
    else:
        print('[-] No se encuentra el archivo CSV para este perfil')
        #return False


#Función a la que se pasa un nombre o ruta hacia archivo y devuelve booleano
def existe_archivo(ruta_archivo):
    return os.path.isfile(ruta_archivo)  # Comprobar que existe


#Convertir a CSV el archivo ODS. Por defecto busca "Publicar.ods"
def inicializar():
    crear_perfiles()

inicializar()


# Publicar
def publicar():
    print('[+] Preparando para publicar')


# Retwittear
def retwittear():
    print('[+] Preparando para retwittear')


# Seguir
def seguir():
    print('[+] Preparando para seguir')


# Programa principal para interactuar con el bot
def panel_control():
    print('Elige una opción de las siguientes (No Implementado')
#panel_control()


# Depuración del programa
def depurador():
    print('Se ha ejecutado el modo depurador (No Implementado)')


#Función de pruebas 1 → Muestra cada publicación sin publicarla
def test0():
    #TODO → CREAR BUCLE FOR PARA MOSTRAR 1 PUBLICACIÓN DE CADA PERFIL
    #Bucle temporal para crear la cadena a publicar a partir de la línea
    while True:
        print('\n[+] Entrada Publicada:\n' + ENTRADAS[0].publicacion_actual())
        ENTRADAS[0].siguiente_linea()
        sleep(5)
test0()


#Función para solo publicar cada 1h mientras se prueba funcionamiento
def test1():
    while True:
        print('\n[+] Entrada Publicada:\n' + ENTRADAS[0].publicacion_actual())
        ENTRADAS[0].siguiente_linea()
        sleep(7200)  # 2 Horas entre publicaciones
#test1


#Función para publicar cada 6 horas
def test2():
    while True:
        print('\n[+] Entrada Publicada:\n' + ENTRADAS[0].publicacion_actual())
        ENTRADAS[0].siguiente_linea()
        sleep(21600)  # 6 Horas entre publicaciones
#test2


#Obtiene el timeline agregándolo a un archivo
def test3():
    print('Conectando API')
    print('Obteniendo timeline')
    print('Pasándolo al archivo XXXX')
#test3


#
def test4():
    print('test')

#test3

#Preparando para cerrar script → print('\n[+]Cerrando Script')
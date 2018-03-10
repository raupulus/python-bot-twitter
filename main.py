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
import time  #Importamos la libreria time --> time.sleep
#import sys  #Importar comandos del sistema, por ejemplo exit
import os  #Importar lib para interactuar con el sistema
#import random  #Genera números aleatorios --> random.randrange(1,100)
from Perfil import Perfil

##############################
##         Variables        ##
##############################
sleep = time.sleep
PERFILES = []  #Todos los perfiles instanciados
CANTIDAD_PERFILES = 0

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
            (perf != 'Plantillas') and (perf != 'plantillas') and
            (perf != '.gitignore')):

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

            #Creando objeto "perfil(id,nombre,AK,AS,CK,CS"
            print('Creando perfil: ' + perf + ' id-' + str(contador_id))
            PERFILES.append(Perfil(contador_id, perf,
                                   ACCESS_KEY, ACCESS_SECRET, CONSUMER_KEY,
                                   CONSUMER_SECRET))
            contador_id += 1

    #Recuenta la cantidad total de perfiles
    CANTIDAD_PERFILES = len(PERFILES)
    print('\n[+] Cantidad de perfiles → ' + str(CANTIDAD_PERFILES))


#Convertir a CSV el archivo ODS. Por defecto busca "Publicar.ods"
def inicializar():
    crear_perfiles()
inicializar()


# Publicar
def publicar(tiempo):
    print('[+] Preparando para publicar')
    while True:
        for i in range(0, CANTIDAD_PERFILES):
            print('Indice del perfil → ' + str(i))
            PERFILES[i].publicar()
            sleep(tiempo)


#Retwittear
def retwittear():
    print('[+] Preparando para retwittear')
    while True:
        for i in range(0, CANTIDAD_PERFILES):
            PERFILES[i].retwittear()

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
    publicar(5)
test0()


#Función para solo publicar cada 1h mientras se prueba funcionamiento
def test1():
    while True:
        print('\n[+] Entrada Publicada:\n' + PERFILES[0].publicar())
        sleep(7200)  # 2 Horas entre publicaciones
#test1


#Función para publicar cada 6 horas
def test2():
    while True:
        print('\n[+] Entrada Publicada:\n' + PERFILES[0].publicar())
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
#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/raupulus/ # ###
## ##                             ## ##
# ###       raupulus.dev        ### #
#######################################

##############################
##    Importar Librerías    ##
##############################
from time import sleep  # Importamos la libreria time --> time.sleep
#import sys  # Importar comandos del sistema, por ejemplo exit
import os  # Importar lib para interactuar con el sistema
#import random  # Genera números aleatorios --> random.randrange(1,100)
from Perfil import Perfil

##############################
##         Variables        ##
##############################
PERFILES = []  # Todos los perfiles instanciados
CANTIDAD_PERFILES = 0

# Lista con cada objeto perfil (clase perfil)
def crear_perfiles():
    global PERFILES, CANTIDAD_PERFILES
    listar_perfiles = os.listdir("Perfiles")
    contador_id = 0

    # Crear un objeto Perfil con los datos de cada subdirectorio "Perfil"
    for perfil in listar_perfiles:
        if (perfil != 'Plantilla') and (perfil != '.gitignore'):

            #Creando objeto "perfil(id,nombre,AK,AS,CK,CS"
            print('Creando perfil: ' + perfil + ' id-' + str(contador_id))
            PERFILES.append(Perfil(contador_id, perfil))
            contador_id += 1

    # Recuenta la cantidad total de perfiles
    CANTIDAD_PERFILES = len(PERFILES)
    print('\n[+] Cantidad de perfiles → ' + str(CANTIDAD_PERFILES))


# Convertir a CSV el archivo ODS. Por defecto busca "Publicar.ods"
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


# Retwittear
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


# Función para solo publicar cada 1h mientras se prueba funcionamiento
def test1():
    while True:
        print('\n[+] Entrada Publicada:\n' + PERFILES[0].publicar())
        sleep(7200)  # 2 Horas entre publicaciones
#test1


# Muestra los últimos 50 elementos del timeline y publica solo 1 entrada
def test4():
    print('Estoy realizando una prueba')
    PERFILES[0].conectar()
    PERFILES[0].publicar()
    #PERFILES[0].leer_timeline()
test4()

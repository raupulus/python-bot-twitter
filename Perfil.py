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
import tweepy  # Librería para facilitar uso de API de twitter
import os  # Importar lib para interactuar con el sistema
import convert_ODS  #Importa script para convertir a CSV
from Token import Token
from Publicacion import Publicacion

##TOFIX las siguientes funciones
##Función para dar favorito
##Función para analizar comentarios de un tweet
##Función para retwittear todo lo de un array de personas
##Función para seguir a quien me siga si cumple un patrón


class Perfil:
    VALIDA = False  # Comprueba si el perfil es válido

    posicion = 0  # Posición en el array donde se almacena este objeto
    API = ''
    ENTRADAS = ''  # Objeto Publicación con las entradas
    total_publicado = 0  # Publicaciones totales de este perfil

    def __init__(self, pos, nom):
        self.posicion = pos
        self.nombre = nom
        self.RUTA_PERFIL = 'Perfiles/' + nom

        self.ARCHIVO_ENTRADA = nom + '/Publicar.ods'
        self.ARCHIVO_ENTRADA_CSV = nom + '/Publicar.csv'

        self.TOKEN = Token(self.RUTA_PERFIL)
        self.ACCESS_KEY = self.TOKEN.ACCESS_KEY
        self.ACCESS_SECRET = self.TOKEN.ACCESS_SECRET
        self.CONSUMER_KEY = self.TOKEN.CONSUMER_KEY
        self.CONSUMER_SECRET = self.TOKEN.CONSUMER_SECRET

        if self.crear_entradas():
            self.VALIDA = True

# Cadena a devolver cuando se convierta el objeto a STR
    def __srt__(self):
        return self.nombre + " posición → " + self.posicion

# Función a la que se pasa un nombre o ruta hacia archivo y devuelve booleano
    def existe_archivo(self, ruta_archivo):
        return os.path.isfile(ruta_archivo)  # Comprobar que existe

# Crea el array de entradas para este perfil
# En el futuro se tomará solo la posición para extraerlo de BD
    def crear_entradas(self):
        ruta_entradas = 'Perfiles/' + self.ARCHIVO_ENTRADA
        ruta_entradas_csv = 'Perfiles/' + self.ARCHIVO_ENTRADA_CSV
        ruta_perfil = self.RUTA_PERFIL

        print('[+] Buscando archivo → ' + ruta_entradas)

        if self.existe_archivo(ruta_entradas):
            print('[+] Utilizando el Archivo Publicar.ods')
            convert_ODS.toCSV(ruta_entradas, ruta_perfil)
        else:
            print('[~] No encontrado ningún archivo Publicar.ods')

        # Se comprueba que el CSV se ha creado antes de intentar crear objetos
        if self.existe_archivo(ruta_entradas_csv):
            self.ENTRADAS = Publicacion(ruta_entradas_csv)
            print('\n[+] Cantidad de entradas → ' + str(
                self.ENTRADAS.TOTAL_LINEAS))
            return True
        else:
            print('[-] No se encuentra el archivo CSV para este perfil')
            return False


# Función para conectar con la API de Twitter
    def conectar(self):
        print('\n[+]Conectando con la API de Twitter')
        print('[+]Espera un momento mientras se establece la conexión')

        try:
            print('[!]Conectando con la API')
            autenticar = tweepy.OAuthHandler(
                self.CONSUMER_KEY,
                self.CONSUMER_SECRET)
            autenticar.set_access_token(
                self.ACCESS_KEY,
                self.ACCESS_SECRET)
            self.API = tweepy.API(autenticar)
        except:
            print('[-]No se ha conectado a la API de twitter')

# Función para Publicar en Twitter (Recibe una cadena de 1 sola línea a
    # publicar)
    def publicar(self):
        self.total_publicado += 1
        print("[+] Twitteando la siguiente entrada...")
        try:
            linea_actual = self.ENTRADAS.LINEA_ACTUAL
            publicacion = self.ENTRADAS.ARRAY_ENTRADAS[linea_actual]
            #self.API.update_status(status=publicacion)
            print("[+] Tweet: " + publicacion)
            print("[+] Se han publicado en total: " + str(self.total_publicado))
            return True
        except:
            print("[-] No se ha logrado publicar")
            return False

# Función para Leer en el timeline las 50 publicaciones últimas
# Al leer timeline también trae información como retweets y like..
    def leer_timeline(self):
        public_tweets = self.API.home_timeline(50)
        for tweet in public_tweets:
            print("[+] %s" % tweet.text)

# Seguir a quien me sigue y cumple unos patrones
# (Solo compruebo los 10 últimos seguidores)
    def seguir(self):
        for follower in tweepy.Cursor(self.API.followers).items(10):
            follower.follow()
            print ("Se ha declarado seguir a → " + follower.screen_name)

# Función para retwittear últimos mensajes según patrón coincidente
    def retwittear(self):
        print('Se retwitteará lo siguiente → ')

# Guardar información de un usuario específico que se pasa a la función
    def recopilar_info(self, usuarios):
        #FIXME → usuarios es un array con la cantidad de usuarios a vigilar
        for usuario in usuarios:
            user = self.API.get_user(usuario)
            #TOFIX → Estos datos se guardarán en CVS o BD
            print("Nombre público o Nick → " + user.screen_name)
            print("Cantidad de seguidores → " + user.followers_count)
            print(" <<<<< LISTA DE AMIGOS >>>>>")
            for friend in user.friends():
                print(friend.screen_name)

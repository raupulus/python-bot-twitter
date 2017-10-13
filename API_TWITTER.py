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

##TOFIX las siguientes funciones
##Función para dar favorito
##Función para analizar comentarios de un tweet
##Función para retwittear todo lo de un array de personas
##Función para seguir a quien me siga si cumple un patrón


class API_TWITTER:

    nombre = ''
    posicion = 0  # Posición en el array donde se almacena este objeto
    API = ''

    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_KEY = ''
    ACCESS_SECRET = ''

    def __init__(self, pos, nom, C_K, C_S, A_K, A_S):
        print('Construyendo Clase')
        global posicion, nombre
        global CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
        posicion = pos
        nombre = nom
        CONSUMER_KEY = C_K
        CONSUMER_SECRET = C_S
        ACCESS_KEY = A_K
        ACCESS_SECRET = A_S

    def __srt__(self):
        global nombre, posicion
        return nombre + " posición → " + posicion

#Función para conectar con la API de Twitter (Variables en VAR.py)
    def conectar():
        global API
        global CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
        print('Conectando con la API')
        autenticar = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        autenticar.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        API = tweepy.API(autenticar)

#Función para Publicar en Twitter (Recibe una cadena de 1 sola línea a publicar)
    def publicar(publicacion):
        global API
        print("[+] Twitteando la siguiente entrada...")
        try:
            API.update_status(status=publicacion)
            print("[+] Tweet: " + publicacion)
            return True
        except:
            print("[-] No se ha logrado publicar")
            return False

#Función para Leer en el timeline las 50 publicaciones últimas
    def leer_timeline():
        global API
        public_tweets = API.home_timeline(50)
        for tweet in public_tweets:
            print "[+] %s" % tweet.text

#Seguir a quien me sigue y cumple unos patrones
#(Solo compruebo los 10 últimos seguidores)
    def seguir():
        global API
        for follower in tweepy.Cursor(API.followers).items(10):
            follower.follow()
            print ("Se ha declarado seguir a → " + follower.screen_name)

#Función para retwittear últimos mensajes según patrón coincidente
    def retwittear():
        print('Se retwitteará lo siguiente → ')

#Guardar información de un usuario específico que se pasa a la función
    def recopilar_info(usuarios):
        #TOFIX → usuarios es un array con la cantidad de usuarios a vigilar
        global API
        for usuario in usuarios:
            user = API.get_user(usuario)
            #TOFIX → Estos datos se guardarán en CVS o BD
            print "Nombre público o Nick → " + user.screen_name
            print "Cantidad de seguidores → " + user.followers_count
            print " <<<<< LISTA DE AMIGOS >>>>>"
            for friend in user.friends():
                print friend.screen_name
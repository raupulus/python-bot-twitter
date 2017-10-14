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
from time import sleep  # Importamos la libreria time --> time.sleep

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
        print('[!] Creando perfil con nombre → ' +
            str(nom) + ' en posición' + str(pos))
        self.posicion = pos
        self.nombre = nom
        self.CONSUMER_KEY = C_K
        self.CONSUMER_SECRET = C_S
        self.ACCESS_KEY = A_K
        self.ACCESS_SECRET = A_S

#Cadena a devolver cuando se convierta el objeto a STR
    def __srt__(self):
        return self.nombre + " posición → " + self.posicion

#Función para conectar con la API de Twitter (Variables en VAR.py)
    def conectar(self):
        print('\n[+]Conectando con la API de Twitter')
        print('[+]Espera un momento mientras se establece la conexión')

        tmp = 0
        while tmp <= 10:
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
                tmp = tmp + 1
                print('[-]No se ha conectado a la API, reintento → ', tmp)
                if tmp < 10:
                    print('[~]Se reintentará en 7 segundos')
                    sleep(7)
                elif tmp == 10:
                    print('[-]Se han realizado 10 intentos de conectar')
        print('[!] Se reintentará más tarde')

#Función para Publicar en Twitter (Recibe una cadena de 1 sola línea a publicar)
    def publicar(self, publicacion):
        global API
        print("[+] Twitteando la siguiente entrada...")
        try:
            self.API.update_status(status=publicacion)
            print("[+] Tweet: " + publicacion)
            return True
        except:
            print("[-] No se ha logrado publicar")
            return False

#Función para Leer en el timeline las 50 publicaciones últimas
    def leer_timeline(self):
        public_tweets = self.API.home_timeline(50)
        for tweet in public_tweets:
            print "[+] %s" % tweet.text

#Seguir a quien me sigue y cumple unos patrones
#(Solo compruebo los 10 últimos seguidores)
    def seguir(self):
        for follower in tweepy.Cursor(self.API.followers).items(10):
            follower.follow()
            print ("Se ha declarado seguir a → " + follower.screen_name)

#Función para retwittear últimos mensajes según patrón coincidente
    def retwittear(self):
        print('Se retwitteará lo siguiente → ')

#Guardar información de un usuario específico que se pasa a la función
    def recopilar_info(self, usuarios):
        #TOFIX → usuarios es un array con la cantidad de usuarios a vigilar
        for usuario in usuarios:
            user = self.API.get_user(usuario)
            #TOFIX → Estos datos se guardarán en CVS o BD
            print "Nombre público o Nick → " + user.screen_name
            print "Cantidad de seguidores → " + user.followers_count
            print " <<<<< LISTA DE AMIGOS >>>>>"
            for friend in user.friends():
                print friend.screen_name
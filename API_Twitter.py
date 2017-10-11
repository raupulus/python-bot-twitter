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
##Función para dar favorito
##Función para analizar comentarios de un tweet
##Función para retwittear todo lo de un array de personas
##Función para seguir a quien me siga si cumple un patrón

#Función para conectar con la API de Twitter (Variables en VAR.py)
def conectar():
    print('Conectando con la API')
    autenticar = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    autenticar.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(autenticar)

#Función para Publicar en Twitter (Recibe una cadena de 1 sola línea a publicar)
def publicar(publicacion):
    print("[+] Twitteando la siguiente entrada...")
    try:
        api.update_status(status = publicacion)
        print("[+] Tweet: " + publicacion)
        return True
    except:
        print("[-] No se ha logrado publicar")
        return False

#Función para Leer en el timeline las 50 publicaciones últimas
def leer_timeline():
    public_tweets = api.home_timeline(50)
    for tweet in public_tweets:
        print "[+] %s" % tweet.text

#Seguir a quien me sigue y cumple unos patrones (Solo compruebo los 10 últimos seguidores)
def seguir():
    for follower in tweepy.Cursor(api.followers).items(10):
        follower.follow()
        print ("Se ha declarado seguir a → " + follower.screen_name)

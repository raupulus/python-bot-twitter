#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/fryntiz/ # ###
## ##                             ## ##
# ###       www.fryntiz.es        ### #
#######################################

####TO_DO AND TO_FIX####
#Comprobar salto de línea "\n" para hacer "break" y no publicarlo
#Establecer formato de publicaciones desde una hoja de cálculo


##############################
##    Importar Librerías    ##
##############################

import time, os, random, tweepy, sys

##############################
##         Variables        ##
##############################

sleep = time.sleep
ARCHIVO_ENTRADA = "./entrada.txt"

#Importar modulo de twitter e iniciar conexión con este usando tokens OAUTH:
#from twitter import Twitter, OAuth, TwitterHTTPError

ACCESS_KEY = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Autentificar en python
#t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
#            CONSUMER_KEY, CONSUMER_SECRET))

filename = open(ARCHIVO_ENTRADA,'r')
f = filename.readlines()
filename.close()

for line in f:
    print("[+] Twitteando la siguiente entrada...")
    api.update_status(status = line)
    print("[+] Tweet: ", line)
    time.sleep(20)


















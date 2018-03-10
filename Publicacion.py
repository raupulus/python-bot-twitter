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
import os  # Importar lib para interactuar con el sistema
import sys  # Importar comandos del sistema, por ejemplo exit


class Publicacion:
    LINEA_ACTUAL = 0
    TOTAL_LINEAS = 0
    documento_abierto = ''
    ARRAY_ENTRADAS = ''  # Contiene las entradas divididas en líneas

    def __init__(self, archivo_publicaciones):
        print('[+] Creando Objeto de publicación')

        self.comprobarCSV(archivo_publicaciones)
        self.leerCSV(archivo_publicaciones)
        self.contar_lineas()

# Función a la que se pasa un nombre o ruta hacia archivo y devuelve booleano
    def existe_archivo(self, archivo_publicaciones):
        return os.path.isfile(archivo_publicaciones)  #Comprobar que existe

# Comprobar archivo, mejorar esta parte para que se
    def comprobarCSV(self, archivo_publicaciones):
        print('\n[+]Comprobando que existe el archivo Publicar.csv')
        if self.existe_archivo(archivo_publicaciones):
            print('[+]El archivo Publicar.csv existe')
        else:
            print('[-]El archivo Publicar.csv NO EXISTE, revísalo')
            sys.exit(0)  # Salir del script
            #return false

    # Abrir CSV en solo lectura para poder publicar
    def leerCSV(self, archivo_publicaciones):
        print('\n[+]Abriendo el archivo Publicar.csv')
        try:
            self.documento_abierto = open(archivo_publicaciones, 'r')
            self.ARRAY_ENTRADAS = self.documento_abierto.read().splitlines()
        except:
            print('[-]Error al abrir Publicar.csv')
            print('[!]Comprueba que existe y tienes permisos de lectura')
            sys.exit(0)
        print('[+]Archivo Publicar.csv abierto en modo LECTURA')

    # Función para contar el total de líneas en el archivo CSV
    def contar_lineas(self):
        print('\n[+]Contando líneas en Publicar.csv')
        try:
            self.TOTAL_LINEAS = len(self.ARRAY_ENTRADAS)
        except:
            print('[-]Error al abrir Publicar.csv')
            print('[!]Comprueba que existe y tienes permisos de lectura')
            sys.exit(0)
        print('[+]Total de líneas → ' + str(self.TOTAL_LINEAS))

# Comprobar línea que se le pasa
    def comprobar_linea(self, linea):
        if ((len(linea) >= 10) and (len(linea) <= 280)):
            return True
        else:
            return False

# Comprueba la validez de la próxima línea y se posiciona sobre ella
    def siguiente_linea(self):
        linea_incorrecta = False
        if not self.comprobar_linea(self.ARRAY_ENTRADAS[self.LINEA_ACTUAL]):
            linea_incorrecta = True
            while linea_incorrecta:
                self.LINEA_ACTUAL = self.LINEA_ACTUAL + 1
                if self.comprobar_linea(self.ARRAY_ENTRADAS[self.LINEA_ACTUAL]):
                    linea_incorrecta = False
                    break
        # Si está en la última línea se vuelve a la primera
        elif self.LINEA_ACTUAL == (self.TOTAL_LINEAS - 1):
            self.LINEA_ACTUAL = 0
        # Si la línea actual es desconocida o errónea se pone a 0
        elif self.comprobar_linea(self.ARRAY_ENTRADAS[self.LINEA_ACTUAL]):
            self.LINEA_ACTUAL += 1
        else:
            self.LINEA_ACTUAL = 0

    # Devuelve una cadena con la línea a publicar
    def publicacion_actual(self):
        try:
            linea = str(self.ARRAY_ENTRADAS[self.LINEA_ACTUAL])
            return linea
        except:
            print("No tiene líneas el documento")
            return False
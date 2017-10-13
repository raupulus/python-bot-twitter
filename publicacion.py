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


class publicacion:
    LINEA_ACTUAL = 0
    documento_abierto = ''
    TOTAL_LINEAS = 0

    def __init__(self, archivo_publicaciones):
        print('Creando Objeto de publicación')
        #Comprobar el archivo CSV pasado

        comprobarCSV()
        contar_lineas()
        leerCSV()




def comprobarCSV():
            print('\n[+]Comprobando que existe el archivo Publicar.csv')
            if existe_archivo(ARCHIVO_ENTRADA):
                print('[+]El archivo Publicar.csv existe')
            else:
                print('[-]El archivo Publicar.csv NO EXISTE, revísalo')
                sys.exit(0)  # Salir del script



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




#TOFIX → mirar este método bien
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
        print('[+]Total de líneas contadas ' + str(TOTAL_LINEAS) + ' líneas')
        sleep(5)


    def comprobar_linea(linea):
        print('Comprobando línea recibida')
        if ((len(linea_test) >= 20) and (len(linea_test) <= 140)):
            return True
        else:
            return False

    def publicacion_actual(linea):
        print('La línea actual es')

        # return string con la línea

#Comprueba la validez de la próxima línea y se posiciona sobre ella
    def siguiente_linea():
        print('Estableciéndo contador en la próxima línea')
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
        elif LINEA_ACTUAL == (TOTAL_LINEAS - 1):
            LINEA_ACTUAL = 0
        # Si la línea actual es desconocida o errónea se pone a 0
        elif comprobar_linea(ARRAY_ENTRADAS[LINEA_ACTUAL]):
            LINEA_ACTUAL += 1
        else:
            LINEA_ACTUAL = 0

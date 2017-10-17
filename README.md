# bot_twitter
Bot para publicar, marcar twitts favoritos y retwittear según patrones coincidentes

El principal objetivo de este bot es analizar antes de actuar y no actuar siempre de manera previsible.

Es posible que requiera una porción insignificante de tiempo por encima de lo normal antes de actuar ya que conecta mediante la API de twitter para comprobar twitt y retwitt de objetivos seleccionados para según el patrón establecido retwittear también o dar me gusta.

Mediante una función se programarán publicaciones cada cierto tiempo, ajustando este valor entre las variables mínimas y máximas. La idea es que pase un tiempo distinto entre cada publicación por ejemplo mínimo 10minutos y máximo 40minutos → Esto será calculado mediante una función que devuelva el tiempo aleatoriamente.

---

## Versión actual 0.1 (beta)
Actualmente está en desarrollo por lo que no se recomienda aún el uso.

Se continúa trabajando sobre el bot, ya es posible twittear pero se ha de solventar manualmente ciertas cuestiones que serán corregidas en breve.

---

## Obejtivos del bot
- [x] Exportar de ODS a CSV
- [x] Conectar con API de Twitter
- [x] Convertir número de línea a cadena
- [x] Publicar automáticamente todas las líneas del CSV
- [x] Crear automáticamente multiperfiles
- [ ] Marcar favoritos según patrones
- [ ] Marcar favorito todo según quien comparta
- [ ] Retwittear según patrones
- [ ] Retwittear todo según quien comparta
- [ ] Estadísticas de seguimiento a otros usuarios recopilando información a una BD
- [ ] Conectar a BD SQLite local donde se controla las veces que se publica cada una
- [ ] Publicaciones aleatorias de todo el archivo, solo se repite a partir de 10 días una publicación (comprobar fecha) y la publicación más twitteada no puede distar más de 3 sobre la menos publicada. Así se equilibra que una se publique mucho más que otra creando cierta aletoriedad

---

## Datos del proyecto
BOT solo probado en _GNU/Linux_ **Debian 9** y **Fedora 26**

Para las publicaciones es necesario que exista un archivo en formato y con la extensión "ods" en el mismo directorio o pedirá elegir donde obtenerlo mediante una ruta absoluta en el sistema. Dicho archivo se busca por defecto en el mismo directorio del bot con el siguiente nombre "publicar.ods"

---

### Conversión a CSV
Para las publicaciones se utiliza un archivo LibreCalc en formato ODS donde la columna "B" será la que contenga las publicaciones y será la que se exportará al CSV como una publicación por línea.

---

## Estructura
- main.py → Contiene el programa principal, todas las llamadas y funcionamiento.
- convert_ODS.py → Transforma hoja de cálculo en formato ODS de LibreOffice a CSV para trabajar más sencillo
- perfil.py → Incluye las funciones para interactuar con la API de twitter, capa intermediaria entre el *main.py* y el módulo *tweepy*
- publicacion.py →
---

## Dependencias
Aquí se listan las dependencias necesarias para el correcto funcionamiento del bot
- python 2.7
- Módulos/Librerías python externos
    - pyexcel-ods
    - twitter
    - codecs
    - tweepy
    - readline

---

## Instalar dependencias en Debian 9
```shell
sudo apt install git python python-pip
```

```shell
pip install pyexcel-{xlsxw,ods,ods3,odsr,xlsx,xls} codecs twitter tweepy readline
```
---

## Colaboradores
### Raúl Caro Pastorino @fryntiz
- GitHub → https://github.com/fryntiz
- E-mail → tecnico@fryntiz.es
- WEB → http://www.fryntiz.es

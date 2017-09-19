# bot_twitter
Bot para publicar, marcar twitts favoritos y retwittear según patrones coincidentes

El principal objetivo de este bot es analizar antes de actuar y no actuar siempre de manera previsible.

Es posible que requiera una porción insignificante de tiempo por encima de lo normal antes de actuar ya que conecta mediante la API de twitter para comprobar twitt y retwitt de objetivos seleccionados para según el patrón establecido retwittear también o dar me gusta.

Mediante una función se programarán publicaciones cada cierto tiempo, ajustando este valor entre las variables mínimas y máximas. La idea es que pase un tiempo distinto entre cada publicación por ejemplo mínimo 10minutos y máximo 40minutos → Esto será calculado mediante una función que devuelva el tiempo aleatoriamente.


## Estructura
- main.py → Contiene el programa principal, todas las llamadas y funcionamiento.
- VAR.lst → Lista de variables para el funcionamiento del programa, incluyendo token de API twitter
- ODS_to_CSV → Transforma oja de cálculo en formato ODS de LibreOffice a CSV para trabajar más sencillo

## Dependencias
Aquí se listan las dependencias necesarias para el correcto funcionamiento del bot
- python 2.7
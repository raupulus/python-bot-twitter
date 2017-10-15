# Este directorio es una plantilla
Para usar esta **plantilla** puedes copiarla y renombrarla rellenando los
datos respecto al perfil con el que lo quieres conectar.

## Archivos de publicaciones
Este programa se ha pensado para que por comodidad editemos una hoja de cálculo
en libreoffice con formato "ODS" y la dejemos en el directorio de perfil con el
nombre "Publicar.ods". Este archivo se convertirá automáticamente a CSV antes
de ser publicado.

Por otro lado podemos directamente editar o exportar a CSV manualmente y añadir
a el mismo directorio del perfil un archivo llamado "Publicar.csv"

Los cambios realizados en el archivo "Publicar.csv" durante la ejecución del
programa, serán aplicados una vez haya terminado de publicarse la última.

## Formato de cada línea dentro de "Publicar.ods"
- Cada línea será una publicación.
- Comenzará en la columna "B" Línea 2, de forma que saltamos la primera
puesto que son títulos
- En la misma línea si introducimos un salto de línea funcionará como otra línea
por ahora

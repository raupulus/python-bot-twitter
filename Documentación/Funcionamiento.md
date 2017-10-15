# Descripción básica del funcionamiento
En este archivo se describe como deberá funcionar, el caso
de uso para este proyecto.

## Entrada de datos
Los datos estarán en un directorio agrupados por perfiles de twitter, de tal
manera que en cada uno de didchos directorios se encuentren:
- TOKEN de api twitter
- Un documento de hojas de cálculo en formato ODS (LibreOffice)
- En el caso de existir un documento CSV no se buscará el documento ODS
- El documento con las publicaciones se deberá llamar "Publicar.ods" o "Publicar.csv"
- Se leerá contínuamente la entrada por telegram para publicar aquellos mensajes
que vengan precedidos por el hastag #publicar seguido de una cadena
- Cuando un perfil termina o más bien llega a la última publicación se comprobará
el archivo "Publicar.ods" en busca de cambios

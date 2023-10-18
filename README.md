# Proyecto Python con selenium 

Este proyecto en Python y selenium se centra en interactuar con las urls: https://www.google.es/.es y 
https://es.wikipedia.org. 

Con la url google, se buscará una palabra, en este caso "Automatizacion". 

Luego de la búsqueda hecha en google, selecciona automatizacion en el link wikipedia.

Luego se commprueba el año del primer proceso automático, en este caso, buscará por palabra clave 
"convirtiéndose en el primer proceso industrial completamente automatizado" 

. Para la ejecución de las pruebas automáticas será necesario tener inslado Pyhon.

## Contenido
* [Librerías](#librerías)
* [Ejecutables](#Ejecutables)
* [IDE](#ide)
* [Scripts](#Scripts)
* [Contribuciones](#Contribuciones)

## Librerías
- Selenium

## Ejecutables
- chromedriver. Se descarga de url: https://chromedriver.chromium.org/downloads. Archivo ejecutable se 
coloca en el ordenador, en este caso he colocado el archivo en ruta C:

## IDE
Para este proyecto se ha usado [IntelliJ](https://www.jetbrains.com/idea/)

### Plugins recomendados para intelliJ

- [SonarLint](https://plugins.jetbrains.com/plugin/7973-sonarlint) - Valida código python.

### Ejecución desde IDE de un test en concreto

Colocar el ratón sobre el scenario a ejecutar y click derecho "Run"

### Scripts

La carpeta scripts contiene los ficheros:

- find.py
  - 
  Contiene código python, en el cual se llama al archivo ejecutable chromedriver.exe para que se haga 
interaccion con navegador chrome. También se hace limpieza de chaché para que el navegador se ejecute 
limpio. Se naveha en la url de google, se maximiza la ventana de la web, se hace la llamada del fichero 
que contiene las funciones a ejecutar.Por último se envía instrucción para cerrar navegador.

- data.json
  - 
- Contiene archivo json, el cual contiene la palabra de la búsqueda en google.

- manejo_errores_funciones.py
  - 
  - Contiene código python, el cual tiene una serie de funciones:
    * obtener_texto_desde_archivo()
    * buscar_texto_en_pagina(driver, texto_a_buscar)
    * tomar_screenshot(driver, nombre_archivo)
    * manejar_errores(driver)

- Contribuciones
  - 
- Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, no dudes en crear un pull request.
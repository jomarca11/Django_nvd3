## DESARROLLO DE VISUALIZACION - PEC FINAL

## AUTORES

- Rubén Cumbreño Juan
- Alejandro Sanz García

## DESCRIPCION

Se ha elegido un dataset de vinos de diferentes paises y se ha realizado un análsiis y criba de datos que posteriormente, haciendo uso de las librerias aprendidas en clase, se ha realizado un dashboard con dichos datos.

Link dataset: https://www.kaggle.com/zynicide/wine-reviews/data#winemag-data_first150k.csv


## REQUISITOS

Para ejecutar la parte de análisis(notebook) es necesario:
	- Python 3.X
	- Jupiter Notebook

Para ejecutar la parte web es necesario:
	- En principio deberia funcionar tanto en python 2.X como en 3.X (testeado en 2.7)
	- Navegador Chrome
	- Necesario instalar previamente Django 1.11 o superior (testeado en la 1.11.13)

Para la ejecución web, posicionarse en el path donde se encuentra el "manage.py" y ejecutar el comando para levantar django:
	- python manage.py runserver localhost:1234 (localhost variará dependiendo de donde se ejecute, es la ip de la máquina)
	- Ir al navegador e iniciar con la url "localhost:1234/pecDefinitiva/home/"
Al abrir el navegador comenzará la carga de los datos en nuestras gráficas. Se ha introducido un "loader" para dejar constancia de que los datos siguen cargando. Esta tardanza viene dada por la forma en que se leen, tratan y almacenan los datos.

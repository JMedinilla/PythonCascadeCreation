## Crear un cascade para detectar objetos mediante OpenCV

##### Requisitos previos:

- Linux
- Tiempo libre

Hay que ctualizar y crear el directorio en el que se va a trabajar
```
sudo apt update
sudo apt upgrade
mkdir directorio_de_trabajo
cd directorio_de_trabajo
mkdir pos neg test
```

Y añadir los ficheros `cascadeCreation.py` y `cascadeTesting.py` al directorio, al mismo nivel que `pos`, `neg` y `test`.

Ahora toca instalar el compilador, las librerías y las distintas herramientas de Python necesarias
```
sudo apt install build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev libopencv-dev python-opencv
```

* * *

Hecho esto, procede una breve descripción.

Este proyecto consta de 2 ficheros, `cascadeCreation.py` y `cascadeTesting.py`, que, dando por hecho que se cumplen los requisitos del directorio, crearán los archivos necesarios para empezar a detectar objetos con OpenCV.

Estos requisitos, que se deben cumplir en el directorio de trabajo en el que se almacenen estos ficheros, son:

- Carpeta "pos", que contiene las imágenes positivas del detector
- Carpeta "neg", que contiene las imágenes negativas del detector
- Carpeta "test", que contiene imágenes que incluyen el objeto a detectar, para realizar las pruebas

* * *

Ejecución en consola del fichero `cascadeCreation.py`:

1. Transforma todas las imágenes de la carpeta de positivos, cambiando sus colores a una escala de grises, cambiando sus nombres por unos más apropiados, y unificando su tamaño
2. Crea un fichero con las rutas relativas a todas las imágenes de la carpeta de positivos, añadiendo a cada línea, la cantidad de instancias del objeto que se busca, dónde comienza la posición del objeto, y sus dimensiones
3. Transforma todas las imágenes de la carpeta de negativos, haciendo lo mismo que con las positivas, aunque  el tamaño de estas debe ser mayor que el de las positivas
4. Crea un fichero con las rutas relativas a todas las imágenes de la carpeta de negativos
5. Usando el fichero de rutas a las imágenes positivas, crea un tercer fichero, el cual las va a contener todas, que será necesario a la hora de entrenar el haar cascade
6. Una vez creados todos estos archivos, mostrará el comando que habrá que ejecutar en la consola a continuación para que comience el entrenamiento, proceso con una duración basada en la cantidad de imágenes usadas, su tamaño y el número de fases (más fases, mayor precisión), lo cual puede variar lo que tarde en crear el archivo, desde los 10 segundos, hasta las 3 semanas incluso

Para más información, consultar el código del fichero

* * *

Ejecución en consola del fichero `cascadeTesting.py`:

```
En construcción
```

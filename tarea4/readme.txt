Ruiz López Jorge Antonio - 315119729


-------------------
LEER HASTA EL FINAL
-------------------
La ejecución del programa se explica al final del archivo



Instalación de dependencias:

Instalar Python:
	sudo apt install python3

si no funciona, usar:
	sudo apt-get install python3


Instalar Tkinter:
	sudo apt install python-tk

Instalar PIP:
	sudo apt install python-pip

si no funciona, usar:
	sudo apt install python-pip3


--- Para las instalaciones que requieren el uso de pip usar "pip" o si no lo instala
    para python3 usar la palabra "pip3" y seguir los siguientes pasos de instalación ---


Instalar Pillow:
	sudo pip install pillow

o si no funciona, usar:
	pip install PIL


Instalar OpenCV para la biblioteca cv2:
	sudo apt-get install libopencv-dev
	sudo apt-get install python-opencv


Si no funciona, usar:
	sudo apt-get install libopencv-dev python-opencv


Instalar Numpy:
	sudo pip install numpy


Instalar Pyinstaller:
	sudo pip install pyinstaller



-------------- Ejecución del programa -----------------

(Se incluyen imagenes de prueba.)

Escribir en la terminal:

	python3 filtros.py   si no funciona, escribir: python filtros.py



Generar el ejecutable con PyInstaller (esto creará dos carpetas; dist y build)

Escribir en la terminal:

	pyinstaller --onefile filtros.py --hidden-import='PIL._tkinter_finder'

después para ejecutarlo escribir en terminal:

	./dist/filtros



Si la imagen está en la misma carpeta de los archivos filtros.py, convolucion.py y manejador.py
Al cargar imagen, el nombre de la imagen debe incluir su formato, ej: 'Imagenprueba.jpg' (sin comillas)


Si la imagen está en otro lado, debemos poner la ruta completa, ej: '<Miruta>/<otracarpeta>/Imagenprueba.jpg' (sin comillas y sin < >)


--------------------------
TENER CUIDADO CON LA RUTA.
--------------------------

Ejemplo de problema:

Si escribo: ~/Imágenes/Wallpapers/Sierra.jpg

la ruta no será encontrada pues no es la ruta real, porque '~' es realmente /home/jorge/ (en mi caso)

Entonces debería escribir: /home/jorge/Imágenes/Wallpapers/Sierra.jpg

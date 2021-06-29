Ruiz López Jorge Antonio - 315119729


-------------------
LEER HASTA EL FINAL
-------------------
La ejecución del programa se explica al final del archivo



Instalación de dependencias:

###Instalar Python:
```sh
sudo apt install python3
```

###si no funciona, usar:
```sh
sudo apt-get install python3
```

###Instalar Tkinter:
```sh
sudo apt install python-tk
```

###Instalar PIP:
```sh
sudo apt install python-pip
```

###si no funciona, usar:
```sh
sudo apt install python-pip3
```


--- Para las instalaciones que requieren el uso de pip usar "pip" o si no lo instala
    para python3 usar la palabra "pip3" y seguir los siguientes pasos de instalación ---


###Instalar Pillow:
```sh
sudo pip install pillow
```

###si no funciona, usar:
```sh
pip install PIL
```	
	
###Instalar tqdm para la barra de progreso:
```sh
pip install tqdm
```
	
###si no funciona, usar: 
```sh
pip3 install tqdm
```


###Instalar OpenCV para la biblioteca cv2:
```sh
sudo apt-get install libopencv-dev
sudo apt-get install python-opencv
```


###Si no funciona, usar:
```sh
sudo apt-get install libopencv-dev python-opencv
```

###Instalar Numpy:
```sh
sudo pip install numpy
```

###Instalar Pyinstaller:
```sh
sudo pip install pyinstaller
```


-------------- Ejecución del programa -----------------

(Se incluyen imagenes de prueba.)

Escribir en la terminal:

	python3 Filtros.py   si no funciona, escribir: python Filtros.py



Generar el ejecutable con PyInstaller (esto creará dos carpetas; dist y build)

Escribir en la terminal:

	pyinstaller --onefile Filtros.py --hidden-import='PIL._tkinter_finder'

después para ejecutarlo escribir en terminal:

	./dist/Filtros



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

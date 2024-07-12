PARA UTILIZAR LA PAGINA DEBE SEGUIR LOS SIGUIENTES PASOS

1 - CREE UNA CARPETA Y 
2 - DESCOMPRIMIR PROYECTO
3 - GUARDE EL PROYECTO EN LA CARPETA CREADA
4 - TENER INSTALADO PYTHON
5 - INSTALAR UN ENTORNO VIRTUAL 
6 - INSTALAR LAS LIBRERIAS NECESARIAS PARA INICIAR EL PROYECTO

PARA INSTALAR UN ENTORNO VIRTUAL DEBE SEGUIR LOS SIGUIENTES PASOS:

en un cmd escribir:

pip install virtualenv

luego de haber instalado crear un entorno virtual:

py -m virtualenv venv

o de la siguiente forma:

virtualenv venv

( venv es el nombre del entorno virtual p asignarle el nombre que desee )

una vez configurado el entorno virtual, iniciarlo de la siguiente manera:
en vscode presionar la tecla F1 y escribir: python select interpreter.
al hacer click aparece un recuadro con los entornos virtuales exitentes, eliga el entorno que aparece con nombre que le asigno 

otra forma de hacerlo es ingresar a la carpeta del entorno virtual y abrir el siguiente archivo

Windows:
venv\Scripts\activate.bat

Linux o Mac:
source venv/bin/activate

(asumiendo que el entorno virtual se llama venv, si no use el nombre que le asigno)


PARA INSTALAR LAS DEPENDENCIAS DE DJANGO

para instalar las libreria del proyecto en el entorno virtual, hay un archivo llamado requierements.txt
en el cual se encuentran las librerias que se necesitan para el proyecto.

en la consola de comando o CMD debe escribir lo siguiente:

pip install -r requierements.txt 

se instalara las dependencias necesarias del proyecto para que funcione



luego de haber instalado lo anterior, para ver el proyecto en una pagina debe hacer lo siguiente:

en la consola de comando o CMD debe escribir lo siguiente: 

py manage.py runserver

o si prefiere:

python manage.py runserver

y se abrira el proyecto en el puerto 8000:

http://localhost:8000/
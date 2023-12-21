# Geocoding with Google Maps API and Python
Este proyecto permite obtener coordenadas de latitud y longitud para una lista de direcciones utilizando la API de Geocodificación de Google Maps en Python.

Requisitos
Para usar este proyecto, necesitas tener Python instalado en tu sistema, así como algunas bibliotecas específicas. Además, necesitarás una clave API de Google Maps.

Instalación de Python
Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde python.org.

Instalación de Bibliotecas
Las siguientes bibliotecas de Python son necesarias para ejecutar el script:

requests: Para realizar solicitudes HTTP a la API de Google Maps.
pandas: Para manejar datos en formato tabular.
openpyxl: Para leer y escribir archivos de Excel.
Puedes instalar estas bibliotecas utilizando el siguiente comando:

  #bash
  #Copy code
  #pip install requests pandas openpyxl
  
#Obtención de la Clave API de Google Maps
Para obtener una clave API:

Visita Google Cloud Console.
Crea un nuevo proyecto o selecciona uno existente.
Navega a la sección "Biblioteca", busca la "API de Geocodificación" y actívala.
Ve a "Credenciales" y crea una nueva clave API.
Uso
Para utilizar el script:
  Asegúrate de que tus direcciones estén en un archivo Excel con las direcciones en una columna específica.
  Configura tu clave API en el script.
  Ejecuta el script con Python:

  #bash
  #Copy code
  #python geocode.py
  #Script geocode.py
El script geocode.py lee direcciones de un archivo Excel, consulta la API de Geocodificación de Google Maps para obtener coordenadas y escribe estas coordenadas en el archivo Excel.

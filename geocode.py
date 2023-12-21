import requests
import pandas as pd

# Carga las direcciones desde Excel
df = pd.read_excel('vlc_tienda.xlsx')  # Asegúrate de tener la ruta correcta

# Tu clave API de Google
api_key = ''

# Itera sobre las direcciones y realiza la geocodificación
for index, row in df.iterrows():
    address = row['direccion']  # Asume que tienes una columna 'Direccion'
    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}')
    resp_json = response.json()
    
    if resp_json['status'] == 'OK':
        lat = resp_json['results'][0]['geometry']['location']['lat']
        lng = resp_json['results'][0]['geometry']['location']['lng']
        df.at[index, 'latitude'] = lat
        df.at[index, 'longitude'] = lng

# Sobrescribe el archivo Excel original con los datos actualizados
df.to_excel('vlc_tienda.xlsx', index=False)

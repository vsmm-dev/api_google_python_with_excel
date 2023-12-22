import requests
import pandas as pd

# Carga las direcciones desde Excel
df = pd.read_excel('vlc_tiendas_actualizar.xlsx')  # Asegúrate de tener la ruta correcta

# Tu clave API de Google
api_key = ''

# Contadores para solicitudes exitosas y fallidas
success_count = 0
fail_count = 0

# Itera sobre las direcciones y realiza la geocodificación
for index, row in df.iterrows():
    address = row['address']  # Asume que tienes una columna 'address'
    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}')
    resp_json = response.json()
    
    if resp_json['status'] == 'OK':
        lat = resp_json['results'][0]['geometry']['location']['lat']
        lng = resp_json['results'][0]['geometry']['location']['lng']
        df.at[index, 'latitude'] = lat
        df.at[index, 'longitude'] = lng
        success_count += 1
    else:
        fail_count += 1

# Calcula los porcentajes
total_requests = success_count + fail_count
success_percentage = (success_count / total_requests) * 100 if total_requests > 0 else 0
fail_percentage = (fail_count / total_requests) * 100 if total_requests > 0 else 0

# Muestra los porcentajes
print(f'Porcentaje de éxito: {success_percentage:.2f}%')
print(f'Porcentaje de fallas: {fail_percentage:.2f}%')

# Sobrescribe el archivo Excel original con los datos actualizados
df.to_excel('vlc_tiendas_actualizar.xlsx', index=False)


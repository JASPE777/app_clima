import requests

def obtener_clima_buenos_aires():
    ciudad = "Buenos Aires"
    pais = "AR"  # Código ISO del país, en este caso Argentina
    api_key = "TU_API_KEY"  # Reemplaza 'TU_API_KEY' con tu clave de API de OpenWeatherMap

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    parametros = {
        "q": f"{ciudad},{pais}",
        "appid": api_key,  # Reemplaza 'TU_API_KEY' con tu clave de API de OpenWeatherMap
        "units": "metric"  # Unidades métricas para Celsius, puedes cambiar a "imperial" para Fahrenheit
    }

    try:
        respuesta = requests.get(base_url, params=parametros)
        datos_clima = respuesta.json()

        if respuesta.status_code == 200:
            # Procesar la información obtenida
            temperatura = datos_clima['main']['temp']
            descripcion_clima = datos_clima['weather'][0]['description']
            print(f"El clima en {ciudad} es {descripcion_clima} con una temperatura de {temperatura}°C.")
        else:
            print("Error al obtener los datos. Verifica tu clave de API o la conexión a Internet.")

    except requests.RequestException as e:
        print(f"Error de solicitud: {e}")

# Ejemplo de uso:
obtener_clima_buenos_aires()
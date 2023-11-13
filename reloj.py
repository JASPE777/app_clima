from tkinter import * 
from PIL import Image, ImageTk
import requests
from datetime import datetime
import pytz

def obtener_hora(ciudad):
    zona_horaria = pytz.timezone(ciudad)
    hora_actual = datetime.now(zona_horaria).strftime("%H:%M:%S")
    return hora_actual

def actualizar_reloj():
    hora_ciudad = obtener_hora(zone)
    reloj.config(text=f"{nombre_ciudad}: {hora_ciudad}")
    reloj.after(1000, actualizar_reloj)

def change_picture(route='./countries_pictures/kiev.jpg'):
    img = Image.open(route)
    bg_picture = ImageTk.PhotoImage(img)
    bg_label.configure(image=bg_picture)
    bg_label.image = bg_picture

def weather(city, country): 
    api_key = "b27b082ff0d604c9a9802f2efa405057"  
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    parametros = {
        "q": f"{city},{country}",
        "appid": api_key,  
        "units": "metric"  
    }

    try:
        respuesta = requests.get(base_url, params=parametros)
        info_weather = respuesta.json()

        if respuesta.status_code == 200:
            temperature = info_weather['main']['temp']
            description_weather = info_weather['weather'][0]['description']
            t_and_w.config(text=f"Weather: {description_weather}\nTemperature: {temperature}°C.")
        else:
            t_and_w.config(text="Error al obtener los datos.")
    except requests.RequestException as e:
        print(f"Error de solicitud: {e}")

# Configuración inicial
root = Tk()
root.title("APP CLIMA")
root.resizable(0, 0)
root.geometry('800x820')
root.iconbitmap(".\icon\icono.ico")
root.config(bg="black")

bg_frame = Frame(root, width=500, height=500) 
bg_frame.pack()
bg_picture = None
bg_label = Label(bg_frame, image=bg_picture, width=500, height=500)
bg_label.pack()

reloj = Label(bg_frame, font=("Roboto", 20), bg="black", fg="white")
reloj.pack()
zone = "Europe/Kiev"

t_and_w = Label(bg_frame, font=("Roboto", 20), bg="black", fg="white")
t_and_w.pack()

menu_countries = Frame(bg_frame, width=500, height=20)
menu_countries.pack()

countries_info = [
    ("./countries_buttons/amsterdam.png", "Amsterdam", "NL"),
    ("./countries_buttons/barcelona.png", "Barcelona", "ES"),
    ("./countries_buttons/berlin.png", "Berlin", "DE"),
    ("./countries_buttons/buenos_aires.png", "Buenos Aires", "AR"),
    ("./countries_buttons/kiev.png", "Kyiv", "UA"),
    ("./countries_buttons/paris.png", "Paris", "FR")
]

def button_command(img_path, city, country):
    change_picture(img_path)
    weather(city, country)
    global zone, nombre_ciudad
    zone = f"Europe/{city.split()[0]}"
    nombre_ciudad = city
    actualizar_reloj()

buttons = []

for i, (img_path, city, country) in enumerate(countries_info, start=1):
    img = ImageTk.PhotoImage((Image.open(img_path)).resize((32, 21)))
    button = Button(menu_countries, image=img, command=lambda c=city, co=country, p=img_path: button_command(p, c, co))
    button.grid(row=1, column=i, padx=5)
    buttons.append((img, button))

# Inicio del bucle principal
change_picture()
weather("Kyiv", "UA")
zone = "Europe/Kiev"
nombre_ciudad = "Kiev"
actualizar_reloj()
root.mainloop()
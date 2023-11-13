from tkinter import * 
from PIL import Image, ImageTk
import requests
from datetime import datetime
import pytz






def hour(city, name):


    # Get the current time for the specified city
    global zone, name_zone

    # Update the value of the variables
    zone = city
    name_zone = name

    # Get city time
    hour_zone = pytz.timezone(zone)
    hour_zone = datetime.now(hour_zone).strftime("%H:%M:%S")
    
    # Update the label with the new time
    reloj.config(text=f"{name}: {hour_zone}")
    
    #---Update Clock
    reloj.after(1000, lambda: hour(zone, name_zone))




def change_picture(route='./countries_pictures/kiev.jpg'):
    global bg_picture

    img = Image.open(route)
    bg_picture = ImageTk.PhotoImage(img)
    bg_label.configure(image=bg_picture)
    # bg_label.image = bg_picture




def weather(city, country): 
    
    api_key = "b27b082ff0d604c9a9802f2efa405057"  
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    parameters = {
        "q": f"{city},{country}",
        "appid": api_key,  
        "units": "metric"  
    }

    try:
        respuesta = requests.get(base_url, params=parameters)
        info_weather = respuesta.json()

        if respuesta.status_code == 200:
            # Procesar la información obtenida
            temperature = info_weather['main']['temp']
            description_weather = info_weather['weather'][0]['description']
            t_and_w.config(text=f"Weather: {description_weather}\nTemperature: {temperature}°C.")
        else:
            t_and_w.config(text=f"Error obtaining data.")
        

    except requests.RequestException as e:
        print(f"Request error: {e}")



#----------------------------Configure the Root-----------------------------

root= Tk()
root.title("APP CLIMA")
root.resizable(0, 0)
root.geometry('800x820')
root.iconbitmap(".\icon\icono.ico")
root.config(bg="black")

#----------------------------Background Frame-------------------------------

bg_frame = Frame(root, width=500, height=500) 
bg_frame.pack()
bg_picture = None
bg_label = Label(bg_frame, image=bg_picture, width=500, height=500)
bg_label.pack()

#--------------------------------Reloj--------------------------------------

reloj = Label(bg_frame, font=("Roboto", 20), bg="black", fg="white")
reloj.pack()
zone = "Europe/Kiev"
name_zone = "Kiev"

#------------------------Temperature & Wheather-----------------------------


t_and_w = Label(bg_frame, font=("Roboto", 20), bg="black", fg="white")
t_and_w.pack()


#----------------------------Menu Countries--------------------------------- 

menu_countries = Frame(bg_frame, width=500, height=20)
menu_countries.pack()


#----Country Buttons----



#--Button--1

button1_picture = ImageTk.PhotoImage((Image.open('./countries_buttons/amsterdam.ico')).resize((32, 21)))
button1 = Button(menu_countries, image=button1_picture, command=lambda: [change_picture('./countries_pictures/amsterdam.jpg'), weather("Amsterdam", "NL"), hour(city="Europe/Amsterdam", name="Amsterdam")])
button1.grid(row=1, column=1)

#--Button--2

button2_picture = ImageTk.PhotoImage((Image.open('./countries_buttons/barcelona.ico')).resize((32, 21)))
button2 = Button(menu_countries, image=button2_picture, command=lambda: [change_picture('./countries_pictures/barcelona.jpg'), weather("Barcelona", "ES"), hour(city="Europe/Madrid", name="Barcelona")])
button2.grid(row=1, column=2)

#--Button--3

button3_picture = ImageTk.PhotoImage((Image.open('./countries_buttons/berlin.ico')).resize((32, 21)))
button3 = Button(menu_countries, image=button3_picture, command=lambda: [change_picture('./countries_pictures/berlin.jpg'), weather("Berlin", "DE"), hour(city="Europe/Berlin", name="Berlin") ])
button3.grid(row=1, column=3)

#--Button--4

button4_picture = ImageTk.PhotoImage((Image.open('./countries_buttons/buenos_aires.ico')).resize((32, 21)))
button4 = Button(menu_countries, image=button4_picture, command=lambda: [change_picture('./countries_pictures/buenos_aires.jpg'), weather("Buenos Aires", "AR"), hour(city="America/Argentina/Buenos_Aires", name="Buenos Aires")])
button4.grid(row=1, column=4)

#--Button--5

button5_picture = ImageTk.PhotoImage((Image.open('./countries_buttons/kiev.ico')).resize((32, 21)))
button5 = Button(menu_countries, image=button5_picture, command=lambda: [change_picture('./countries_pictures/kiev.jpg'), weather("Kyiv", "UA"), hour(city="Europe/Kiev", name="Kiev") ])
button5.grid(row=1, column=5)

#--Button--6

button6_picture = ImageTk.PhotoImage((Image.open('./countries_buttons/paris.ico')).resize((32, 21)))
button6 = Button(menu_countries, image=button6_picture, command=lambda: [change_picture('./countries_pictures/paris.jpg'), weather("Paris", "FR"), hour(city="Europe/Paris", name="Paris") ])
button6.grid(row=1, column=6)






change_picture()
weather("Kyiv", "UA")
hour(zone, "Kiev")
root.mainloop()


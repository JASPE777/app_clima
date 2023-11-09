from tkinter import * 
from PIL import Image, ImageTk


def hacer_algo():
    pass


#----------------------------Configure the Root-----------------------------

root= Tk()
root.title("APP CLIMA")
root.resizable(0, 0)
root.geometry('800x820')
root.iconbitmap(".\icon\icono.ico")
root.config(bg="black")

#----------------------------Our background Frame---------------------------

bg_frame = Frame(root, width=800, height=800) 
bg_frame.pack()
bg_picture = ImageTk.PhotoImage(Image.open('./countries_pictures/kiev.jpg')) 
bg_label = Label(bg_frame, image=bg_picture)
bg_label.pack()


#----------------------------Menu Countries--------------------------------- 

menu_countries = Frame(bg_frame, width=500, height=20)
menu_countries.pack()

#----Country Buttons----


#--Button--1

button1_picture = ImageTk.PhotoImage((Image.open('./countries_buttons/amsterdam.png')).resize((32, 21)))
button1 = Button(menu_countries, image=button1_picture, command=hacer_algo)
button1.grid(row=1, column=1)

#--Button--2

button2_picture = ImageTk.PhotoImage((Image.open('./countries_buttons/barcelona.png')).resize((32, 21)))
button2 = Button(menu_countries, image=button2_picture, command=hacer_algo)
button2.grid(row=1, column=2)

#--Button--3

button3_picture = ImageTk.PhotoImage((Image.open('./countries_buttons/berlin.png')).resize((32, 21)))
button3 = Button(menu_countries, image=button3_picture, command=hacer_algo)
button3.grid(row=1, column=3)

#--Button--4

button4_picture = ImageTk.PhotoImage((Image.open('./countries_buttons/buenos_aires.png')).resize((32, 21)))
button4 = Button(menu_countries, image=button4_picture, command=hacer_algo)
button4.grid(row=1, column=4)

#--Button--5

button5_picture = ImageTk.PhotoImage((Image.open('./countries_buttons/kiev.png')).resize((32, 21)))
button5 = Button(menu_countries, image=button5_picture, command=hacer_algo)
button5.grid(row=1, column=5)

#--Button--6

button6_picture = ImageTk.PhotoImage((Image.open('./countries_buttons/paris.png')).resize((32, 21)))
button6 = Button(menu_countries, image=button6_picture, command=hacer_algo)
button6.grid(row=1, column=6)





root.mainloop()


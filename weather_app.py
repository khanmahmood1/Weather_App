from tkinter import *
from tkinter import ttk
import requests

def data_get():
  city = city_name.get()
  data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b5516418b8f8c4433b4a5b293ca3e124").json()
  weath_label1.config(text=data["weather"][0]["main"])
  desc_label1.config(text=data["weather"][0]["description"])
  temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
  pres_label1.config(text=data["main"]["pressure"])




 
win = Tk()
win.title("WEATHER APP")
win.config(bg = "blue")
win.geometry("500x570")


#title name of the project
name_label = Label(win,text="My WEATHER APP",font=("Time New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

#combo box of India stringVar
city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="My WEATHER APP",values=list_name,font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)





weath_label = Label(win,text="Weather Climate",font=("Time New Roman",20,"bold"))
weath_label.place(x=25,y=260,height=50,width=220)
weath_label1 = Label(win,text="",font=("Time New Roman",20,"bold"))
weath_label1.place(x=255,y=260,height=50,width=220)




desc_label = Label(win,text="Weather Description",font=("Time New Roman",16,"bold"))
desc_label.place(x=25,y=330,height=50,width=220)
desc_label1 = Label(win,text="",font=("Time New Roman",16,"bold"))
desc_label1.place(x=255,y=330,height=50,width=220)




temp_label = Label(win,text="Temperature",font=("Time New Roman",20,"bold"))
temp_label.place(x=25,y=400,height=50,width=220)
temp_label1 = Label(win,text="",font=("Time New Roman",20,"bold"))
temp_label1.place(x=255,y=400,height=50,width=220)




pres_label = Label(win,text="Pressure",font=("Time New Roman",20,"bold"))
pres_label.place(x=25,y=470,height=50,width=220)
pres_label1 = Label(win,text="",font=("Time New Roman",20,"bold"))
pres_label1.place(x=255,y=470,height=50,width=220)




done_button = Button(win,text="Done",font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)


win.mainloop()
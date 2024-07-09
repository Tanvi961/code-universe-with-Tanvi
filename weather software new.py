from tkinter import*
import requests
root=Tk()
City=input("enter city:")
api_key="962bec67fb909166235c902d72278e2b"
url="http://api.openweathermap.org/data/2.5/weather?"
complete_url= url + "appid=" + api_key + "&q=" + City
res=requests.get(complete_url)
def get_weather():
    city=City.get()
    data=res.json()
    temperature=data['main']['temp']
    pressure=data['main']['pressure']
    humidity=data['main']['humidity']
    tempmin=data['main']['temp_min']
    tempmax=data['main']['temp_max']
    wind=data['wind']['speed']
    sunrise=data['sys']['sunrise']
    sunset=data['sys']['sunset']
    longtitude=data['coord']['lon']
    latitude=data['coord']['lat']
    country=data['sys']['country']
    description=data['weather'][0]['description']
    
    t.insert(0,temperature)
    p.insert(0,pressure)
    h.insert(0,humidity)
    temp_min.insert(0,tempmin)
    temp_max.insert(0,tempmax)
    speed.insert(0,wind)
    s1.insert(0,sunrise)
    s2.insert(0,sunset)
    l1.insert(0,longtitude)
    l2.insert(0,latitude)
    c.insert(0,country)
    d.insert(0,description)

City=Label(root,text="City").grid(row=1)
City=Entry(root)
City.grid(row=1,column=1,ipady=10,stick="w")
t=Label(root,text="Temperature").grid(row=2)
t=Entry(root)
t.grid(row=2,column=1,ipady=10,stick="w")
p=Label(root,text="Pressure").grid(row=3)
p=Entry(root)
p.grid(row=3,column=1,ipady=10,stick="w")
h=Label(root,text="Humidity").grid(row=4)
h=Entry(root)
h.grid(row=4,column=1,ipady=10,stick="w")
temp_min=Label(root,text="Min Temp").grid(row=5)
temp_min=Entry(root)
temp_min.grid(row=5,column=1,ipady=10,stick="w")
temp_max=Label(root,text="max Temp").grid(row=6)
temp_max=Entry(root)
temp_max.grid(row=6,column=1,ipady=10,stick="w")
speed=Label(root,text="Wind Speed").grid(row=7)
speed=Entry(root)
speed.grid(row=7,column=1,ipady=10,stick="w")
s1=Label(root,text="Sunrise").grid(row=8)
s1=Entry(root)
s1.grid(row=8,column=1,ipady=10,stick="w")
s2=Label(root,text="Sunset").grid(row=9)
s2=Entry(root)
s2.grid(row=9,column=1,ipady=10,stick="w")
l1=Label(root,text="longtitude").grid(row=10)
l1=Entry(root)
l1.grid(row=10,column=1,ipady=10,stick="w")
l2=Label(root,text="latitude").grid(row=11)
l2=Entry(root)
l2.grid(row=11,column=1,ipady=10,stick="w")
c=Label(root,text="Country").grid(row=12)
c=Entry(root)
c.grid(row=12,column=1,ipady=10,stick="w")
d=Label(root,text="description").grid(row=13)
d=Entry(root)
d.grid(row=13,column=1,ipady=10,stick="w")

button=Button(root,text='Result',command=get_weather).grid(row=1,column=2,sticky="W",pady=4)

root.mainloop()

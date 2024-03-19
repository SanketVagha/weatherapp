from tkinter import *
import requests
 
 
root =Tk()
root.geometry("1200x1200")
root.resizable(0,0)

root.title("Weather App")

city_value = StringVar()
 
def showWeather():
    api_key = "6f6480b2de4c6f14dc731224524c39a4"
 
    city_name = city_value.get()
 
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
 
    response = requests.get(weather_url)
 
    weather_info = response.json()
 
    if weather_info['cod'] == 200:
        kelvin = 273
 
        global templable
        global citylable
        global tempimagelable
        global humiditylabel
        global wind_speedlabel
        global errorlabel

        weather = weather_info['weather'][0]['main']

        if 'templable' in globals():
            templable.destroy()
            tempimagelable.destroy()
            humiditylabel.destroy()
            wind_speedlabel.destroy()
            citylable.destroy()

        if 'errorlabel' in globals():
            errorlabel.destroy()
        
        city = weather_info['name']
        citylable = Label(text=f"City : {city}", font=('arial',28,'bold'))
        citylable.pack(pady=20)    

        temp = int(weather_info['main']['temp'] - kelvin)
        templable = Label(text=f"Temperature :   {round(temp,2)}°c", font=('arial',25,'bold'))
        templable.pack(pady=20)        
        
        tempimagelable =  Label(text= f"Weather :  {weather}", font=('arial',18,'bold'))
        tempimagelable.pack(pady= 20)

        

        humidity = weather_info['main']['humidity']

        humiditylabel = Label(text=f"Humidity : {round(humidity,2)} %", font= ('arial',18,'bold'))
        humiditylabel.pack(pady= 20)

        wind_speed = weather_info['wind']['speed'] * 3.6
        wind_speedlabel = Label(text=f"Wind Speed : {round(wind_speed,2)} km/h", font= ('arial',18,'bold'))
        wind_speedlabel.pack(pady= 20)

    else:

        if 'templable' in globals():
            tempimagelable.destroy()
            templable.destroy()
            humiditylabel.destroy()
            wind_speedlabel.destroy()
            citylable.destroy()

        if 'errorlable' in globals():
            errorlabel.destroy()
        
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
        errorlabel = Label(text= weather, font= ('arial',18,'bold'))
        errorlabel.pack(pady=50)
 
  
 
city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10)
 
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold').pack()
 
 
Button(root, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
 
weather_now = Label(root, text = "The Weather is:", font = 'arial 12 bold').pack(pady=10)
 
def on_enter(event = None):
    showWeather()

root.bind('<Return>', on_enter)

root.mainloop()

import tkinter as tk
from PIL import Image,ImageTk # type: ignore
import PIL # type: ignore
import requests


root = tk.Tk()

root.title('Weather Application')
root.geometry('600x500')

#1d1e12e59d84bdc4a1e0b7c1da6a97b6     key

def format_response(weather):
    try:
        city = weather['name']
        condition = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City:%s\nCondition:%s\nTemprature:%s'%(city,condition,temp)
    except:
        final_str='There was a problem in retrieving that information'
    return final_str

def get_weather(city):
    weather_key = '1d1e12e59d84bdc4a1e0b7c1da6a97b6'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':weather_key, 'q':city}
    response = requests.get(url,params)
    weather = response.json()
    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp'])

    result['text']=format_response(weather)



img = Image.open('C:/Users/ansha/OneDrive/Desktop/Projects/Weather App/bg5.jpg')
img = img.resize((600,500),PIL.Image.Resampling.LANCZOS)
img_photo = ImageTk.PhotoImage(img)

bg_lbl = tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)

heading_title = tk.Label(bg_lbl,text='Earth Including Over 200,000 Cities',fg='sky blue',bg='white',font=('times new roman',18,'bold'))
heading_title.place(x=120,y=18)

frame_one = tk.Frame(bg_lbl,bg='#42c2f4',bd=5)
frame_one.place(x=80,y=60,width=450,height=50)

txt_box = tk.Entry(frame_one,font=('times new roman',25),width=17)
txt_box.grid(row=0,column=0,sticky='w')

btn = tk.Button(frame_one,text='Get Weather',fg='green',font=('times new roman',16,'italic'), command=lambda : get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=10)

frame_two = tk.Frame(bg_lbl,bg='#42c2f4',bd=5)
frame_two.place(x=80,y=130,width=450,height=300)

result = tk.Label(frame_two,font=40,bg='white',justify='left',anchor='nw')
result.place(relwidth=1,relheight=1)






root.mainloop()


from tkinter import Tk, ttk
from tkinter import *

from PIL import Image, ImageTk

import requests
import json

#screen
root = Tk()
root.title("Currency GLobal Money Converter")
root.geometry("800x450")
root.configure(bg='#FFFFFF')
#root.resizable()

#color
color1="#FFFFFF" #WHITE
color2="#333333" #BLACK
color3="#4c6826" #GREEN

#frames
top = Frame(root,width=350,height=75,bg=color3)
top.grid(row=0, column=0)

main = Frame(root,width=350,height=300,bg=color1)
main.grid(row=1, column=0)

right = Frame(root,width=350,height=75,bg=color2)
right.grid(row=0, column=2)

#connect to api
def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    #currency
    currency_1 = box1.get()
    currency_2 = box2.get()
    amount = value.get()

    querystring = {"from":currency_1,"to":currency_2,"amount":amount}
    

    if currency_2 =='AED':
        symbol = 'د. إ'
    elif currency_2 == 'USD':
        symbol= '$'
    elif currency_2 =='EUR':
        symbol = '€'
    elif currency_2 =='GBP':
        symbol = '£'
    elif currency_2 =='PESO':
        symbol = '₱'
    elif currency_2 =='JPY':
        symbol = '¥'
    

    headers = {
	  "X-RapidAPI-Key": "d41b054c73msh562ffc028f3c701p138de1jsn777fe07e3558",
	  "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    formatted = symbol + " {:,.2f}".format(converted_amount)


    result['text'] = formatted

    print(converted_amount, formatted)
    


#top frame
icon = Image.open('money-exchange.png')
icon = icon.resize((40,40))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top, image = icon, compound=LEFT, text = "Currency Converter", height=5, padx=40, pady=30, anchor=CENTER, font=('Roboto',15), bg=color3, fg=color1)
app_name.place(x=0,y=0)

#right frame
right_name =Label(top, compound=RIGHT, text = "Currency Exchange Today ", height=5, padx=40, pady=30, anchor=CENTER, font=('Roboto',15), bg=color3, fg=color1)
right_name.place(x=300,y=0)


#main frame
result = Label(root,text = " ", width= 16,height=2, padx=13, pady=7,relief="solid", anchor=CENTER, font=('Roboto',17),bg=color1, fg=color2)
result.place(x=45,y=350)

#right frame fo forex charts


#currency- add more currency
currency = ['AED', 'USD', 'EUR', 'GBP', 'PESO', 'JPY']

#from
exchange_label =  Label(top, width= 8,height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Roboto',10), bg=color1, fg=color1)
exchange_label.place(x=40, y=150)

#the choices from what do you want to exchange
box1 = ttk.Combobox(main, width=8, justify=CENTER, font=('Roboto 12 bold'))
box1['values'] = (currency)
box1.place(x=45, y=40)

#arrow
image = Image.open('arrow.png')
image = image.resize((40,20))
image = ImageTk.PhotoImage(image)
arrow = Label(main, image=image, bg=color1)
arrow.place(x=146, y=40)

#to
exchangeto_label =  Label(top, width= 8,height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Roboto',10), bg=color1, fg=color1)
exchangeto_label.place(x=80, y=150)

#the choices from what do you want to exchange part 2
box2 = ttk.Combobox(main, width=8, justify=CENTER, font=('Roboto 12 bold'))
box2['values'] = (currency)
box2.place(x=200, y=40)

#the amount
value_text = Label(root, text="Amount", justify=LEFT, font=("Roboto 7 bold"),fg=color2, bg=color1)
value = Entry(root, text="Amount", width=17, justify=CENTER, font=("Roboto 13 bold"),fg=color2, relief=SOLID)
value_text.place(x=85,y=175)
value.place(x=85,y=190)

#button/convert now
button = Button(main,text="Convert now", width=19, padx=5, height=1, bg=color3, fg=color1, font=("Roboto 12 bold"),command=convert)
button.place(x=55, y=190)

root.mainloop()


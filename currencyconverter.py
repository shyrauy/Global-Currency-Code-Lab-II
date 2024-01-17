from tkinter import Tk, ttk
from tkinter import *

from PIL import Image, ImageTk

import requests
import json

#screen
root = Tk()
root.title("Currency GLobal Money Converter")
root.geometry("700x450")
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
    first_currency = box1.get()
    second_currency = box2.get()
    amount = value.get()

    querystring = {"from":first_currency,"to":second_currency,"amount":amount}
    

    if second_currency =='AED':
        symbol = 'د. إ'
    elif second_currency == 'USD':
        symbol= '$'
    elif second_currency =='EUR':
        symbol = '€'
    elif second_currency =='GBP':
        symbol = '£'
    elif second_currency =='PHP':
        symbol = '₱'
    elif second_currency =='JPY':
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
logo = Image.open('money-exchange.png')
logo = logo.resize((40,40))
logo = ImageTk.PhotoImage(logo)
platform_name = Label(top, image = logo, compound=LEFT, text = "Currency Converter", height=5, padx=35, pady=30, anchor=CENTER, font=('Roboto bold',16), bg=color3, fg=color1)
platform_name.place(x=0,y=0)

#right frame
#Not YET WORKING!!!
#right_name =Label(main, compound=RIGHT, text = "Currency Exchange Today ", height=5, padx=40, pady=30, anchor=CENTER, font=('Roboto bold',15), bg=color2, fg=color1)
#right_name.place(x=300,y=1)


with open('rate.txt') as file_handler:
    contents = file_handler.read()
    content_label = Label(root, height=15, width=20,text=contents, font=('Roboto',15),bg=color1,fg=color2 ) 
    content_label.place(x=400, y=80)



#currency- add more currency
currency = ['AED', 'USD', 'EUR', 'GBP', 'PHP', 'JPY']

#from
exchange_label =  Label(top, width= 8,height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Roboto',10), bg=color1, fg=color1)
exchange_label.place(x=40, y=150)

#the choices from what do you want to exchange
box1 = ttk.Combobox(main, width=8, justify=CENTER, font=('Roboto 12 bold'))
box1['values'] = (currency)
box1.place(x=45, y=40)

#arrow
image = Image.open('arrow.png')
image = image.resize((38,15))
image = ImageTk.PhotoImage(image)
arrow = Label(main, image=image, bg=color1)
arrow.place(x=149, y=42)

#to
exchangeto_label =  Label(main, width= 8,height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Roboto',10), bg=color1, fg=color1)
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

#result
result = Label(root,text = " ", width= 16,height=2, padx=13, pady=7,relief="solid", anchor=CENTER, font=('Roboto',17),bg=color1, fg=color2)
result.place(x=45,y=350)


root.mainloop()


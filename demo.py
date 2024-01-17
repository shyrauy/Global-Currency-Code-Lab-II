import requests
import json

url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

#currency
currency_1 = "AED",# "USD", "EURO", "GBP", "PESO", "YEN"
currency_2 =  "USD" #"AED", "USD", "EURO", "GBP", "PESO", 
amount = "1000"

querystring = {"from":currency_1,"to":currency_2,"amount":amount}

headers = {
	"X-RapidAPI-Key": "d41b054c73msh562ffc028f3c701p138de1jsn777fe07e3558",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)
converted_amount = data["result"]["convertedAmount"]
formatted = "{:,.2f}".format(converted_amount)

print(converted_amount, formatted)

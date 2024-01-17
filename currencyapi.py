import requests
import json

url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

#currency
first_currency = "AED", "USD", "EUR", "GBP", "PHP", "YEN"
second_currency =  "GBP" ,"AED", "USD", "EUR", "PHP", "YEN"
amount = "1000"

querystring = {"from":first_currency,"to":second_currency,"amount":amount}

headers = {
	"X-RapidAPI-Key": "d41b054c73msh562ffc028f3c701p138de1jsn777fe07e3558",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)
converted_amount = data["result"]["convertedAmount"]
formatted = "{:,.2f}".format(converted_amount)

print(converted_amount, formatted)

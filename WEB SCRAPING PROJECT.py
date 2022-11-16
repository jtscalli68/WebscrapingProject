
from urllib.request import urlopen
from bs4 import BeautifulSoup
# import openpyxl as xl
# from openpyxl.styles import Font

import random
import keys2
from twilio.rest import Client

client = Client(keys2.accountSID, keys2.authToken)

TwilioNumber = "+12543322359"
myCellphone = "+15086483007"




#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://coinmarketcap.com/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title


tr = soup.findAll('tr')

print()
print(f'******* {title.text} *******')
print()

for x in range(1,6):
    td = tr[x].findAll('td')
    caret = tr[x].findAll('span', class_='icon-Caret-down')
    if td: 
        #Infromation 
        rank = td[1].text
        name = td[2].text
        price = td[3].text
        per_chg = td[5].text

        #Formatting 
        namestrip = name.split(str(rank), 1 )
        name = namestrip[0]
        symbol = namestrip[1]
    
        price_calc = price.lstrip('$')
        price_calc = float(price_calc.replace(',',''))

        per_chg_calc = float(per_chg.rstrip('%'))

        #Calculations
        if caret: 
            per_chg_calc = per_chg_calc
        else: 
            per_chg_calc = (-1 * per_chg_calc)

        prev_price = (price_calc) * (1 - per_chg_calc/100)
        prev_price = format(prev_price,'.2f')
        #output
        print(f'Name: {name}') 
        print(f'Symbol: {symbol}')
        print(f'Price: {price}')  
        print(f'Percent Change: {str(per_chg_calc)}%')
        print(f'Previos Price: ${prev_price}')
        print()

        if name == 'Bitcoin':
            if price_calc < 40000:
                textmsg = client.messages.create(to=myCellphone, from_=TwilioNumber, body= 'Bitcoin price has fallen below $40,000')
            else:
                pass
        else: 
            pass

        if name == 'Ethereum':
            if price_calc < 3000:
                textmsg = client.messages.create(to=myCellphone, from_=TwilioNumber, body= 'Ethereum price has fallen below $3,000')
            else:
                pass
        else: 
            pass
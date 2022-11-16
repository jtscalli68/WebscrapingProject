from urllib import request
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup




##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"


# url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/'
url = 'https://www.webull.com/quote/us/gainers'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')            #this last few lines will almost always be the same, you cna copy and paste this each time 

title = soup.title

# print(title.text)


tablecells = soup.findAll("div",attrs={'class':'table-cell'})

# print('No.:         ',tablecells[0].text)
# print('Syboml/Name: ', tablecells[1].text)
# print('% Chg in 1 D:', tablecells[3].text)
# print('Last price:  ', tablecells[4].text)
# print('High:        ', tablecells[5].text)
# print('Low:         ',tablecells[6].text)
# print('Volumne:     ', tablecells[7].text)
# print('% Range:     ', tablecells[8].text)
# print('P/E          ', tablecells[9].text)
# print('Market Cap:  ',tablecells[10].text)

#or

for cell in tablecells[:7]:
    print(cell.text)

counter = 1 

for x in range(5):
    name = tablecells[counter].text
    change = tablecells[counter+2].text
    high = float(tablecells[counter+4].text)
    low = float(tablecells[counter+5].text)

    calc_change = round(((high - low)/low) * 100)

    print(name)
    print(f"%change on webpage: {change}")
    print(f"High: {high}")
    print(f"low: {low}")
    print(f"Calculated change %: {calc_change}")
    print()
    print()
    counter += 11









#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")


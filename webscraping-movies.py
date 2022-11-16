
from urllib.request import urlopen
from bs4 import BeautifulSoup
# import openpyxl as xl
# from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print()
print(title.text)

table = soup.findAll("table")
movietable = table[0]

movie_rows = movietable.findAll('tr')


for x in range(1,6):
    td = movie_rows[x].findAll('td')
    rank = td[0].text
    release = td[1].text
    
    tot_gross = td[5].text
    distributor = td[9].text
    print(rank, release, tot_gross, distributor)
    print()
    input()

    
    
# for rec in tr: 
#     td = rec.findAll('td')
#     for rec in td:
#         if td: 
#             rank = td[0].text
#             release = td[1].text
#             tot_gross = td[5].text
#             distributor = td[9].text
#             print(rank, release, tot_gross, distributor)


#     movie_rows = 


            
            
    

# print(rank, release, tot_gross, distributor)
# # print(rank, release, tot_gross, distributor)



#rank, release, gros, distributor





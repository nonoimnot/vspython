from bs4 import BeautifulSoup
import urllib.request
import csv

# specify the url
urlpage =  'http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/'

# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(urlpage)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')
print(soup)

#find results within table
table = soup.find('table', attrs={'class': 'tableSorter'})
print(table)
#results = table.find_all('tr')

#print('Number of results', len(results))
#print(results)


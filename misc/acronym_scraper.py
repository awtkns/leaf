import requests
from bs4 import BeautifulSoup

acronym = 'SFU'
page = requests.get('https://www.acronymfinder.com/{}.html'.format(acronym))
soup = BeautifulSoup(page.content, 'html.parser')

# Find the first table entry for the results
td = soup.find('td', {'class':'result-list__body__meaning'})

# Remove outer table entry tag
stringWithoutTd = str(td).split("\">",1)[1]

# Remove href tag if it exists
if 'href' in stringWithoutTd:
	stringWithoutTd = stringWithoutTd.split("\">",1)[1]
	
finalString = stringWithoutTd.split("<",1)[0]

# Remove extra brackets if it exists
if '(' in finalString:
	finalString = finalString.split("(",1)[0]

print(finalString)
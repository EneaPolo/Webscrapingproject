import requests
from bs4 import BeautifulSoup
import json

# URL i faqes për scraping
url = 'https://www.bbc.com/news'

# Kërko për faqen dhe merr HTML-në
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Nxjerr titujt e artikujve (për shembull të gjitha elementet <h3> që përdoren për tituj)
titles = soup.find_all('h3')

# Ruaj titujt në një listë
data = [{'title': title.get_text()} for title in titles]

# Ruaj të dhënat në një skedar JSON
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Të dhënat u ruajtën me sukses në data.json.")
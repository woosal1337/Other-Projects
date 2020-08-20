import bs4 as BeautifulSoup
import requests
response = requests.get('https://www.python.org')

soup = BeautifulSoup(response.content,'html5lib')

text = soup.get_text(strip=True)

print(text)

import requests
from bs4 import BeautifulSoup


r = requests.get("http://www.pyclass.com/example.html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
content = r.content

soup = BeautifulSoup(content,"html.parser")

cities = soup.find_all("div", {"class": "cities"}) 

# h2 = cities[0].find_all("h2")

# print(h2)

for item in cities:
    print(item.find_all("h2"))
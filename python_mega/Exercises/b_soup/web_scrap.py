import requests
from bs4 import BeautifulSoup


r = requests.get("http://www.pyclass.com/example.html", headers={
                 'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

content = r.content

soup = BeautifulSoup(content, "html.parser")

all_div = soup.find_all("div", {"class": "cities"})

for item in all_div:
    print(item.find_all("p")[0].text)

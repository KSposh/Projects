import requests
import pandas
from bs4 import BeautifulSoup

"""
Scrap website
"""

def page_scraper():
    r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={
                    'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    soup = BeautifulSoup(r.content, "html.parser")

    all_div = soup.find_all("div", {"class": "propertyRow"})

    l =[]
    for item in all_div:
        d = {}
        d['Address'] = item.find_all("span", {"class": "propAddressCollapse"})[0].text
        d['Locality'] = item.find_all("span", {"class": "propAddressCollapse"})[1].text
        d['Price'] = item.find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ", "")
        try:
            d['Beds'] = item.find("span", {"class": "infoBed"}).find("b").text
        except:
            d['Beds'] = None
        try:
            d['Area'] = item.find("span", {"class": "infoSqFt"}).find("b").text
        except:
            d['Area'] = None
        try:
            d['Full Baths'] = item.find("span", {"class": "infoValueFullBath"}).find("b").text
        except:
            d['Full Baths'] = None
        try:
            d['Half Baths'] = item.find("span", {"class": "infoValueHalfBath"}).find("b").text
        except:
            d['Half Baths'] = None

        for column in item.find_all("div", {"class": "columnGroup"}):
            for f_group, f_name in zip(column.find_all("span", {"class": "featureGroup"}), column.find_all("span", {"class": "featureName"})):
                if "Lot Size" in f_group.text:
                    d['Lot Size'] = f_name.text
        l.append(d)

    df = pandas.DataFrame(l)
    df.to_csv("Output.csv")

base_url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s=%s.html"

for page in range(0, 30, 10):
    print(base_url % str(page))
    r = requests.get(base_url % str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    print(soup.prettify())

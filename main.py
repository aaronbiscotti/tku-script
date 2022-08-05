import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import tldextract
import re
import pandas as pd
from lxml.html import fromstring
from itertools import cycle
import traceback
from requests_ip_rotator import ApiGateway, EXTRA_REGIONS
from googlesearch import search




websites_data = pd.read_excel('websites.xlsx')

all_links = []

for x in range(5):
    domain = websites_data[x+1].iloc[0]
    mentions = []

    page = requests.get(f"https://www.google.com/search?q=site%3A{domain}+%22neurodiversity%22+OR+%22neurodivergent%22+OR+%22autistic%22+OR+%22neurodiverse%22&rlz=1C1ONGR_enUS933US933&sxsrf=ALiCzsazMpQL1TcfIIWR-z7QBuEoSnxt7w%3A1659668026456&ei=OobsYqbGG9KoptQPuPCD8AI&ved=0ahUKEwimy6WZ2a75AhVSlIkEHTj4AC4Q4dUDCA4&uact=5&oq=site%3Atd.com+%22neurodiversity%22+OR+%22neurodivergent%22+OR+%22autistic%22+OR+%22neurodiverse%22&gs_lcp=Cgdnd3Mtd2l6EANKBAhBGAFKBAhGGABQzAxY2hdg4zBoAnAAeACAAWyIAfYFkgEEMTIuMZgBAKABAcABAQ&sclient=gws-wiz&safe=active&ssui=on")
    soup = BeautifulSoup(page.content, "html.parser")

    links = soup.findAll("a")
    for link in soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
        temp = re.split(":(?=http)",link["href"].replace("/url?q=",""))
        url = temp[0]
        print(url)
        domain_name = tldextract.extract(url)
        if domain_name.registered_domain == domain:
            mentions.append(url)
        print(mentions)
        mentions.append(url)
    all_links.append(mentions)

url = f'https://www.{domain}/'
df = pd.DataFrame()
df[url] = all_links
df.to_excel('result.xlsx', index = False)
print(all_links)

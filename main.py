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

websites_data = pd.read_excel('news_sources.xlsx')
all_links = []
for x in range(86):
    domain = websites_data[x+1].iloc[0]
    mentions = []
    page = requests.get(f"https://www.google.com/search?q=site%3A{domain}+%22neurodiversity%22+OR+%22neurodivergent%22+OR+%22autistic%22+OR+%22neurodiverse%22&rlz=1C1ONGR_enUS933US933&oq=site%3A&aqs=chrome.0.69i59l3j69i57j69i59l3j69i58.823j0j7&sourceid=chrome&ie=UTF-8&safe=active&ssui=on")
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.findAll("a")
    print(links)
    for link in soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
        temp = re.split(":(?=http)",link["href"].replace("/url?q=",""))
        url = temp[0]
        domain_name = tldextract.extract(url)
        print(url)
        if domain_name.registered_domain == domain:
            mentions.append(url)
    all_links.append(mentions)
url = f'{domain}'
df = pd.DataFrame()
df[url] = all_links
df.to_excel('result.xlsx', index = False)
print(all_links)
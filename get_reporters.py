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

websites_data = pd.read_excel('result.xlsx')
all_links = []
print(websites_data)
# domain = websites_data[0].iloc[0]
# print(domain)
# for x in range(86):
#     print(domain)




# url = f'{domain}'
# df = pd.DataFrame()
# df[url] = all_links
# df.to_excel('result.xlsx', index = False)
# print(all_links)
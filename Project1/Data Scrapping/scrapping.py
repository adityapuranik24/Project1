import requests
import json
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import csv
from xml.etree import ElementTree
import xmltodict
import pandas as pd

url = "http://apps.who.int/gho/athena/api/GHO/WHOSIS_000001"
res = requests.get(url)
dict_data = xmltodict.parse(res.content)
#print(dict_data)
df = pd.DataFrame(dict_data)
print(df)
# soup = BeautifulSoup(res.content, 'html5lib')
# print(soup.prettify())W
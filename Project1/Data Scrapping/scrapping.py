import requests
import json
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import csv
from xml.etree import ElementTree
import xmltodict
import pandas as pd

url = "https://twitter.com/explore/tabs/trending"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")
#print(soup.prettify())
title = soup.
print(title)
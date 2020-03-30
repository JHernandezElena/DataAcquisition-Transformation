import time
import requests
from bs4 import BeautifulSoup

url = "https://ifconfig.me/"
proxies = "179.60.127.35:60562"
proxy = {"http": proxies, "https": proxies}
response = requests.get(url, proxies=proxy)
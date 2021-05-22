from bs4 import BeautifulSoup, SoupStrainer
import requests
from urllib.parse import urlparse
def getLinks(url):
  try:
    urls = []
    req = requests.get(url)
    data = req.text
    soup = BeautifulSoup(data,features="html.parser")
    for link in soup.find_all("a"):
      urls.append(link.get("href"))
    return urls
  except:
    return []

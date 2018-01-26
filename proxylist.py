"""
Copyright © 2018 Tüm Hakları Saklıdır.

Author : Onur Güngör

https://www.facebook.com/onur.gungor.792

"""

import requests

from bs4 import BeautifulSoup

url = requests.get("https://premproxy.com/list/")

soup = BeautifulSoup(url.content,'html.parser')

proxy = [tr.text for tr in soup.findAll("tr",class_="anon")]

for i in proxy:

    i = i.replace("\n","")

    i = i.replace("anonymous" ," | Anonymous | ")

    i = i.replace("elite" ," | Elite | ")

    i = i.replace("transparent" ," | Transparent | ")

    print(i)

    print(len(i)*"-")
# Editor: GOTHIZzz
# Dev Date: 2021/10/13
import requests
from pyquery import PyQuery
url = 'https://pvp.qq.com/web201605/herolist.shtml'
html = requests.get(url).content
print(html)
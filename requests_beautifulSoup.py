'''
Created on Sep 28, 2018

@author: Tanner Yilmaz
'''

import requests
from bs4 import BeautifulSoup
 
url = 'http://github.com'
r = requests.get(url)
r_html = r.text
# .encode("utf-8")
soup = BeautifulSoup(r_html, 'html.parser')
# print(soup.p)
print(soup.prettify())
# soup = bs4.BeautifulSoup(html.text, 'html.parser').encode('utf-8')
# print(soup.prettify())
#<h2 class="h00-mktg mt-3 mb-2 text-center">\n      Boxes? Check.\n    </h2>


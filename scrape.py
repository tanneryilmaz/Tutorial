from bs4 import BeautifulSoup
import requests

source = requests.get('https://en.wikipedia.org/wiki/United_States_Census').text
soup = BeautifulSoup(source, 'lxml')

heading = soup.find_all('div', class_='body') #grabs all of the div tags that have a class 'body. heading is a list

for i in heading: #printing the text of each item in heading
    print(i.text.encode("utf-8"))
    print()

    
            
    



    
   


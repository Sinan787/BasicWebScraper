import httpx
from bs4 import BeautifulSoup

# Get the HTML file of the web page - here is an exexmplary notice about the 25th anniversary of Wikipedia

web_page = httpx.get("https://www.bpb.de/kurz-knapp/hintergrund-aktuell/574397/wissen-fuer-alle-25-jahre-wikipedia/")

#Creating a soup object to parse the HTML file
soup = BeautifulSoup(web_page, 'html.parser')

#Extracting the title and text of the web page
title = soup.title.string
text = soup.get_text()


with open(f"{title}.txt", "w", encoding="utf-8") as file:
    file.write(text)

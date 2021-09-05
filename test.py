from bs4 import BeautifulSoup
from urllib.request import urlopen

from bs4.element import Script

b_url = "http://olympus.realpython.org"

html_page = urlopen(b_url + "/profiles")
html_text = html_page.read().decode("utf-8")

soup = BeautifulSoup(html_text, "html.parser")

# print(soup.find_all)

for link in soup.find_all("a"):
    # add the link to the base url 
    link_url = b_url + link["href"]
    print(link_url)

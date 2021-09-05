from bs4 import BeautifulSoup
from urllib.request import urlopen

from bs4.element import Script

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
# "html.parser", tells the object which parser to use behind the scenes
soup = BeautifulSoup(html, "html.parser")

# Gets all the text within the tags 
print(soup.get_text())
# returns all the instances of a tag
print(soup.find_all("img"))

img_1, img_2 = soup.find_all("img")

img_1["src"]
img_2["src"]

# finds items in the html object with the "title" tag
print(soup.title)
# .string removes the extra shit around the word
print(soup.title.string) 
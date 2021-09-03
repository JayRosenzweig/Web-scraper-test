from urllib.request import urlopen

# REGX library
import re

url = "http://olympus.realpython.org/profiles/aphrodite"

url_2 = "http://olympus.realpython.org/profiles/poseidon"

url_3 = "http://olympus.realpython.org/profiles/dionysus"


page = urlopen(url_2)

# page is an HTTPResponse object (wrapper on the HTTP response from the server)
page

# use READ method to return a seqeunce of bytes from the 
html_bytes = page.read()
# decode the sequence into a string with utf-8 formatt 
html = html_bytes.decode("utf-8")

print("html from URL 2: \n" + html)

# extracting the title
title_index = html.find("<title>")
start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
print("this is the title: " + title)


page_REGEX = urlopen(url_3)
# string the read and recode together
html = page_REGEX.read().decode("utf-8")

print("\nhtml from url 3:\n " + html)

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
# use .group after .search to select the top response from the search
title = match_results.group()
title = re.sub("<.*?>", "", title) #remove HTML tags 
print("this is the title: " + title)


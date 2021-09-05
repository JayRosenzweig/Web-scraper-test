import mechanicalsoup
browser = mechanicalsoup.Browser()

url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
# get the beautiful soup object from the get request
login_html = login_page.soup

# prints the status code of the request 
# 200 = sucess
# 404 = not found
# 500 = server error
# print(login_page.soup)

# ineract with the form html
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"
# sumbit the input values 
profiles_page = browser.submit(form, login_page.url)
# THIS IS HOW HACKERS BRUTE FORCE 


#  once logged into the website,
#  obtain all the links used on the page the user logs into 
links = profiles_page.soup.select("a")
base_url = "http://olympus.realpython.org"
for link in links:
    text = link.text
    address = base_url + link["href"]
    print(f"{text}: {address}")
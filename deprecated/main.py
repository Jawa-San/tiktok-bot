import requests
import os.path
from bs4 import BeautifulSoup

def getRequest(link):
    if not os.path.exists('output.txt'):      #check if the request was outputted
        r = requests.get(link)
        f = open("output.txt", "a")
        f.write(r.text)
        f.close()
    else:
        print("File exists")

def getSoup():
    if os.path.exists('output.txt'):
        f = open("output.txt", "r")
        soup = BeautifulSoup(f, "html.parser")
        return soup
    else:                                   #if there is no output file, call getrequest and recall getsoup
        getRequest("https://www.reddit.com/r/tifu/comments/zqilqm/tifu_using_sign_language_to_make_my_deaf_partners/")
        getSoup()


def getText(soup):
    for i in soup.find_all("div", class_="_292iotee39Lmt0MkQZ2hPV"):
        print(i.get_text())






soup = getSoup()
print(type(soup))
getText(soup)




# # f = open("output.txt", "a")
# # f.write(soup.prettify())
# for i in soup.find_all("div", class_="_292iotee39Lmt0MkQZ2hPV RichTextJSON-root"):
#     print(i.get_text())
# # f.close()


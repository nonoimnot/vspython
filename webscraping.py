from bs4 import BeautifulSoup
import urllib.request
import csv
import selenium
from selenium.webdriver.common.keys import Keys
import requests

url = "https://www.pantip.com"
data = requests.get(url)
# print(data.status_code)
print(data.text)

soup = BeautifulSoup(data.text , "html.parser")
#print(soup.prettify())

x = soup.find_all("h3",{"class":"post-title"}) # <- ค่าที่ใช้ในการค้นหา
#x = soup.find_all("h2")
print("---------------------------------------------------------------------------")

for i in x:
    print("==========================================================")
    print(i.text)
    #print(i)
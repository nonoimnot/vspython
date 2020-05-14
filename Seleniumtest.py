from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os

#set Chrome option
chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--headless")
driver=webdriver.Chrome(options=chrome_options)

#Set directory
# path = 'C:/Python/' #กำหนด folder ที่ระบบจะต้องทำงาน
# os.chdir(path)
# driver=webdriver.Chrome(path+"chromedriver.exe")
driver.get("https://www.imdb.com/chart/top/")

print("-------------------------------------------------------------")
print("Detail : ", driver.title)
print("Window Handles : ", driver.window_handles)
print("Current Window Handles : ", driver.current_window_handle)
print("Current Url : ", driver.current_url)
# print("Page Source : ", driver.page_source)
print("-------------------------------------------------------------")

#Get location of movie names
movienames = driver.find_elements_by_class_name("titleColumn")
Movienames=[name.text for name in movienames]
# for n in Movienames:
#     print(str(n))

print("Number of Movies is ",str(len(Movienames)))

#Get rating of movies 
rating = driver.find_elements_by_class_name("ratingColumn.imdbRating")
Rating=[rate.text for rate in rating]
print("Number of rating = ", str(len(Rating)))

#Get location of links
links = driver.find_elements_by_xpath("//td[@class='titleColumn']/a")
Links = [link.get_attribute('href') for link in links ]
print("Number of Links is ", str(len(Links)))

# for l in Links:
#     print(str(l))

driver.find_element_by_class_name("titleColumn").click()

driver.close()
driver.quit()
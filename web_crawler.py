import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--disable-infobars")


chromedriver = "Desktop/chromedriver"
#os.environ["webdriver.chrome.driver"] = chromedriver
#browser = webdriver.Chrome(chromedriver)

browser = webdriver.Chrome(chromedriver,chrome_options=options)

companies=pd.read_csv("/Users/divalicious/Companies.csv")
companies=list(companies["name"])


companies_text={"name":[],"text":[]}

for company in companies:
	browser.get("https://www.google.co.in/")
	textBox = browser.find_element_by_id("lst-ib")
	time.sleep(3)
	textBox.send_keys(company+" wikipedia ")
	textBox.send_keys(Keys.ENTER)
	time.sleep(3)
	#time.sleep(6)
	#browser.find_element_by_name('btnK').click()

	#first_element=browser.find_elements_by_class_name('rc')
	#for elem in first_element:
	#	url=elem.find_elements_by_xpath('.//h3')
	#	for u in url:
	#		u.click()


	element=browser.find_element_by_xpath("""//*[@id="rso"]/div[1]/div/div[1]/div/div/h3/a""")
	element.click()
	time.sleep(3)

	paragraphs=browser.find_element_by_xpath("""//*[@id="mw-content-text"]/div""")
	time.sleep(3)
	print (paragraphs.text)

	browser.close()
	companies_text["name"].append(company)
	companies_text["text"].append(paragraphs.text)


df = pd.DataFrame(companies_text)
df.to_csv("Output.csv")

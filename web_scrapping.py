from bs4 import BeautifulSoup
import pandas as pd
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)
services = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=services, options=options)
driver.maximize_window()

# Logic Implementation

driver.get('https://www.flipkart.com/search?q=macbook+pro&sid=6bo%2Cb5g&as=on&as-show=on')
driver.implicitly_wait(20)

products = []
price = []
rating = []

content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
    nam = a.find('div', attrs={'class':'_4rR01T'})
    pric = a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    # ratin = a.find('div', attrs={'class':'_3LWZlK'}))
    products.append(nam.text)
    price.append(pric.text)

df = pd.DataFrame({'Product Name':products,'Price':price}) 
df.to_csv('products.csv', index=False, encoding='utf-8')

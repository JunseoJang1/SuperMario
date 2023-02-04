from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()),
                          options=chrome_options)

ID = "lhj2442"
PW = "zheld123"

url = 'https://memberssl.auction.co.kr/Authenticate/default.aspx?\
url=http%3A//corners.auction.co.kr/AllKill/AllDay.aspx'
driver.get(url)
driver.implicitly_wait(3)

e = driver.find_element(By.ID, 'id')
e.clear()
e.send_keys(ID)
e = driver.find_element(By.ID, 'password')
e.clear()
e.send_keys(PW)
e.send_keys(Keys.ENTER)
driver.implicitly_wait(3)

s = driver.find_element(By.CLASS_NAME, 'search_input_keyword')
s.clear()
s.send_keys("선풍기")
s.send_keys(Keys.ENTER)

#p = driver.find_element(By.CLASS_NAME, 'for')#
#for i in p:
    #print(i.text)#


# By.CLASS_NAME
# By.ID


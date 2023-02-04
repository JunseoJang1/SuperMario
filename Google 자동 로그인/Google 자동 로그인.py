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

driver.get('http://escrow.auction.co.kr/close/\OrderProcessList.aspx?loginType=50')
webpage = driver.page_source

#상품명 출력
products = driver.find_elements(By.CLASS_NAME, 'product-name')
for i in products:
    print(i.text)
#주문번호 출력
products = driver.find_elements(By.CLASS_NAME, 'product-order-num')
for i in products:
    print(i.text)
#상품금액 출력
products = driver.find_elements(By.CLASS_NAME, 'charge')
for i in products:
    print(i.text)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
import time
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()),
                          options=chrome_options)

html_source = driver.page_source
soup = BeautifulSoup(html_source, 'lxml')

###########################################
# 설정

name = "워크맨"
url = 'https://www.youtube.com/watch?v=hJYr4oLnu8w'

###########################################

comments = []
comment = ''
send = True
driver.get(url)
driver.implicitly_wait(3)



last_page_height = driver.execute_script("return document.documentElement.scrollHeight")

youtube_title = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-watch-metadata')
for j in youtube_title:
    title = j.text.split("\n")[0]
    print("영상 제목 : ", title)

while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3.0)
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight")

    if new_page_height == last_page_height:
        break
    last_page_height = new_page_height



    youtube_commenterID = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-comment-renderer')
    #youtube_comments = soup.select('yt-formatted-string#content-text')
    f = open(name + ".txt", 'w')
    for i in youtube_commenterID:
        if i.text in comments:
            send = False
        else:
            send = True
            if "답글" in i.text:
                commenter = i.text.split('\n')[0]
                comment_time = i.text.split('\n')[1]
                comment = i.text.split('\n')[2]
        if send != False:
            try:
                f.write("댓글을 단 채널 : "+ commenter +' '+ comment_time)
                f.write("댓글 : "+ comment +'\n')
            except Exception as err:
                print("이모티콘 저장에 문제가 있습니다.")
            finally:
                print("오류를 건너뛰었습니다.")
                      
            print("댓글을 단 채널 : ", commenter ,' ', comment_time)
            print("댓글 : ", comment, '\n')
            comments.append(i.text)
            send = False
    f.close()
    break

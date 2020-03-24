from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.google.com.tw/#q=%E8%9F%B2%E5%B8%AB'

driver = webdriver.PhantomJS(executable_path=r'D:\GitHub\Python\phantomjs-2.1.1-windows\bin\phantomjs.exe')  # PhantomJS
driver.get(url)  # 把網址交給瀏覽器 
pageSource = driver.page_source  # 取得網頁原始碼
soup = BeautifulSoup(pageSource, 'lxml')  # 解析器接手
for text in soup.select('#result-stats'):
    print('蟲師', text.get_text())
# result = soup.select('#result-stats').get_text()  # 「約有 1,550,000,000 項結果」
# print('蟲師', result)
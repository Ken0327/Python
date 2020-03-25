import requests

res = requests.get('http://pala.tw/js-example/')
print(res.text)

from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r'D:\GitHub\Python\phantomjs-2.1.1-windows\bin\phantomjs.exe')  # PhantomJs
driver.get('http://pala.tw/js-example/')  # 輸入範例網址，交給瀏覽器 
pageSource = driver.page_source  # 取得網頁原始碼
print(pageSource)

driver.close()  # 關閉瀏覽器
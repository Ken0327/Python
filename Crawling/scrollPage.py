import time
from selenium import webdriver
from bs4 import BeautifulSoup
# from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=r'C:\Users\user\.wdm\drivers\chromedriver\80.0.3987.106\win32\chromedriver.exe') # chrome瀏覽器
# driver = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(3)
driver.get('https://hahow.in/courses')

for i in range(10):  # 進行十次
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')  # 重複往下捲動
    time.sleep(1)  # 每次執行打瞌睡一秒                    

driver.close()  # 關閉瀏覽器
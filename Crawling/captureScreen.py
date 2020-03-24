from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\user\.wdm\drivers\chromedriver\80.0.3987.106\win32\chromedriver.exe')
driver.get('http://www.pixiv.net/')
driver.save_screenshot('D:\GitHub\Python\Crawling\pictures\capture.png')  # 保存截圖
driver.close()
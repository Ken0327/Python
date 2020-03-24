from datetime import date
import requests
from bs4 import BeautifulSoup

# tag = input("請輸入定位元素，class前面加上.，id前面加上# ")

print('淨值爬蟲 - 安聯收益成長基金-南非幣')
res = requests.get('https://www.moneydj.com/funddj/yp/yp011001.djhtm?a=TLZ78')
soup = BeautifulSoup(res.text, "lxml")
today = date.today().strftime("%Y/%m/%d")
values_Rand = []
print('Today is ' + today)
print('最新日期: ' + str(soup.select('.t3n2c1')[0].get_text()))

for drink in soup.select('.t3n2'):
    values_Rand.append(drink.get_text())

print('*最新淨值: ' + values_Rand[0])
print('最高淨值: ' + values_Rand[1])
print('最低淨值: ' + values_Rand[2])

unitAll = float('3131.98')
print('目前單位數:' + str(unitAll))

print('淨值爬蟲 - 安聯收益成長基金-美金')
res = requests.get('https://www.moneydj.com/funddj/yp/yp011001.djhtm?a=TLZ64')
soup = BeautifulSoup(res.text, "lxml")
values_US = []
print('最新日期: ' + str(soup.select('.t3n2c1')[0].get_text()))

for drink in soup.select('.t3n2'):
    values_US.append(drink.get_text())

print('*最新淨值: ' + values_US[0])
print('最高淨值: ' + values_US[1])
print('最低淨值: ' + values_US[2])

print('----------------------------------------')

print('匯率爬蟲 - 南非幣轉美金匯率')
res_USDtoRand = requests.get('https://tw.money.yahoo.com/currency/USDZAR=X')
res_RandtoTWD = requests.get('https://forex.cnyes.com/currency/ZAR/TWD')
res_UStoTWD = requests.get('https://forex.cnyes.com/currency/USD/TWD')
soup_USDtoRand = BeautifulSoup(res_USDtoRand.text, "lxml")
soup_RandtoTWD = BeautifulSoup(res_RandtoTWD.text, "lxml")
soup_UStoTWD = BeautifulSoup(res_UStoTWD.text, "lxml")

data = soup_USDtoRand.find_all("div", class_="Ta-end remark")[0].text[0:10] # soup.select('.Ta-end remark')
print('最新日期: ' + data)
currency_UStoRand = float(soup_USDtoRand.find_all("span", class_="Fw-b Fz-27 Lh-27 C-n Pend-20")[0].text)
currency_RandtoUS = 1 / currency_UStoRand

currency_RandtoTW = float(soup_RandtoTWD.find_all("div", class_="jsx-685978323 currency-number currency-now")[0].text)
currency_UStoTW = float(soup_UStoTWD.find_all("div", class_="jsx-685978323 currency-number currency-now")[0].text)

print('匯率-美金->南非幣: ' + str(currency_UStoRand))
print('匯率-美金->台幣: ' + str(currency_UStoTW))
print('匯率-南非幣->美金匯率: ' + str(currency_RandtoUS))
print('匯率-南非幣->台幣匯率: ' + str(currency_RandtoTW))

print('----------------------------------------')

print('*保單價值-台幣: ' + str(unitAll * float(values_Rand[0]) * currency_RandtoTW))
print('*保單價值-美金: ' + str(unitAll * float(values_Rand[0]) * currency_RandtoUS) + '-> 美金轉回台幣: ' + str(unitAll * float(values_Rand[0]) * currency_RandtoUS * currency_UStoTW) )
print('*可購買美金保單單位數: ' + str(unitAll * float(values_Rand[0]) * currency_RandtoUS / float(values_US[0])))
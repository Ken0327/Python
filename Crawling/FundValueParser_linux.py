import syslog
from datetime import date
import requests
from bs4 import BeautifulSoup

from flask import Flask, request, abort

from linebot import ( LineBotApi, WebhookHandler )
from linebot.models import ( MessageEvent, TextMessage, TextSendMessage )
from linebot.exceptions import LineBotApiError

def fundValueCrawling():
    try:
        Messages = ''
        divider = '----------------------------------------\n'
        today = date.today().strftime("%Y/%m/%d")
        todayis = '今天是 ' + today
        Messages += todayis + '\n'
        syslog.syslog(today)

        fundRand = '淨值爬蟲 - 安聯收益成長基金-南非幣'
        Messages += fundRand + '\n'
        res = requests.get('https://www.moneydj.com/funddj/yp/yp011001.djhtm?a=TLZ78')
        soup = BeautifulSoup(res.text, "lxml")
        values_Rand = []
        lastdate = '最新日期: ' + str(soup.select('.t3n2c1')[0].get_text())
        Messages += lastdate + '\n'

        for drink in soup.select('.t3n2'):
            values_Rand.append(drink.get_text())

        lastvalueRand = '*最新淨值: ' + values_Rand[0]
        highvalueRand = '最高淨值: ' + values_Rand[1]
        lowvalueRand = '最低淨值: ' + values_Rand[2]
        Messages += lastvalueRand + '\n'
        Messages += highvalueRand + '\n'
        Messages += lowvalueRand + '\n'

        unitAll = float('3131.98')
        unitnow = '目前單位數:' + str(unitAll)
        Messages += unitnow + '\n'

        #----------------------------------------------
        Messages += divider

        fundUS = '淨值爬蟲 - 安聯收益成長基金-美金'
        Messages += fundUS + '\n'
        res = requests.get('https://www.moneydj.com/funddj/yp/yp011001.djhtm?a=TLZ64')
        soup = BeautifulSoup(res.text, "lxml")
        values_US = []
        # print('最新日期: ' + str(soup.select('.t3n2c1')[0].get_text()))

        for drink in soup.select('.t3n2'):
            values_US.append(drink.get_text())

        lastvalueUS = '*最新淨值: ' + values_US[0]
        highvalueUS = '最高淨值: ' + values_US[1]
        lowvalueUS = '最低淨值: ' + values_US[2]
        Messages += lastvalueUS + '\n'
        Messages += highvalueUS + '\n'
        Messages += lowvalueUS + '\n'

        #------------------------------------------------
        Messages += divider

        currency = '匯率爬蟲 - 南非幣轉美金匯率'
        Messages += currency + '\n'

        res_USDtoRand = requests.get('https://tw.money.yahoo.com/currency/USDZAR=X')
        res_RandtoTWD = requests.get('https://forex.cnyes.com/currency/ZAR/TWD')
        res_UStoTWD = requests.get('https://forex.cnyes.com/currency/USD/TWD')
        soup_USDtoRand = BeautifulSoup(res_USDtoRand.text, "lxml")
        soup_RandtoTWD = BeautifulSoup(res_RandtoTWD.text, "lxml")
        soup_UStoTWD = BeautifulSoup(res_UStoTWD.text, "lxml")

        data = soup_USDtoRand.find_all("div", class_="Ta-end remark")[0].text[0:10] # soup.select('.Ta-end remark')
        # print('最新日期: ' + data)
        currency_UStoRand = float(soup_USDtoRand.find_all("span", class_="Fw-b Fz-27 Lh-27 C-n Pend-20")[0].text)
        currency_RandtoUS = 1 / currency_UStoRand

        currency_RandtoTW = float(soup_RandtoTWD.find_all("div", class_="jsx-685978323 currency-number currency-now")[0].text)
        currency_UStoTW = float(soup_UStoTWD.find_all("div", class_="jsx-685978323 currency-number currency-now")[0].text)

        currencyUS2Rand = '匯率-美金->南非幣: ' + str(currency_UStoRand)
        currencyUS2TW = '匯率-美金->台幣: ' + str(currency_UStoTW)
        currencyRand2US = '匯率-南非幣->美金匯率: ' + str(currency_RandtoUS)
        currencyRand2TW = '匯率-南非幣->台幣匯率: ' + str(currency_RandtoTW)
        Messages += currencyUS2Rand + '\n'
        Messages += currencyUS2TW + '\n'
        Messages += currencyRand2US + '\n'
        Messages += currencyRand2TW + '\n'

        # print('----------------------------------------')
        Messages += divider

        valuetotalTW = '*保單價值-台幣: ' + str(unitAll * float(values_Rand[0]) * currency_RandtoTW)
        valuetotalUS = '*保單價值-美金: ' + str(unitAll * float(values_Rand[0]) * currency_RandtoUS) + '-> 美金轉回台幣: ' + str(unitAll * float(values_Rand[0]) * currency_RandtoUS * currency_UStoTW)
        affodableunitUS = '*可購買美金保單單位數: ' + str(unitAll * float(values_Rand[0]) * currency_RandtoUS / float(values_US[0]))
        Messages += valuetotalTW + '\n'
        Messages += valuetotalUS + '\n'
        Messages += affodableunitUS + '\n'
        return Messages
    except error as e:
        print(e)
        syslog.syslog(e)
        return 'crawling error'


# -----------------------------------------------------------------
LINE_CHANNEL_SECRET="Uac7151e06ab765d8f64c3168480b1b19"
LINE_CHANNEL_ACCESS_TOKEN="tRJfr5AgsY8gLeDzBLwHddKY98kPdmxojkE1E3hptG4o99yree69YQfrjz4UbZhIkUtK5dWyE4DiQsTsGZgPLe+x6HpDVJO8OUV2Ht5EdZvtnkysUtgcj0Ht1Joso6HZfn3Dkj/zLogB+xKs1UmvHgdB04t89/1O/w1cDnyilFU="

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

def pushMessages(message):
    try:
        line_bot_api.push_message(LINE_CHANNEL_SECRET, TextSendMessage(text=message))
    except LineBotApiError as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error.message)
        print(e.error.details)
        syslog.syslog(e)

if __name__ == "__main__":
    syslog.syslog('Start Fund Value Crawling')
    Messages = fundValueCrawling()
    print(Messages)
    pushMessages(Messages)
    syslog.syslog('Finished Crawling')
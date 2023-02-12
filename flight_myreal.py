from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import requests
import json
from selenium.webdriver.common.by import By

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


driver = set_chrome_driver()
driver.implicitly_wait(5)
#
def get_min_price():
    videos, titles = [], []
    row = 1
    col = 1
    start_url = "https://flights.myrealtrip.com/air/b2c/AIR/INT/AIRINTSCH0100100010.k1?initform=RT&domintgubun=I&depctycd=SEL&depctycd=OSA&depctycd=&depctycd=&depctynm=%EC%84%9C%EC%9A%B8&depctynm=%EC%98%A4%EC%82%AC%EC%B9%B4&depctynm=&depctynm=&arrctycd=OSA&arrctycd=SEL&arrctycd=&arrctycd=&arrctynm=%EC%98%A4%EC%82%AC%EC%B9%B4&arrctynm=%EC%84%9C%EC%9A%B8&arrctynm=&arrctynm=&depdt=2023-04-15&depdt=2023-04-19&depdt=&depdt=&opencase=N&opencase=N&opencase=N&openday=&openday=&openday=&depdomintgbn=I&tasktype=B2C&servicecacheyn=Y&adtcount=2&chdcount=0&infcount=0&cabinclass=Y&cabinsepflag=Y&preferaircd=&secrchType=FARE&maxprice=&availcount=250&KSESID=air%3Ab2c%3ASELK138RB%3ASELK138RB%3A%3A00"
    driver.get(start_url)

    while(1):
        try:
            path = ".mrt_scdul_srch_foreign .fare_total"
            min_price = driver.find_element(By.CSS_SELECTOR,path).text
            min_price = min_price.replace('원', '')
            return min_price
        except Exception as e:
            print(e)
            a = 1

    return '123'

while(1):
    price = get_min_price()
    int_price = price.replace(',', "")
    int_price = int(int_price)

    if int_price < 370000:
        url = "https://hooks.slack.com/services/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"
        # response = requests.get(url_items)

        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
        body = {
            "text": "https://flights.myrealtrip.com/air/b2c/AIR/INT/AIRINTSCH0100100010.k1?initform=RT&domintgubun=I&depctycd=SEL&depctycd=OSA&depctycd=&depctycd=&depctynm=%EC%84%9C%EC%9A%B8&depctynm=%EC%98%A4%EC%82%AC%EC%B9%B4&depctynm=&depctynm=&arrctycd=OSA&arrctycd=SEL&arrctycd=&arrctycd=&arrctynm=%EC%98%A4%EC%82%AC%EC%B9%B4&arrctynm=%EC%84%9C%EC%9A%B8&arrctynm=&arrctynm=&depdt=2023-04-15&depdt=2023-04-19&depdt=&depdt=&opencase=N&opencase=N&opencase=N&openday=&openday=&openday=&depdomintgbn=I&tasktype=B2C&servicecacheyn=Y&adtcount=2&chdcount=0&infcount=0&cabinclass=Y&cabinsepflag=Y&preferaircd=&secrchType=FARE&maxprice=&availcount=250&KSESID=air%3Ab2c%3ASELK138RB%3ASELK138RB%3A%3A00 gogogo!!!"
        }
        response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
        print(response)
        print("boom")
    print(int_price)


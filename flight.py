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
    start_url = "https://m-flight.naver.com/flights/international/ICN-KIX-20230415/KIX-ICN-20230419?adult=2&fareType=Y"
    driver.get(start_url)

    while(1):
        try:
            path = "/html/body/div[1]/div/div[1]/div[6]/div/div[3]/div[1]/div/div[2]/div/div/div/div/b/i"
            min_price = driver.find_element(By.XPATH,path).text
            return min_price
        except Exception as e:
            print(e)
            a = 1

    return '123'

while(1):
    price = get_min_price()
    int_price = price.replace(',', "")
    int_price = int(int_price)

    if int_price < 360000:
        url = "https://hooks.slack.com/services/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"
        # response = requests.get(url_items)

        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
        body = {
            "text": "https://m-flight.naver.com/flights/international/ICN-KIX-20230415/KIX-ICN-20230419?adult=2&fareType=Y gogogo!!!"
        }
        response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
        print(response)
        print("boom")
    print(int_price)


import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import Testing
import os

def login():
    # get the path of ChromeDriverServer
    dir = os.path.dirname(__file__)
    driver = webdriver.Chrome(executable_path=r"G:\chromedriver_win32\chromedriver.exe")
    #driver.implicitly_wait(30)
    driver.maximize_window()

    URL = 'http://codeforces.com/enter?back=%2F'
    # navigate to the application home page
    driver.get(URL)
    #print('fsd')
    # get the search textbox
    search_field = driver.find_element_by_id("handle")
    search_field.send_keys("")
    search_field = driver.find_element_by_id("password")
    search_field.send_keys("")
    x=search_field.submit()

    driver.implicitly_wait(50)

    return driver

def startHacking(max_pages):
    page = 1
    driver = login()
    while page <= max_pages:
        url = "http://codeforces.com/contest/903/status/A/page/" + str(page) + "?order=BY_ARRIVED_DESC"
        #url = "http://codeforces.com/contest/915/status/A/page/" + str(page) + "?order=BY_ARRIVED_DESC"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")

        view_source = soup.findAll('a', {'class': 'view-source'})
        verdict = soup.findAll('span', {'class': 'verdict-accepted'})

        i = 0
        for verd in verdict:
            if  verd.text == "Accepted" :
            #if i<1:
                code_url = "http://codeforces.com" + view_source[i].get('href')
                #code_url = "http://codeforces.com/contest/915/submission/34174730"
                code = requests.get(code_url)
                plain = code.text
                code_soup = BeautifulSoup(plain, "lxml")
                rows = code_soup.findAll('td')
                lang = rows[3].text[6:-6]
                #print(lang)
                s = plain.find('<pre class="prettyprint')
                custom_code = plain[s + 73:]
                e = custom_code.find('<div class="roundbox ')
                custom_code = custom_code[:e - 30]
                #print(s, s + e)

                custom_code = custom_code.replace("&gt;", ">")
                custom_code = custom_code.replace("&lt;", "<")
                custom_code = custom_code.replace("&apos;", "'")
                custom_code = custom_code.replace("&quot;", '"')
                custom_code = custom_code.replace("&amp;", "&")
                #print(code_url)
                #print(custom_code)

                Testing.custom_invoc(custom_code, lang, driver)
            i+=1



        page += 1


startHacking(1)

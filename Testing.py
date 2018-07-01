from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def custom_invoc(custom_code, lang, driver):
    #driver = webdriver.Chrome(executable_path=r"G:\chromedriver_win32\chromedriver.exe")
    testing_url = "http://codeforces.com/contest/915/customtest"

    input = "2 6 5"
    desired_output = "YES\nNO"

    driver.get(testing_url)

    btn = driver.find_elements_by_name("submit")[0]
    select = Select(driver.find_element_by_name('programTypeId'))

    # select by visible text
    select.select_by_visible_text('Free Pascal 3')

    # driver.find_elements_by_id("toggleEditorCheckbox")[0].click()

    driver.implicitly_wait(100)

    txt = driver.find_elements_by_class_name("ace_text-input")[0]
    txt.clear()
    txt.send_keys(custom_code)

    test = driver.find_elements_by_name("input")[0]
    test.send_keys(input)

    driver.implicitly_wait(100)
    #select.select_by_visible_text(lang)
    select.select_by_visible_text('GNU G++14 6.4.0')

    driver.implicitly_wait(100)

    # driver.find_elements_by_id("toggleEditorCheckbox")[0].click()
    btn.submit()

    driver.implicitly_wait(1000)

    time.sleep(5)
    #op = driver.find_elements_by_name("output")[0]
    # get the textarea element by tag name
    textarea = driver.find_element_by_name('output')

    # print the attribute of the textarea
    output = textarea.get_attribute('value')
    o = output.replace("\n", " ")
    #print(o)
    i = 0
    b = 1
    for s in desired_output:
        if s != output[i]:
            b = 0
            break
        i+=1
    if(b):
        print("Don't Hack")
    else:
        print("Hack Maaro!!")


    #print(textarea.get_attribute('rows'))
    #print(textarea.get_attribute('cols'))

    #output = driver.find_elements_by_name("output")[0]
    #print(output.getText())
    #print(repr(op.text))
    time.sleep(3)

    driver.implicitly_wait(1000)

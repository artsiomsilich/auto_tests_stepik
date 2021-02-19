import math
from selenium import webdriver
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link='http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_answer = browser.find_element_by_xpath('//input[@id="answer"]')
    x = browser.find_element_by_xpath('//img[@id="treasure"]').get_attribute("valuex")
    checkbox_robot = browser.find_element_by_xpath('//input[@id="robotCheckbox"]').click()
    time.sleep(3)
    radio = browser.find_element_by_xpath('//form//input[@class="check-input" and @id="robotsRule"]').click()
    time.sleep(3)
    input_answer.send_keys(calc(x))
    time.sleep(3)
    button = browser.find_element_by_xpath('//button').click()
    time.sleep(10)



finally:
    browser.quit()
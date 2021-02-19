from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

link='http://suninjuly.github.io/explicit_wait2.html'
browser=webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)
    price_path = '//*[@id="price"]'
    WebDriverWait(browser, 15).until(ec.text_to_be_present_in_element((By.XPATH, price_path), '$100'))
    browser.find_element_by_xpath('//*[@id="book"]').click()
    ans = calc(int(browser.find_element_by_xpath('//*[@id="input_value"]').text))
    browser.find_element_by_xpath('//input').send_keys(ans)
    browser.find_element_by_xpath('//button[@id="solve"]').click()
    time.sleep(5)

finally:
    browser.quit()
from selenium import webdriver
import time

link='http://suninjuly.github.io/registration2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    forms = browser.find_elements_by_xpath('//form/div[@class="first_block"]//input')
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    for e in forms:
        e.send_keys("Мой ответ")
    button.click()
    time.sleep(10)

finally:
    browser.quit()
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

link='http://suninjuly.github.io/selects1.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    number1=int(browser.find_element_by_xpath('//span[@id="num1"]').text)
    number2=int(browser.find_element_by_xpath('//span[@id="num2"]').text)
    ans=str(number1+number2)

    selector=Select(browser.find_element_by_xpath('//select'))
    selector.select_by_value(ans)
    # time.sleep(10)
    # time.sleep(2)
    browser.find_element_by_xpath('//button').click()
    time.sleep(5)


finally:
    browser.quit()
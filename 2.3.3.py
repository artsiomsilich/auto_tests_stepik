from selenium import webdriver
import time
import math

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser.get(link)
    browser.find_element_by_xpath('//button').click()
    browser.switch_to.alert.accept()
    ans = calc(int(browser.find_element_by_xpath('//*[@id="input_value"]').text))
    browser.find_element_by_xpath('//input').send_keys(ans)
    browser.find_element_by_xpath('//button').click()
    time.sleep(5)




finally:
    browser.quit()
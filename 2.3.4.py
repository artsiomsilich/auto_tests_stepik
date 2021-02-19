from selenium import webdriver
import time
import math

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser.get(link)
    browser.find_element_by_xpath('//button').click()
    Window_list = browser.window_handles
    print(str(Window_list))
    browser.switch_to.window(Window_list[1])
    browser.switch_to.window(Window_list[0])
    time.sleep(2)
    ans = calc(int(browser.find_element_by_xpath('//*[@id="input_value"]').text))
    browser.find_element_by_xpath('//input').send_keys(ans)
    browser.find_element_by_xpath('//button').click()
    time.sleep(5)




finally:
    browser.quit()
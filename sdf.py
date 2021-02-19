from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()

    browser.get(link)


    x = int(browser.find_element_by_xpath('//label//*[@id="input_value"]').text)
    a = str(math.log((abs(12 * (math.sin(x))))))
    print(a)
    browser.find_element_by_xpath('//*[@id="answer"]').send_keys(a)
    robot_checkbox = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)# scroll
    robot_checkbox.click()
    robot_radio = browser.find_element_by_xpath('//*[@id="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radio)
    robot_radio.click()
    button = browser.find_element_by_xpath('//button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radio)
    button.click()
    time.sleep(10)
finally:
    browser.quit()

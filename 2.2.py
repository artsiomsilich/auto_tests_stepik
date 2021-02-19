from selenium import webdriver
import time
import os

try:
    link='http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_xpath('//input[@name="firstname"]').send_keys('Art_name')
    browser.find_element_by_xpath('//input[@name="lastname"]').send_keys('Art_surname')
    browser.find_element_by_xpath('//input[@name="email"]').send_keys('Art@email.com')


    current_loc = os.path.abspath(os.path.dirname('2.2.py'))
    loc = os.path.abspath('2.2.py')
    file_path = os.path.join(current_loc, 'asdf.txt')
    browser.find_element_by_xpath('//input[@id="file"]').send_keys(file_path)
    browser.find_element_by_xpath('//button').click()
    time.sleep(5)

finally:
    browser.quit()
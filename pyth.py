from selenium import webdriver
import time

link='https://tsglove-prod-staging.azurewebsites.net/'

try:

    browser = webdriver.Chrome()
    browser.get(link)
    browser.set_window_size(width=1400,height=900)

    time.sleep(10)
    preorder = browser.find_element_by_xpath('//*[@class="btn btn-primary btn-md p-2"]')
    # first_name_field = browser.find_element_by_xpath('//input[@id="first_name"]')
    form=browser.find_elements_by_xpath('//div[@class="form-group"]//input')
    for element in form:
        element.send_keys("Artemio XXX")
        time.sleep(1)

    #preorder_button = browser.find_element_by_xpath("//*[text()='Pre-order now']")
    # learn_more_button = browser.find_element_by_xpath("//button[@class='accept-policy close btn btn-success']")


    # learn_more_button.click()
    preorder.click()
    time.sleep(10)
    # first_name_field.send_keys("Artemio XXX")
    time.sleep(5)
finally:
    browser.quit()




__author__ = 'jessie'

import time
from selenium import webdriver


# launch Firefox
driver = webdriver.Firefox()

# load Twitter login page
driver.get("https://twitter.com/login")

# find the username and password element
username_element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input")
password_element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input")

# type in username and password
username_element.send_keys('274558119@qq.com')
password_element.send_keys('wxc16888')

 # click Sign In and we should be logged in
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/button').click()

# the following javascript scrolls down the entire page body.  Since Twitter
# uses "inifinite scrolling", more content will be added to the bottom of the
# DOM as you scroll... since it is in the loop, it will scroll down up to 100
# times.
for _ in range(100):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# print all of the page source that was loaded
f = open('twitter.html', 'w')
f.write(driver.page_source.encode("utf-8"))
f.close()

# quit and close browser
driver.quit()
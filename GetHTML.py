__author__ = 'jessie'

import time
from selenium import webdriver
from PIL import Image


# launch Firefox
driver = webdriver.Firefox()

# load Twitter login page
driver.get("https://twitter.com/login")

# find the username and password element
username_element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input")
password_element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input")

# type in username and password
username_element.send_keys('weixc123@outlook.com')
password_element.send_keys('wxc16888')

 # click Sign In and we should be logged in
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/button').click()

# click Tweets and go into the page showing all tweets
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div[1]/div/div[3]/ul/li[1]/a/span[1]').click()

# find the element in HTML containing all the tweets
element = driver.find_element_by_class_name('GridTimeline') # find part of the page you want image of
location = element.location
size = element.size

# take screenshot of the whole page
driver.save_screenshot('screenshot.png')

# go back to the home page
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div/div[2]/ul/li[1]/a/span[2]').click()

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

# uses PIL library to open image in memory
im = Image.open('screenshot.png')

left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']

# crop the screenshot to contain only the tweets
im = im.crop((left, top, right, bottom))
im.save('screenshot.png')

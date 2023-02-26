# code using chatgpt so not optimize

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from loguru import logger

# set up options for headless browsing
chrome_options = Options()
chrome_options.add_argument("--headless")

# create a new instance of the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# navigate to the website's login page
# driver.get("https://example.com/login")

# # enter username and password and submit the form
# username_input = driver.find_element_by_name("username")
# password_input = driver.find_element_by_name("password")
# username_input.send_keys("your_username")
# password_input.send_keys("your_password")
# password_input.send_keys(Keys.RETURN)

# # wait for the page to load
# time.sleep(5)

# navigate to the page you want to scrape
driver.get("https://docsumo.com/")

# scroll to the bottom of the page to load all content
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# get all the text on the page
text = driver.page_source
text = driver.execute_script("return document.body.innerText")
logger.info(f"text: {text}")
driver.save_screenshot("screen-shot.png")

# close the browser window
driver.quit()

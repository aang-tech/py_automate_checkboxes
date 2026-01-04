import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# Optional: remove the "Chrome is being controlled by automated software" banner
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

web = webdriver.Chrome(options=chrome_options)
web.get("https://the-internet.herokuapp.com/checkboxes")

#grab all checkboxes that has checked
#un check them
checked_boxs = web.find_elements(By.CSS_SELECTOR, "input[type='checkbox'][checked]")
for checkbox in checked_boxs:
    checkbox.click()

time.sleep(2)

#check the checkbox that has a text after the input tag
unchecked_box = web.find_element(By.XPATH, "//input[@type='checkbox'][following-sibling::text()[contains(., 'checkbox 1')]]")
unchecked_box.click()


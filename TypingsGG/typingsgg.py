# Imports:

from selenium import webdriver
import time

# Path to Chrome Driver

browser = webdriver.Chrome("C:\Program Files\WebDriver\chromedriver.exe")

# Getting into Typings.gg

url="https://typings.gg"
browser.get(url)

# The total word count:

theButton = browser.find_element_by_xpath("//*[@id='wc-250']")
theButton.click()

time.sleep(1)

# Writing the Founded Words:

input_field = browser.find_element_by_xpath("//*[@id='input-field']")

# Find Words Here:
i = 1
while i < 251:
    current_word_xpath = browser.find_element_by_xpath("//*[@id='text-display']/span["+str(i)+"]")
    current_word = current_word_xpath.text
    input_field.send_keys(current_word+" ")
    #time.sleep(0.15) #COMMENT FOR TURBO MODE
    i += 1

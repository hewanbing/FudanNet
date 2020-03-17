#!/usr/bin/python3
import sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support.select import Select
def login(browser,FudanID,Password):
    username = browser.find_element_by_css_selector('#loginname')
    username.clear()
    username.send_keys(FudanID)
    password = browser.find_element_by_css_selector('#password')
    password.clear()
    password.send_keys(Password)
    submit = browser.find_element_by_css_selector('#button')
    submit.click()
    time.sleep(1)
    WebDriverWait(browser,60).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    

options = webdriver.FirefoxOptions()
options.set_headless()
options.add_argument('--disable-gpu')
browser = webdriver.Firefox(firefox_binary="/usr/bin/firefox",firefox_options=options)
browser.get("http://10.108.255.249/")
WebDriverWait(browser,60).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
time.sleep(1)
WebDriverWait(browser,60).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
login(browser,sys.argv[1],sys.argv[2])    
browser.close()

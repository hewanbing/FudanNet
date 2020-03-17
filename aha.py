#!/usr/bin/python3
import sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support.select import Select
def login(browser,FudanID,Password):
    username = browser.find_element_by_css_selector('#username')
    username.clear()
    username.send_keys(FudanID)
    password = browser.find_element_by_css_selector('#password')
    password.clear()
    password.send_keys(Password)
    submit = browser.find_element_by_css_selector('#idcheckloginbtn')
    submit.click()
    time.sleep(1)
    WebDriverWait(browser,60).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    
def report(browser):
    sfzx = browser.find_element_by_css_selector('.form>ul:nth-child(1)>li:nth-child(4)>div:nth-child(1)>div:nth-child(2)>div:nth-child(2)>span:nth-child(1)')
    sfzx.click()
    #
    sfzgn = browser.find_element_by_css_selector('.form>ul:nth-child(1)>li:nth-child(5)>div:nth-child(1)> div:nth-child(2)>div:nth-child(2)>span:nth-child(1)')
    sfzgn.click()
    myprovice = Select(browser.find_element_by_css_selector('#myprovice'))
    myprovice.select_by_value("上海市")
    time.sleep(0.5)
    mycity = Select(browser.find_element_by_css_selector('#mycity'))
    mycity.select_by_value("上海市")
    time.sleep(0.5)
    myarea = Select(browser.find_element_by_css_selector('#myarea'))
    myarea.select_by_value("杨浦区")
    #
    tw = browser.find_element_by_css_selector('.form>ul:nth-child(1)>li:nth-child(7)>div:nth-child(1)>div:nth-child(2)>div:nth-child(1)>span:nth-child(1)')
    tw.click()
    #
    tzjssfjkyc = browser.find_element_by_css_selector('.form>ul:nth-child(1)>li:nth-child(8)>div:nth-child(1)>div:nth-child(2)>div:nth-child(2)>span:nth-child(1)')
    tzjssfjkyc.click()
    #
    tzjssfjthb = browser.find_element_by_css_selector('.form>ul:nth-child(1)>li:nth-child(9)>div:nth-child(1)>div:nth-child(2)>div:nth-child(2)>span:nth-child(1)')
    tzjssfjthb.click()
    #
    tzjssfqz = browser.find_element_by_css_selector('.form>ul:nth-child(1)>li:nth-child(10)>div:nth-child(1)>div:nth-child(2)>div:nth-child(2)>span:nth-child(1)')
    tzjssfqz.click()
    #
    sfcxzysx = browser.find_element_by_css_selector('.form>ul:nth-child(1)>li:nth-child(11)>div:nth-child(1)>div:nth-child(2)>div:nth-child(2)>span:nth-child(1)')
    sfcxzysx.click()
    #
    submit = browser.find_element_by_css_selector('.footers>a')
    submit.click()
    time.sleep(0.5)
    submit = browser.find_element_by_css_selector('div.wapcf-btn:nth-child(2)')
    submit.click()
    #
    WebDriverWait(browser,60).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

options = webdriver.FirefoxOptions()
options.set_headless()
options.add_argument('--disable-gpu')
browser = webdriver.Firefox(firefox_binary="/usr/bin/firefox",firefox_options=options)
browser.get("https://zlapp.fudan.edu.cn/site/ncov/fudanDaily")
WebDriverWait(browser,60).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

time.sleep(1)
WebDriverWait(browser,60).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
if 'https://uis.fudan.edu.cn/authserver/login' in browser.current_url:
    WebDriverWait(browser,60).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    login(browser,sys.argv[1],sys,argv[2])
    
if 'https://zlapp.fudan.edu.cn/site/ncov/TfudanDaily' in browser.current_url:
    report(browser)

browser.close()

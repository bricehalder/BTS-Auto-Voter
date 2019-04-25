from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import PySimpleGUI as sg
import sys
import re

email = sg.PopupGetText('Enter email address:', 'BTS Auto Voter',keep_on_top=True)

if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
    sg.Popup('Error: Please enter a valid email address', keep_on_top=True)
    exit()

browser = webdriver.Chrome('./chromedriver')
browser.get(('https://bbma.votenow.tv/?initialWidth=984&childId=telescope_app&parentTitle=Vote%20for%20-%20Billboard%20Music%20Awards%202019%20%7C%20Billboard&parentUrl=https%3A%2F%2Fwww.billboard.com%2Fbbmasvote%23telescope_app'))

browser.implicitly_wait(10)
browser.find_element_by_class_name("login").click()

browser.implicitly_wait(10)
browser.find_element_by_id('optin_1').click()

browser.implicitly_wait(10)
browser.find_element_by_class_name('btn-reveal-email').click()

browser.implicitly_wait(10)
browser.find_element_by_class_name('form-control').send_keys(email)

browser.implicitly_wait(10)
browser.find_element_by_class_name('btn-auth-email').click()

browser.implicitly_wait(10)
browser.find_element_by_class_name('name-align').click()

while True:
    try:
        browser.implicitly_wait(10)
        browser.find_element_by_xpath('//*[@id="TelescopeWidgetCategoryVote"]/div[1]/div/div/div/div/div[2]/ul/li[1]/div/div/div/div/button').click()

        browser.implicitly_wait(10)
        browser.find_element_by_xpath('//*[@id="thankscat2-A1"]/div[2]/div[3]/button').click()

        browser.implicitly_wait(10)
        browser.find_element_by_xpath('//*[@id="thankscat2-A1"]/div[2]/div[3]/button[3]').click()
    except:
        break

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

email = 'REPLACE'

try:
	email = sys.argv[1]
except:
	print("\nError: This script should be run with the following flags:\n"
	+ "python bts-bot.py email\n"
	+ "ex: python bts-bot.py hello@example.com\n")
	exit()

browser = webdriver.Chrome('./chromedriver')
browser.get(('https://bbma.votenow.tv/?initialWidth=984&childId=telescope_app&parentTitle=Vote%20for%20-%20Billboard%20Music%20Awards%202019%20%7C%20Billboard&parentUrl=https%3A%2F%2Fwww.billboard.com%2Fbbmasvote%23telescope_app'))

# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "login")))
browser.implicitly_wait(10)
browser.find_element_by_class_name("login").click()

# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "optin_1")))
browser.implicitly_wait(10)
browser.find_element_by_id('optin_1').click()

# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-reveal-email")))
browser.implicitly_wait(10)
browser.find_element_by_class_name('btn-reveal-email').click()

# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "form-control")))
browser.implicitly_wait(10)
browser.find_element_by_class_name('form-control').send_keys(email)

# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-auth-email")))
browser.implicitly_wait(10)
browser.find_element_by_class_name('btn-auth-email').click()

# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "name-align")))
browser.implicitly_wait(10)
browser.find_element_by_class_name('name-align').click()

while True:
    try:
        # WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="TelescopeWidgetCategoryVote"]/div[1]/div/div/div/div/div[2]/ul/li[1]/div/div/div/div/button')))
        browser.implicitly_wait(10)
        browser.find_element_by_xpath('//*[@id="TelescopeWidgetCategoryVote"]/div[1]/div/div/div/div/div[2]/ul/li[1]/div/div/div/div/button').click()

        # WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="thankscat2-A1"]/div[2]/div[3]/button')))
        browser.implicitly_wait(10)
        browser.find_element_by_xpath('//*[@id="thankscat2-A1"]/div[2]/div[3]/button').click()

        # WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="thankscat2-A1"]/div[2]/div[3]/button[3]')))
        browser.implicitly_wait(10)
        browser.find_element_by_xpath('//*[@id="thankscat2-A1"]/div[2]/div[3]/button[3]').click()
    except:
        break

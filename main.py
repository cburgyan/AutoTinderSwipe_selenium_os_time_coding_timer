import selenium.webdriver

import coding_timer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import os
import time


coding_timer = coding_timer.CodingTimer("time_main.txt")
# coding_timer.start_time()
# coding_timer.pause_time()
# coding_timer.unpause_time()
# coding_timer.stop_time()


URL = 'https://tinder.com/app/recs'
WAIT_FOR_WEBELEMENT = 10
NUMBER_OF_CANDIDATES = int(os.environ.get('NUM_CANDIDATES'))


#Create Chrome Driver
CHROME_EXEC_PATH = 'C:/Users/T852/DeveloperFoo/chromedriver_win32/chromedriver.exe'
servicer = webdriver.chrome.service.Service(CHROME_EXEC_PATH)
driver = webdriver.Chrome(service=servicer)


#Connect Driver to Website
driver.get(URL)
main_page = driver.current_window_handle
print(driver.window_handles)


#Get Go-to-login Button
go_to_login_we = WebDriverWait(driver, WAIT_FOR_WEBELEMENT).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')))
go_to_login_we.click()


# #Fill Out Login Form
time.sleep(2)
facebook_login_btn_we = WebDriverWait(driver, WAIT_FOR_WEBELEMENT).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')))
facebook_login_btn_we.click()


#Switch to New Pop-up Login Window
time.sleep(2)
print(driver.window_handles)
print(driver.current_window_handle)
login_page = driver.window_handles[1]
driver.switch_to.window(login_page)


#Continue Filling Out Login Form
fb_email_we = WebDriverWait(driver, WAIT_FOR_WEBELEMENT).until(expected_conditions.element_to_be_clickable((By.ID, 'email')))
fb_email_we.send_keys(os.environ.get("EMAIL"))
fb_password_we = WebDriverWait(driver, WAIT_FOR_WEBELEMENT).until(expected_conditions.element_to_be_clickable((By.ID, 'pass')))
fb_password_we.send_keys(os.environ.get("PASS"))
fb_login_we = WebDriverWait(driver, WAIT_FOR_WEBELEMENT).until(expected_conditions.element_to_be_clickable((By.NAME, 'login')))
fb_login_we.click()


#Allow Location to be Used
driver.switch_to.window(main_page)
location_we = WebDriverWait(driver, WAIT_FOR_WEBELEMENT).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]/span')))
location_we.click()


#Accept Cookies
accept_cookies_we = WebDriverWait(driver, WAIT_FOR_WEBELEMENT).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/span')))
accept_cookies_we.click()


#Enable Notifications
enable_notifications_we = WebDriverWait(driver, WAIT_FOR_WEBELEMENT).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]/span')))
enable_notifications_we.click()


#Begin Main Program Flow
for index in range(1, NUMBER_OF_CANDIDATES + 1):
    time.sleep(5)
    candidate_we = driver.find_element(by=By.XPATH, value='/html/body')
    # candidate_we.send_keys(Keys.UP)
    try:
        babble_we = driver.find_element(By.XPATH, value=os.environ.get("PATHER"))
        if int(babble_we.text) > os.environ.get("WELL"):
            candidate_we.send_keys(Keys.LEFT)
    except Exception:
        candidate_we.send_keys(Keys.LEFT)

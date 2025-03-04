from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def startBot(username, password, url):
    # Use ChromeDriver without specifying a path (Selenium will manage it)
    driver = webdriver.Chrome()

    # Open the website
    driver.get(url)

  

    # Enter username and password
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)

    # Click the login button
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()



# Credentials & URL
username = "omegaN3xus404"
password = "Manishbon@321"
url = "https://github.com/login"

startBot(username, password, url)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

with open('setting.txt', 'r') as file:
    setting = file.readlines()
    browser = (setting[0].split(": "))[1]
    URL = (setting[1].split(": "))[1]


service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get(URL)
driver.maximize_window()
print(driver.title)
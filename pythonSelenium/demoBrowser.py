from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

with open('setting.txt', 'r') as file:
    setting = file.readlines()
    videoLink = (setting[0].split(": "))[1]

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.youtube.com/"+videoLink)
driver.maximize_window()

driver.find_element(By.XPATH,"//div[@class='ytp-left-controls']/button[@class='ytp-play-button ytp-button']").click()
maxtime = driver.find_element(By.XPATH,"//div[@class='ytp-left-controls']/div[@class='ytp-time-display notranslate']/span[2]/span[@class='ytp-time-duration']").text
print(maxtime)
time = maxtime.split(":")
videoTime = (int(time[0])*60) + int(time[1])
print(videoTime)
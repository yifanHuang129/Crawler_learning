from selenium import webdriver
import time

brower = webdriver.Chrome()
brower.get('https://www.baidu.com')
time.sleep(100)
brower.quit()
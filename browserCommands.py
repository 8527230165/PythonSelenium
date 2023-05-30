import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(5)  # seconds
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

time.sleep(5)

driver.close()



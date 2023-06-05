from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
wait=WebDriverWait(driver,10,poll_frequency=2)
driver.get("https://www.amazon.in/")

cookies=driver.get_cookies()
print("Number of Cookies: ",len(cookies))

for cookie in cookies:
    print(cookie.get('name'))

import time
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
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

#open alert popup
alert_element=driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
alert_element.click()
time.sleep(5)

alert_window=driver.switch_to.alert

alert_text=alert_window.text
print(alert_text)

alert_window.send_keys("Hello Alert")
#alert_window.accept()
alert_window.dismiss()


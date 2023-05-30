from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
wait=WebDriverWait(driver,10,poll_frequency=2)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
#driver.find_element(By.XPATH,"//input[@id='monday']").click()
day_checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(day_checkboxes))
for day in day_checkboxes:
    day.click()
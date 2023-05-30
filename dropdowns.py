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
driver.get("https://www.amazon.in/")
wait.until(EC.presence_of_element_located((By.XPATH,"//select[@id='searchDropdownBox']")))
country_dropdown_element=driver.find_element(By.XPATH,"//select[@id='searchDropdownBox']")
country_dropdown=Select(country_dropdown_element)

country_dropdown.select_by_visible_text("Alexa Skills")
country_dropdown.select_by_value("search-alias=electronics")
country_dropdown.select_by_index(6)

all_options=country_dropdown.options
print("Total number of options are :",len(all_options))
for option in all_options:
    print(option.text)
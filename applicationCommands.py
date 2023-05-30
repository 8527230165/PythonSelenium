from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(5)  # seconds
driver.get("https://demo.nopcommerce.com/register")

#is_displayed

search_box=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Display search status: ",search_box.is_displayed())

print("Enable search status: ",search_box.is_enabled())

#is_selected
male_radio_button=driver.find_element(By.XPATH,"//input[@id='gender-male']")
female_radio_button=driver.find_element(By.XPATH,"//input[@id='gender-female']")
print("Male Radio button status: ",male_radio_button.is_selected())
print("Female Radio button status: ",female_radio_button.is_selected())

male_radio_button.click()
#female_radio_button.click()
print("After selecting radio buttons ->")
print("Male Radio button status: ",male_radio_button.is_selected())
print("Female Radio button status: ",female_radio_button.is_selected())


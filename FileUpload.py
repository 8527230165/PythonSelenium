from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/upload")
choose_file=driver.find_element(By.ID,'file-upload')
choose_file.send_keys("D:\\Projects\\Bench\\SeleniumWithPython\\Users.xlsx")
driver.find_element(By.ID,'file-submit').click()
success_text=driver.find_element(By.TAG_NAME,'h3').text
assert success_text == "File Uploaded!"
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

#options=options,service=Service(ChromeDriverManager().install())
#executable_path="D:\Projects\Bench\SeleniumWithPython\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)#seconds
driver.get("https://opensource-demo.orangehrmlive.com/")

time.sleep(5)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()


actualTitle=driver.title
expectedTitle="OrangeHRM"

if actualTitle==expectedTitle:
    print("login test passed")
else:
    print("login test failed")

#driver.close()
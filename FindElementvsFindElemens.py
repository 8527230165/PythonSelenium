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

#find_element
search_box=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
search_box.send_keys("Apple")

elements=driver.find_element(By.XPATH,"//div[@class='footer']//a")
print("Footer element text :",elements.text)

#find_elements
elements2=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print("No of Elements in Footer: ",len(elements2))
for ele in elements2:
    print(ele.text)


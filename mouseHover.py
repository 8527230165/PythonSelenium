from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
wait=WebDriverWait(driver,10,poll_frequency=2)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

#wait.until(EC.presence_of_element_located((By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")))
button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
action=ActionChains(driver)
action.context_click(button).perform()
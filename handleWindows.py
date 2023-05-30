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
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH,"//input[@class='wikipedia-search-input']").send_keys("Selenium")
driver.find_element(By.XPATH,"//input[@class='wikipedia-search-button']").click()
wait.until(EC.presence_of_element_located((By.XPATH,"//div[@id='wikipedia-search-result-link']")))
results=driver.find_elements(By.XPATH,"//div[@id='wikipedia-search-result-link']")
print("Number of Results are:",len(results))
print("Searched Results are:")
for result in results:
    print(result.text)
    driver.find_element(By.LINK_TEXT,result.text).click()
new_windows=driver.window_handles
print("All open Window Titles are: ")
for new_win in new_windows:
    driver.switch_to.window(new_win)
    print(driver.title)
    if driver.title!='Automation Testing Practice':
        driver.close()
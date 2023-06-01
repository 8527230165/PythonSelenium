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
driver.get("https://jqueryui.com/datepicker/")

wait.until(EC.presence_of_element_located((By.XPATH,"//iframe[@class='demo-frame']")))
driver.switch_to.frame(0)
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
mm='September'
yr='2023'
dd='15'
while True:
    month=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    year=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if month==mm and year==yr:
        break
    else:
        next=driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']")
        next.click()
dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody//tr//td")
print(len(dates))
for date in dates:
    if date.text==dd:
        driver.find_element(By.XPATH,"//a[normalize-space()='"+dd+"']").click()
        print(date.text)


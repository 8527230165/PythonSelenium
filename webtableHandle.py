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
rows=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
print("Number of Rows:",len(rows))
cols=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]//th")
print("Number of Columns: ",len(cols))

driver.find_element(By.XPATH,"//td[normalize-space()='Master In Selenium']")

driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[2]/td[1]")

for row in range(2,len(rows)+1):
    for col in range(1,len(cols)+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(row)+"]/td["+str(col)+"]").text
        print(data,end=' ')
    print()
print("List of Bookes wrote by Mukesh------------------------------------")
for row in range(2,len(rows)+1):
    author=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[2]").text
    if(author=='Mukesh'):
        bookname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[1]").text
        print(bookname)


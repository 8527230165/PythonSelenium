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
driver.get("https://opensource-demo.orangehrmlive.com/")
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='username']")))
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

wait.until(EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='Admin']")))
driver.find_element(By.XPATH,"//a[normalize-space()='Admin']").click()

wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='oxd-table-card']")))
data_rows=driver.find_elements(By.XPATH,"//div[@class='oxd-table-body']//div[@class='oxd-table-row oxd-table-row--with-border']//div[5]")
print("Total Users are: ",len(data_rows))
count=0

for row in data_rows:
    if row.text =='Enabled':
        count+=1
print("Number of Enabled users are:",count)
print("Number of Disabled users are:",len(data_rows)-count)

for i in range(1,len(data_rows)+1):
    username=driver.find_element(By.XPATH,"//div[@class='oxd-table-body']//div["+str(i)+"]//div[@class='oxd-table-row oxd-table-row--with-border']//div[2]")
    userrole=driver.find_element(By.XPATH,"//div[@class='oxd-table-body']//div["+str(i)+"]//div[@class='oxd-table-row oxd-table-row--with-border']//div[3]")
    if userrole.text == 'ESS':
        print(username.text,' , ',userrole.text,end= '     ')





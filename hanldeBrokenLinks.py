import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
wait=WebDriverWait(driver,10,poll_frequency=2)
driver.get("https://www.amazon.in/")
countBroken=0
countValid=0
links=driver.find_elements(By.TAG_NAME,"a")
url_status_code=0
for link in links:
    url=link.get_attribute('href')
    #print(url)
    
    try:
        res=requests.head(url)
        url_status_code=res.status_code
    except:
        None

    #print(url,' --> ', res)
    if url_status_code==200:
        countValid+=1
    else:
        countBroken+=1
print("Total Number of links are :",len(links))
print("Number of Valid links are :",countValid)
print("Number of Broken links are :",countBroken)
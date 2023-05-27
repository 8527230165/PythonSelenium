from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(5)  # seconds
driver.get("https://money.rediff.com/gainers")

#self Xpath Axes
text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Authum Investment')]/self::a").text
print("Self XPATH text:"+text_msg)

#Parent Xpath Axes
text_parent=driver.find_element(By.XPATH,"//a[contains(text(),'Authum Investment')]/parent::td").text
print("Parent XPATH text:"+text_parent)

#Child Xpath Axes
childs=driver.find_elements(By.XPATH,"//a[contains(text(),'Authum Investment')]/ancestor::tr/child::td")
print("Child XPATH text:"+str(len(childs)))

#Ancestor Xpath Axes
ancestor_text=driver.find_element(By.XPATH,"//a[contains(text(),'Authum Investment')]/ancestor::tr").text
print("Ancestor XPATH text:"+ancestor_text)

#Descendant Xpath Axes
descendant_text=driver.find_elements(By.XPATH,"//a[contains(text(),'Authum Investment')]/ancestor::tr/descendant::*")
print("Descendant XPATH text:"+str(len(descendant_text)))

#Following Xpath Axes
following_text=driver.find_elements(By.XPATH,"//a[contains(text(),'Authum Investment')]/ancestor::tr/following::*")
print("Following XPATH text:"+str(len(following_text)))

#Following-Sibling Xpath Axes
following_sibling_text=driver.find_elements(By.XPATH,"//a[contains(text(),'Authum Investment')]/ancestor::tr/following-sibling::*")
print("Following-Sibling XPATH text:"+str(len(following_sibling_text)))

#Preceding Xpath Axes
preceding_text=driver.find_elements(By.XPATH,"//a[contains(text(),'Authum Investment')]/ancestor::tr/preceding::tr")
print("Preceding XPATH text:"+str(len(preceding_text)))

#Preceding-Sibling Xpath Axes
preceding_sibling_text=driver.find_elements(By.XPATH,"//a[contains(text(),'Authum Investment')]/ancestor::tr/preceding-sibling::tr")
print("Preceding-Sibling XPATH text:"+str(len(preceding_sibling_text)))


driver.close()
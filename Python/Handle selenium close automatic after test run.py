from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# handle selenium close automatic after test run
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://stage.mobipaid.com/en/register")
print("Page title is:" + driver.title)
driver.find_element(By.ID, 'btn-register').click()

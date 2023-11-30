from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://stage.mobipaid.com/en/register")
print("Page title is:" + driver.title)
driver.find_element(By.ID, 'btn-register').click()

# using CSS SELECTOR
print("Assert error is: " + WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#signatory_first_name'))).get_attribute("validationMessage"))
# using XPATH
print("Assert error is: " + WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="signatory_first_name"]'))).get_attribute("validationMessage"))

driver.get_screenshot_as_file("screenshot/pp.png")

driver.close()
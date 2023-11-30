from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import faker

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://stage.mobipaid.com/en/register")
print("Page title is : " + driver.title)

# random data or faker
# reference https://faker.readthedocs.io
from faker import Faker
fake = Faker(['id_ID'])

Fname = driver.find_element(By.ID, 'signatory_first_name')
Fname.send_keys(fake.first_name())

Lname = driver.find_element(By.ID, 'signatory_last_name')
Lname.send_keys(fake.last_name())

driver.find_element(By.ID, 'btn-register').click()

# handle HTML validate pop-up
# using CSS SELECTOR
print("Assert error is: " + WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#email'))).get_attribute("validationMessage"))
# using XPATH
print("Assert error is: " + WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]'))).get_attribute("validationMessage"))

driver.get_screenshot_as_file('Screenshot/REG02.png')
driver.close()

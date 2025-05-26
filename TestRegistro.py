from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://localhost/software%202/registro.php")

name_input = driver.find_element(By.NAME, "nombres")
apell_input = driver.find_element(By.NAME, "apellidos")
equipo_input = driver.find_element(By.NAME, "equipo")
fecha_input = driver.find_element(By.NAME, "fecha_nacimiento")
sexo_input = driver.find_element(By.NAME, "sexo")
telefono_input = driver.find_element(By.NAME, "telefono")
email_input = driver.find_element(By.NAME, "email")
pais_input = driver.find_element(By.NAME, "pais")
ciudad_input = driver.find_element(By.NAME, "ciudad")
direccion_input = driver.find_element(By.NAME, "direccion")
pass_input = driver.find_element(By.NAME, "password")
checkbox_input = driver.find_element(By.NAME, "terminos")

name_input.send_keys("usuario2")
apell_input.send_keys("apellido2")
equipo_input.send_keys("Ineos Grenadiers")
fecha_input.send_keys("1983-11-06")
sexo_input.send_keys("Masculino")
telefono_input.send_keys("3847590235")
email_input.send_keys("usuario2@gmail.com")
pais_input.send_keys("Francia")
ciudad_input.send_keys("Pekin")
direccion_input.send_keys("cllae45# 73-54")
pass_input.send_keys("usuario2123")
checkbox_input.click()

submit_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
submit_btn.click()

time.sleep(2)

try:
    error_msg = driver.find_element(By.ID, "error-registro")
    print("❌ Registro fallido: ", error_msg.text)
except NoSuchElementException:
    print("✅ Registro exitoso y redireccionado")

driver.quit()

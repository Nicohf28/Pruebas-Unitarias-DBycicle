from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://localhost/software%202/ticket.php")

ticket_input = driver.find_element(By.NAME, "ticket")
descripcion_input = driver.find_element(By.NAME, "ticket-descripcion")


ticket_input.send_keys("Jugador lesionado")
descripcion_input.send_keys("Se solicita la apertura de la actualizacion de usuario para realizar una cambio al jugador")


submit_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
submit_btn.click()

time.sleep(2)

try:
    error_msg = driver.find_element(By.ID, "error-registro")
    print("❌ Ticket fallido: ", error_msg.text)
except NoSuchElementException:
    print("✅ Ticket realizado exitosamente")

driver.quit()

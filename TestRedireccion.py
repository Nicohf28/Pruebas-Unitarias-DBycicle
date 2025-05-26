from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://localhost/software%202/index.php")

# Espera opcional por si hay carga de página
time.sleep(1)

# Buscar el botón o enlace de "INICIAR SESIÓN"
# Esto depende de cómo esté el enlace en tu navbar. Si es un <a href="inicio_sesion.php">, puedes buscarlo así:
login_link = driver.find_element(By.LINK_TEXT, "INICIO SESION")
login_link.click()

time.sleep(2)

# Verifica que estamos ahora en la URL del formulario de inicio de sesión
if "inicio_sesion.php" in driver.current_url:
    print("✅ Redirección exitosa al formulario de inicio de sesión.")
else:
    print("❌ No se redireccionó correctamente al formulario.")

driver.quit()

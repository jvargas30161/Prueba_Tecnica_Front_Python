
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from manejo_errores_funciones import manejar_errores   # Importa la función desde archivo


# Ruta del archivo ejecutable de ChromeDriver
chromedriver_path = "C:/web_drivers/chromedriver.exe"

# Opciones de Chrome para limpiar la caché
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=./chrome_profile")  # Carpeta para el perfil de usuario
chrome_options.add_argument("--disable-extensions")  # Deshabilitar extensiones
chrome_options.add_argument("--disable-plugins")  # Deshabilitar plugins

# Inicializa el controlador de Chrome
driver = webdriver.Chrome()

# Maximiza la ventana del navegador
driver.maximize_window()

# Navega a Google
driver.get("https://www.google.com")
time.sleep(2)

# Llama a la función manejar_errores
manejar_errores(driver)
time.sleep(5)

# Cierra el navegador
driver.close()
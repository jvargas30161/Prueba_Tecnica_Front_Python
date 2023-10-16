import json
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def obtener_texto_desde_archivo():
    try:
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
            busqueda = data.get("busqueda", "")
        return busqueda
    except FileNotFoundError as e:
        print("Error al abrir el archivo JSON:", e)
        return None


def buscar_texto_en_pagina(driver, texto_a_buscar):
    page_content = driver.page_source
    if texto_a_buscar in page_content:
        print(f"Se encontró el texto '{texto_a_buscar}' en la página de Wikipedia.")
    else:
        print(f"No se encontró el texto '{texto_a_buscar}' en la página de Wikipedia.")


def tomar_screenshot(driver, nombre_archivo):
    try:
        driver.save_screenshot(nombre_archivo)
        print(f"Screenshot guardado como {nombre_archivo}")
    except Exception as e:
        print(f"Error al tomar el screenshot: {e}")

def manejar_errores(driver):
    try:
        # Encuentra el elemento por selector CSS (ejemplo: #W0wltc > div)
        element = driver.find_element(By.CSS_SELECTOR, "#W0wltc > div")
        element.click()

        busqueda = obtener_texto_desde_archivo()
        if busqueda is not None:
            # Encuentra el elemento por su selector CSS (#APjFqb) y escribe el contenido del JSON
            element_to_fill = driver.find_element(By.CSS_SELECTOR, "#APjFqb")
            element_to_fill.send_keys(busqueda)

            # "Enter" para realizar la búsqueda
            element_to_fill.send_keys(Keys.RETURN)
            time.sleep(5)

            # Encuentra enlace que contiene el texto "automatización Wikipedia"
            enlace_wikipedia = driver.find_element(By.PARTIAL_LINK_TEXT, "https://es.wikipedia")
            time.sleep(5)
            enlace_wikipedia.click()
            time.sleep(5)

        buscar_texto_en_pagina(driver, "convirtiéndose en el primer proceso industrial completamente automatizado")

        # screenshot de la página de Wikipedia
        tomar_screenshot(driver, "screenshot.png")

    except Exception as e:
        print("Error en la operación:", e)
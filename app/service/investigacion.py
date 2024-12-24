import os
from env.env import dir_res 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from service.antecedentes_policia import antecedentes_policia

# Verificar si la carpeta 'res' existe; si no, crearla
if not os.path.exists(dir_res):
    os.makedirs(dir_res)

# Función para investigar un equipo
def investigar_documento(tipo, documento):

    # Configuración del controlador de Chrome
    chrome_options = Options()

    # Ruta al ChromeDriver
    driver_path = "C:\\selenium\\chromedriver.exe"

    # Configurar el servicio de ChromeDriver
    service = Service(driver_path)

    # Crear instancia del navegador
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # # Maximizar la ventana del navegador
    driver.maximize_window()

    investigaciones(tipo, documento, driver)

    return investigaciones

def investigaciones(tipo, documento, driver):

    try:
        antecedentes_policia(tipo, documento, driver)
    except Exception as e:
        print("Error en la investigación de antecedentes policiales: ", e)

    input("Presione Enter para continuar...")
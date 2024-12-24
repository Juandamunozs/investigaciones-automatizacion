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

    try:
        options = Options()
        options.add_argument(f"user-data-dir=C:\\Users\\juand\\AppData\\Local\\Google\\Chrome\\User Data")  
        options.add_argument(f"profile-directory=Profile 1") 

        # Ruta al ejecutable de ChromeDriver
        service = Service(r"C:\\selenium\\chromedriver.exe")  

        # Crear el driver
        driver = webdriver.Chrome(service=service, options=options)
        # driver = webdriver.Chrome(service=service)

        # # Maximizar la ventana del navegador
        driver.maximize_window()

        res_investigacion = investigaciones(tipo, documento, driver)

        return res_investigacion
    
    except Exception as e:
        print("Error al abrir el navegador: ", e)


def investigaciones(tipo, documento, driver):

    res_antecedentes_policia = None

    try:
        res_antecedentes_policia = antecedentes_policia(tipo, documento, driver)
    except Exception as e:
        print("Error en la investigación de antecedentes policiales: ", e)

    dic_investigaciones ={
        "antecedentes_policia": res_antecedentes_policia
    }

    driver.quit()

    return dic_investigaciones
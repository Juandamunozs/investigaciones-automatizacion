import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from service.busquedas.antecedentes_policia import antecedentes_policia
from service.busquedas.multas_transito import antecedentes_trasito
from service.busquedas.sisben import sisben
from service.busquedas.rama_judicial import rama_judicial
from service.busquedas.funcion_publica import funcion_publica
from env.env import dir_res, dir_chromedriver, dir_pdf
from module.limpiar.limpiar_json import limpiar_json
from module.email.modulo_correo.email import send_email
from service.pdf.pdfService import crear_pdf

# Verificar si la carpeta 'res' existe; si no, crearla
if not os.path.exists(dir_res):
    os.makedirs(dir_res)

# Función para investigar un equipo
def investigar_documento(tipo_documento, numero_documento, nombre_documento, tipo_persona, email_informe):
    try:
        options = Options()
        options.add_argument(f"user-data-dir=C:\\Users\\juand\\AppData\\Local\\Google\\Chrome\\User Data")  
        options.add_argument(f"profile-directory=Profile 1") 

        # Ruta al ejecutable de ChromeDriver
        service = Service(dir_chromedriver)  

        # Crear el driver
        driver = webdriver.Chrome(service=service, options=options)
        # driver = webdriver.Chrome(service=service)

        # Maximizar la ventana del navegador
        driver.maximize_window()

        res_investigacion = investigaciones(tipo_documento, numero_documento, driver, nombre_documento, tipo_persona, email_informe)

        return res_investigacion
    
    except Exception as e:
        print("Error al abrir el navegador: ", e)

def investigaciones(tipo_documento, numero_documento, driver, nombre_documento, tipo_persona, email_informe):
    res_antecedentes_policia = None
    res_antecedentes_transito = None
    res_sisben = None
    res_adress = None
    res_rama_judicial = None
    res_funcion_publica = None
    res_procuraduria = None

    try:
        res_antecedentes_transito = antecedentes_trasito(tipo_documento, numero_documento, driver)
    except Exception as e:
        print("Error en la investigación de antecedentes de tránsito: ", e)

    try:
        res_antecedentes_policia = antecedentes_policia(tipo_documento, numero_documento, driver)
    except Exception as e:
        print("Error en la investigación de antecedentes policiales: ", e)

    try:
        res_sisben = sisben(tipo_documento, numero_documento, driver)
    except Exception as e:
        print("Error en la investigación del sisben: ", e) 

    try:
        res_rama_judicial = rama_judicial(tipo_documento, numero_documento, nombre_documento, tipo_persona, driver)
    except Exception as e:
        print("Error en la investigación de la rama judicial): ", e)

    try:
        res_funcion_publica = funcion_publica(nombre_documento, driver)
    except Exception as e:
        print("Error en la investigación de la función pública: ", e)

    # try:
    #     res_adress = adress(tipo_documento, numero_documento driver)
    # except Exception as e:
    #     print("Error en la investigación de ADRESS: ", e)

    # try:
    #     res_procuraduria = procuradoria(tipo_documento, numero_documento driver)
    # except Exception as e:
    #     print("Error en la investigación de la procuraduría: ", e)
    
    driver.quit()


    # Limpiar las respuestas de los antecedentes
    dic_investigaciones = {
        "info": {
            "antecedentes_policia": limpiar_json(res_antecedentes_policia),
            "antecedentes_transito": limpiar_json(res_antecedentes_transito),
            "sisben": limpiar_json(res_sisben),
            "rama_judicial": limpiar_json(res_rama_judicial),
            "funcion_publica": limpiar_json(res_funcion_publica)
        }
    }

    ruta_pdf = f"{dir_pdf}\\{tipo_documento}_{numero_documento}.pdf"
    crear_pdf(dic_investigaciones, nombre_documento, tipo_documento, numero_documento, tipo_persona)
    send_email(ruta_pdf, tipo_documento, numero_documento, nombre_documento, tipo_persona, email_informe)
    return dic_investigaciones
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

def antecedentes_trasito(tipo_documento, numero_documento, driver):
    driver.get("https://www.fcm.org.co/simit/#/home-public")

    # Cerrar dialogo
    while True:
        try:
            btn_aceptar_politicas = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="modalInformation"]/div/div/div[1]/button'))
            )
            btn_aceptar_politicas.click()
            break
        except Exception as e:
            print(f"Reintentando clic en cerrar dialogo: {e}")


    # Ingresar documento
    while True:
        try:
            input_documento = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, "txtBusqueda"))
            )
            input_documento.send_keys(numero_documento)
            break
        except Exception as e:
            print(f"Reintentando ingreso de documento: {e}")

    # Buscar
    while True:
        try:
            btn_consultar = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.ID, 'consultar'))
            )
            btn_consultar.click()
            break
        except Exception as e:
            print(f"Reintentando clic en buscar {e}")

    try:

        try:
            # Espera hasta que el elemento esté presente en el DOM (hasta 10 segundos)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="resumenEstadoCuenta"]/div')))

            # Localiza el elemento por su ID y captura el texto
            mensaje_ciudadano = driver.find_element(By.XPATH, '//*[@id="resumenEstadoCuenta"]/div')

            # Extrae el texto contenido en el elemento
            respuesta = mensaje_ciudadano.text

            respuesta = respuesta.replace("\n", " ")

        except:
            script = """
            const elemento = document.getElementsByClassName('col-lg-6 px-lg-3 px-0 mt-3')[0];
            const texto = elemento.innerText;
            return texto;
            """

            respuesta = driver.execute_script(script)
            respuesta = respuesta.replace("\n", " ")
           
    except Exception as e:
        respuesta = f"Error en la consulta de antecedentes de tránsito: {e}"

    return respuesta
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

def antecedentes_policia(tipo, documento, driver):
    driver.get("https://antecedentes.policia.gov.co:7005/WebJudicial/")

    # Aceptar políticas
    while True:
        try:
            btn_aceptar_politicas = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="aceptaOption:0"]'))
            )
            btn_aceptar_politicas.click()
            break
        except Exception as e:
            print(f"Reintentando clic en aceptar políticas: {e}")

    # Continuar después de aceptar políticas
    while True:
        try:
            btn_enviar = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.ID, 'continuarBtn'))
            )
            btn_enviar.click()
            break
        except Exception as e:
            print(f"Reintentando clic en enviar políticas: {e}")

    # Ingresar documento
    while True:
        try:
            input_documento = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, "cedulaInput"))
            )
            input_documento.send_keys(documento)
            break
        except Exception as e:
            print(f"Reintentando ingreso de documento: {e}")

    # Manejar el iframe del CAPTCHA
    while True:
        try:
            iframe = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "iframe"))
            )
            driver.switch_to.frame(iframe)
            break
        except Exception as e:
            print(f"Reintentando localización del iframe: {e}")

    # Esperar hasta que el elemento del reCAPTCHA esté presente
    checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "recaptcha-anchor"))
    )

    # Resolver el CAPTCHA
    while True:
        try:
            btn_captcha = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'recaptcha-checkbox-border'))
            )
            btn_captcha.click()
            break
        except Exception as e:
            print(f"Reintentando clic en CAPTCHA: {e}")

    # Esperar hasta que el reCAPTCHA esté marcado (aria-checked="true")
    max_attempts = 60
    attempts = 0

    while True:
        # Obtener el estado del atributo aria-checked
        is_checked = checkbox.get_attribute("aria-checked")
        if is_checked == "true":
            print("reCAPTCHA marcado. Continuando...")
            break
        elif attempts >= max_attempts:
            print("No se pudo completar el reCAPTCHA.")
            return False  
        else:
            print("Esperando que el reCAPTCHA sea marcado...")
            attempts += 1
            time.sleep(1)

    driver.switch_to.default_content()

    # Consultar después de que el reCAPTCHA esté marcado
    while True:
        try:
            btn_consultar = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'j_idt17'))
            )
            btn_consultar.click()
            break
        except Exception as e:
            print(f"Reintentando clic en consultar: {e}")

    # Espera hasta que el elemento esté presente en el DOM (hasta 10 segundos)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'form:mensajeCiudadano')))

    # Localiza el elemento por su ID y captura el texto
    mensaje_ciudadano = driver.find_element(By.ID, 'form:mensajeCiudadano')

    # Extrae el texto contenido en el elemento
    respuesta = mensaje_ciudadano.text

    return respuesta
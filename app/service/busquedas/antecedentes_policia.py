from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

def antecedentes_policia(tipo_documento, numero_documento, driver): 
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
    try:
        input_documento = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, "cedulaInput"))
        )
        input_documento.send_keys(numero_documento)
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

    #Verificar si el checkbox está marcado automáticamente
    checked_automatic = """

            let captchaCheckbox = document.querySelector('.recaptcha-checkbox');

            let isChecked = captchaCheckbox.getAttribute('aria-checked');

            if (isChecked === 'false') {
                console.log('El reCAPTCHA no está marcado automáticamente.');
                return false;
            } else {
                console.log('El reCAPTCHA está marcado automáticamente.');
                return true;
            }

        """

    checked = driver.execute_script(checked_automatic)

    if checked == False:    

        # Resolver el CAPTCHA
        intentos = 0
        max_intentos = 2

        while intentos < max_intentos:
            try:
                btn_captcha = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'recaptcha-checkbox-border'))
                )
                btn_captcha.click()
                break
            except Exception as e:
                intentos += 1
                print(f"Reintentando clic en CAPTCHA ({intentos}/{max_intentos}): {e}")

        if intentos == max_intentos:
            print("Se alcanzó el límite de intentos. Saliendo del bucle.")


        # Esperar hasta que el reCAPTCHA esté marcado (aria-checked="true")
        max_attempts = 45
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
    else:
        print("reCAPTCHA marcado automáticamente. Continuando...")

    driver.switch_to.default_content()

    # Número de intentos
    intentos = 0
    max_intentos = 3

    # Intentar hacer clic en el botón de consulta después de marcar el reCAPTCHA
    while intentos < max_intentos:
        try:
            # Intentar hacer clic con WebDriverWait
            btn_consultar = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'j_idt17'))
            )
            btn_consultar.click()
            print("Clic en el botón de consultar exitoso")
            break  # Salir del bucle si se hizo clic correctamente
        except Exception as e:
            print(f"Reintentando clic en consultar (Intento {intentos + 1}/{max_intentos}): {e}")

            # Ejecutar JavaScript para intentar hacer clic en el botón con la clase 'ui-button-text ui-c'
            resultado = driver.execute_script("""
                var respuesta = document.getElementsByClassName('ui-button-text ui-c');
                if (respuesta.length > 0) {
                    console.log('Botón encontrado, haciendo clic...');
                    respuesta[0].click();
                    return true;
                } else {
                    console.log('No hay botón con la clase especificada.');
                    return false;
                }
            """)

            # Verificar si el clic fue exitoso con JavaScript
            if resultado:
                print("Clic en el botón realizado mediante JavaScript")
                break  # Salir del bucle si el clic se realizó correctamente
            else:
                intentos += 1
                if intentos == max_intentos:
                    print("Se alcanzó el número máximo de intentos para hacer clic en el botón.")


    # Espera hasta que el elemento esté presente en el DOM (hasta 10 segundos)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'form:mensajeCiudadano')))

    # Localiza el elemento por su ID y captura el texto
    mensaje_ciudadano = driver.find_element(By.ID, 'form:mensajeCiudadano')

    # Extrae el texto contenido en el elemento
    respuesta = mensaje_ciudadano.text

    respuesta = respuesta.replace("\n", " ")

    return respuesta
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support.ui import Select

def sisben(tipo_documento, numero_documento, driver):
    driver.get("https://www.sisben.gov.co/paginas/consulta-tu-grupo.html")

    intentos_frame = 0
    # Manejar el iframe 
    while intentos_frame < 10:
        try:
            iframe = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "iframe"))
            )
            driver.switch_to.frame(iframe)
            break
        except Exception as e:
            print(f"Reintentando localización del iframe: {e}")
            intentos_frame += 1
            time.sleep(1)


    # Esperar hasta que el <select> sea visible
    select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "TipoID"))
    )
    
    # Crear objeto Select
    dropdown = Select(select_element)

    while True:
            try:
                dropdown.select_by_value("3") 
                selected_value = dropdown.first_selected_option.get_attribute("value")

                if selected_value != "-1":
                    print(f"Opción seleccionada: {dropdown.first_selected_option.text}")
                    break
                else:
                    print("Por favor, selecciona una opción válida del menú desplegable.")
                    WebDriverWait(driver, 10).until(
                        lambda d: dropdown.first_selected_option.get_attribute("value") != "-1"
                    )
            except Exception as e:
                print(f"Error al seleccionar una opción: {e}")

    # Ingresar documento
    while True:
        try:
            input_documento = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, "documento"))
            )
            input_documento.send_keys(numero_documento)
            break
        except Exception as e:
            print(f"Reintentando ingreso de documento: {e}")

    # Bajar la página
    script_scroll = """
            window.scrollBy(0, 1500);
    """

    driver.execute_script(script_scroll)

    time.sleep(3)

    # Buscar
    while True:
        try:
            btn_consultar = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.ID, 'botonenvio'))
            )
            btn_consultar.click()
            break
        except Exception as e:
            print(f"Reintentando clic en buscar {e}")

    try:
        # Espera hasta que el elemento esté presente en el DOM (hasta 10 segundos)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div[1]/div[2]/div/div[2]/div[3]/div/p')))

        # Localiza el elemento por su ID y captura el texto
        mensaje_ciudadano = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[1]/div[2]/div/div[2]/div[3]/div/p')

        # Extrae el texto contenido en el elemento 
        respuesta = mensaje_ciudadano.text

        respuesta = respuesta.replace("\n", " ")

        # salir del iframe
        driver.switch_to.default_content()

        return respuesta
    except:
        # Espera hasta que el elemento esté presente en el DOM (hasta 10 segundos)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]')))

        # Localiza el elemento por su ID y captura el texto
        mensaje_ciudadano = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]')

        print(mensaje_ciudadano)
        
        # Extrae el texto contenido en el elemento
        respuesta = mensaje_ciudadano.text

        respuesta = respuesta.replace("\n", " ")
        
        # salir del iframe
        driver.switch_to.default_content()

        return respuesta
    
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def antecedentes_policia(tipo, documento, driver):
       
     driver.get("https://antecedentes.policia.gov.co:7005/WebJudicial/")

     time.sleep(7)

     try:
          btn_aceptar_politicas = WebDriverWait(driver, 30).until(
               EC.element_to_be_clickable((By.XPATH, '//*[@id="aceptaOption:0"]'))
          )

          btn_aceptar_politicas.click()
     except Exception as e:
          print(f"Error al hacer clic en el botón de aceptar politicas {e}")
          return None
       
     time.sleep(1)

     try:
          btn_enviar = WebDriverWait(driver, 30).until(
               EC.element_to_be_clickable((By.ID, 'continuarBtn'))
          )

          btn_enviar.click()
     except Exception as e:
          print(f"Error al hacer clic en el botón de enviar politicas {e}")
          return None
       
     time.sleep(7)

     try:
          input_documento = driver.find_element(By.ID, "cedulaInput")

          input_documento.send_keys(documento)

     except Exception as e:

          print(f"Error al ingresar el documento {e}")
          return None
     
     try:
          btn_captcha = WebDriverWait(driver, 10).until(
               EC.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha-anchor"]'))
          )

          btn_captcha.click()

     except Exception as e:
          print(f"Error al hacer clic en captcha {e}")
          return None
     
     try:
          btn_consultar = WebDriverWait(driver, 10).until(
               EC.element_to_be_clickable((By.ID, 'j_idt17'))
          )

          btn_consultar.click()

     except Exception as e:
          print(f"Error al hacer clic en consultar {e}")
          return None


     input("Presione Enter para continuar...")
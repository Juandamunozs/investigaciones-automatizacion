from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

def funcion_publica(nombre_documento, driver):
    try:
        driver.get("https://www.funcionpublica.gov.co/dafpIndexerBHV/hvSigep/index")

        input_nombre = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.ID, "query"))
        )
        input_nombre.send_keys(nombre_documento)

    except Exception as e:
        print(f"Ocurrió un error al ingresar el nombre: {e}")

    try:
        btn_buscar = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.ID, "find"))
        )
        btn_buscar.click()

    except Exception as e:
        print(f"Ocurrió un error al hacer clic en el botón de búsqueda: {e}")

    try:
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "odd"))
        )

        script = """
            let respuesta = document.getElementsByClassName("odd");

            if (respuesta.length > 0) {
                console.log(respuesta[0].textContent.trim());
                return respuesta[0].textContent.trim();
            }
        """

        res = driver.execute_script(script)

        res = res.replace("\n", " ").replace("\t", "")

    except Exception as e:
        script = """
            let respuesta = document.getElementById("div-resultados-busqueda");

            if (respuesta) {
                console.log(respuesta.textContent.trim());
                return respuesta.textContent.trim();
            } 
        """

        res = driver.execute_script(script)

        res = res.replace("\n", " ").replace("\t", "")

    return res
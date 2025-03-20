import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def rama_judicial(tipo_documento, numero_documento, nombre_documento, tipo_persona, driver):
    driver.get("https://consultaprocesos.ramajudicial.gov.co/Procesos/NombreRazonSocial")

    
    try:
        script_tipo_proceso = """ 
        
            todoProcesos = document.evaluate('/html/body/div[1]/div/div[3]/main/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/div[1]/div/div[2]/div/div', document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
            if (todoProcesos.snapshotLength > 0) {
                todoProcesos.snapshotItem(0).click();  
            } 
        """

        driver.execute_script(script_tipo_proceso)

    except:
        print("Error en decidir tipo de proceso")

    
    try:
        script_tipo_sppiner= """ 
            persona_natural = document.getElementById('input-72');
            if (persona_natural) {
                persona_natural.click();
                console.log('Persona natural seleccionada')
            } else {
                console.log('No se encontró el elemento persona natural');
            }
        """
        driver.execute_script(script_tipo_sppiner)

    except:
        print("Error en decidir abrir spinner")

    time.sleep(1)

    try:

        if tipo_persona == "NATURAL":
            xpath = '/html/body/div[1]/div[2]/div/div[1]/div/div'
        elif tipo_persona == "JURIDICA":
            xpath = '/html/body/div[1]/div[2]/div/div[2]/div/div'
        else:
                print("Tipo de persona no válido")

        script_tipo_persona= f""" 
            tipo_persona = document.evaluate('{xpath}', document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
            
            console.log(tipo_persona);  

            if (tipo_persona.snapshotLength > 0) {{
                tipo_persona.snapshotItem(0).click(); 
                console.log('Tipo de persona seleccionado');
            }} else {{
                console.log('No se encontró el tipo de persona');
            }}
        """
        driver.execute_script(script_tipo_persona)

    except:
        print("Error en decidir tipo de persona")

    try:
        script_documento = f""" 
            input_nombre = document.getElementById('input-78')

                input_nombre.click()
                
                input_nombre.focus()

                input_nombre.value = '{nombre_documento}' 

                input_nombre.dispatchEvent(new Event('input'))
                
                console.log('Valor insertado correctamente')

        """

        driver.execute_script(script_documento)

    except:
        print("Error en ingresar documento")

    time.sleep(1)

    try:
        script_btn_consultar = f""" 
            boton_consultar = document.getElementsByClassName('v-btn v-btn--is-elevated v-btn--has-bg theme--light v-size--default success mt-2 mx-2 font-weight-bold');

            if (boton_consultar.length > 0) {{
                boton_consultar[0].click();
                console.log('Botón clickeado');
            }}

        """

        driver.execute_script(script_btn_consultar)

    except:
        print("Error al boton consultar")
        

    try:
        dialogo_disponible = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'v-alert__content'))
        )
        
        script_resultado = """ 
            let respuesta = document.getElementsByClassName('pl-1');
            if (respuesta.length > 0) {
                return respuesta[0].textContent;  
            } else {
                return 'No se encontraron elementos con la clase "pl-1"'; 
            }
        """
        
        respuesta = driver.execute_script(script_resultado)

    except:
        print("Error al obtener respuesta del dialogo")

    try:
        if respuesta == "La consulta no generó resultados, por favor revisar las opciones ingresadas e intentarlo nuevamente.":
            return respuesta + "(Posiblemente no tiene asuntos judiciales)"
        
    except:
        print("Error al devolver la respuesta de sin resultados")

    try:

        if respuesta == "Se han encontrado varios registros con el mismo nombre o razón social. Por favor consulte todos sus procesos.":
            
            try:
                script_cerrar_dialogo = """
                    var btn = document.querySelector('.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--dark.v-size--default.leading');
                    if (btn) {
                        btn.click();  
                    } else {
                        console.log('Botón de cerrar no encontrado.');
                    }
                """
                driver.execute_script(script_cerrar_dialogo)
            except Exception as e:
                print(f"Error al cerrar el diálogo: {e}")

           
            time.sleep(1)

            try:
                script_resultado = """
                    let contenidoTablas = [];
                    let tablas = document.getElementsByTagName('table');
                    
                    if (tablas.length > 0) {
                        for (let tabla of tablas) {
                            let filas = tabla.getElementsByTagName('tr');
                            let tablaContenido = [];

                            for (let fila of filas) {
                                let celdas = fila.getElementsByTagName('td');
                                let filaContenido = [];

                                for (let celda of celdas) {
                                    filaContenido.push(celda.textContent.trim());
                                }

                                if (filaContenido.length > 0) {
                                    tablaContenido.push(filaContenido);
                                }
                            }

                            if (tablaContenido.length > 0) {
                                contenidoTablas.push(tablaContenido);
                            }
                        }
                    }

                    return contenidoTablas;
                """
            except:
                print("Error al extraer contenido de las tablas js")
            
            res = driver.execute_script(script_resultado)

            return res
        
        else:
            return respuesta + "(respuesta desconocida)"
    
    except Exception as e:
        print(f"Error al obtener resultado de los delitos: {e}")
        return None

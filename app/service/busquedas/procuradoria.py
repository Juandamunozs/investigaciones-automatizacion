# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# def procuradoria(tipo, documento, driver):
#     try:
#         # Abrir la primera página
#         driver.get("https://www.procuraduria.gov.co/Pages/Consulta-de-Antecedentes.aspx")

#     except Exception as e:
#         print("Error al abrir la página de la procuraduría: ", e)

#     try:

#         script_tipo_documento = f"""

#         try {{
#             let selectElement = document.getElementById('ddlTipoID'); // Obtener el select por id
#             selectElement.value = '1'; // Establecer el valor de la opción deseada (1)
#         }} catch (e) {{
#             console.log("Error al seleccionar el valor:", e);
#         }}

#         """

#         driver.execute_script(script_tipo_documento)
    
#     except Exception as e:
#         print(f"Error al generar el script: {e}")

#     try:
#         script_input = f"""
#         try {{
#             let inputDocumento = document.getElementById('txtNumID');
            
#             if (inputDocumento) {{
#                 inputDocumento.value = '{documento}'; 
#             }} else {{
#                 console.log("Campo no encontrado");
#             }}
#         }} catch (e) {{
#             console.error("Error al ejecutar el script:", e);
#         }}
#         """

#         driver.execute_script(script_input)

#     except Exception as e:
#         print(f"Error al generar el script: {e}")



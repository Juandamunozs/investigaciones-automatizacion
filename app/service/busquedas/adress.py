# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# import time
# from env.env import dir_imagen_catpcha

# def adress(tipo, documento, driver):
#     try:
#         # Acceder a la URL
#         driver.get("https://aplicaciones.adres.gov.co/bdua_internet/Pages/ConsultarAfiliadoWeb.aspx")

#         txt_input = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.ID, "txtNumDoc"))
#         )

#         script = f"""document.getElementById('txtNumDoc').value = '{documento}';"""
#         driver.execute_script(script)

#         captcha_image = """
#         var captchaImage = document.getElementById('Capcha_CaptchaImageUP');

#         var captchaImageUrl = captchaImage.src;

#         var link = document.createElement('a');
#         link.href = captchaImageUrl;  // Establecer el URL de la imagen como destino
#         link.download = 'captcha_image.png';  // Nombre del archivo a descargar

#         link.click();

#     """
#         driver.execute_script(captcha_image)
#         time.sleep(5)

#         num_captcha = captcha(dir_imagen_catpcha)

#         script_num_captcha = f"""
#             document.getElementById('Capcha_CaptchaTextBox').value = {num_captcha};
#         """

#         driver.execute_script(script_num_captcha)

#         script_btn_consultar = """
#             document.getElementById('btnConsultar').click();
#         """

#         driver.execute_script(script_btn_consultar)

#         input("Parar script")


#     except Exception as e:

#         print(f"Ocurrió un error: {e}")


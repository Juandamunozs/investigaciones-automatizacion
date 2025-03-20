# #Vericar el hash
# import bcrypt

# # El hash que almacenaste en la base de datos
# stored_hash = "$2b$12$zR/fWoIUslsaPhEQQCC1Q.AifKj/o6T3vrsvovdpCGHEuVif86FFy"

# # La contraseña ingresada por el usuario
# password = "1234"  # Sustituir por la contraseña que el usuario ingresa

# # Verificar si la contraseña coincide con el hash
# if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
#     print("La contraseña es correcta")
# else:
#     print("La contraseña es incorrecta")

# to_email = ""

# domain = to_email.split('@')[1]


# dicc_domain = {

#     "gmail.com": "smtp.gmail.com",
# }

# print(domain)
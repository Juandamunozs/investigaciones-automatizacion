from pydantic import BaseModel

# Modelo de datos para recibir los datos a investigar
class SolicitudDocumento(BaseModel):
    tipo_documento: str
    numero_documento: str
    nombre_documento: str
    tipo_persona: str
    email_informe: str

# Modelo de datos para autenticar usuarios
class UsuarioLogin(BaseModel):
    nombre_usuario: str
    contrasena: str

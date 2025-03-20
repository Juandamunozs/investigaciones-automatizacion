from fastapi import APIRouter, HTTPException
from service.investigacion import investigar_documento
from module.token import token_utils
from schemas.schemas import SolicitudDocumento, UsuarioLogin
import time
from typing import Dict

# Crear un router para agrupar las rutas
router = APIRouter()

@router.post("/buscar-documento", summary="Buscar información con los datos de la persona", tags=["Documentos"])
# def buscar_documento(data: SolicitudDocumento, user_auth: str = Depends(token_utils.verificar_token)) -> Dict: # Con autenticación
def buscar_documento(data: SolicitudDocumento) -> Dict: # Sin autenticación
    
    inicia_analisis = time.time()

    tipo_documento = data.tipo_documento
    numero_documento = data.numero_documento
    nombre_documento = data.nombre_documento
    tipo_persona = data.tipo_persona
    email_informe = data.email_informe

    try:
        # Aquí se obtiene la información o el análisis del documento
        document_info = investigar_documento(tipo_documento, numero_documento, nombre_documento, tipo_persona, email_informe)
        
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"No se encontró información para el documento {tipo_documento} {numero_documento}: {str(e)}")
    
    finaliza_analisis = time.time()
    tiempo_analisis = finaliza_analisis - inicia_analisis

    return {
        "tipo_documento": tipo_documento,
        "numero_documento": numero_documento,
        "nombre_documento": nombre_documento,
        "documento_info": document_info,
        "tiempo_analisis": f"{tiempo_analisis:.2f} s"
    }

# Ruta para autenticar usuarios
@router.post("/login", summary="Autenticar usuario para investigar", tags=["Login"])
async def login(usuario: UsuarioLogin):
    usuario_valido = token_utils.authenticate_user(usuario.nombre_usuario, usuario.contrasena)

    if not usuario_valido:
        raise HTTPException(
            status_code=401,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Obtener rol del usuario
    rol = token_utils.obtener_rol(usuario.nombre_usuario)

    # Crear token de acceso
    token_acceso = token_utils.create_access_token(data={"sub": usuario.nombre_usuario, "role": rol})

    return {"token": token_acceso, "type": "bearer"}

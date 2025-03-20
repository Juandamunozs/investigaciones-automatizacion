import json

# Función para limpiar los caracteres de escape en el JSON
def limpiar_json(respuesta):
    try:
        respuesta_decodificada = json.loads(respuesta)
        
        respuesta_limpia = json.dumps(respuesta_decodificada, ensure_ascii=False)
        
        respuesta_limpia = respuesta_limpia.replace("\\", "")  
        respuesta_limpia = respuesta_limpia.replace("\"{", "")

        return respuesta_limpia
    except Exception as e:
        print(f"Error al limpiar JSON: {e}")
        return respuesta  
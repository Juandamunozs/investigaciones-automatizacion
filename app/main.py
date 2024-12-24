from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from service.investigacion import investigar_documento
import time
import json

# Crear la aplicación FastAPI
app = FastAPI()

# Modelo de datos para recibir el número y tipo de documento
class DocumentRequest(BaseModel):
    document_type: str
    document_number: str

@app.post("/buscar-documento", summary="Buscar información de documento", tags=["Documentos"])
def buscar_documento(data: DocumentRequest) -> Dict[str, str]:
    """
    Endpoint que recibe un tipo y número de documento y utiliza la función investigar_documento para obtener información relacionada.

    **Parámetros:**
    - `document_type` (str): Tipo de documento (ejemplo: "CC", "TI").
    - `document_number` (str): Número del documento.

    **Respuesta:**
    - Devuelve un diccionario con la información encontrada del documento.

    **Errores:**
    - Si no se encuentra información del documento, devuelve un error 404.

    **Ejemplo de uso:**
    ```json
    {
        "document_type": "CC",
        "document_number": "123456789"
    }
    ```

    Respuesta esperada:
    ```json
    {
        "document_type": "CC",
        "document_number": "123456789",
        "document_info": "Detalles del documento encontrado"
    }
    """

    inicia_analisis = time.time()

    document_type = data.document_type
    document_number = data.document_number

    try:
        # Aquí se obtiene la información o el análisis del documento
        document_info = investigar_documento(document_type, document_number)
        
        # Asegúrate de que document_info sea una cadena de texto (string)
        if not isinstance(document_info, str):
            document_info = json.dumps(document_info)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"No se encontró información para el documento {document_type} {document_number}: {str(e)}")
    
    finaliza_analisis = time.time()

    tiempo_analisis = finaliza_analisis - inicia_analisis

    return {
        "document_type": document_type,
        "document_number": document_number,
        "document_info": document_info,
        "tiempo_analisis": f"{tiempo_analisis:.2f} s"
    }


"""

Para ejecutar la aplicación, puedes utilizar el siguiente comando:

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

"""
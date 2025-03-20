from weasyprint import HTML
from service.pdf.plantillaPDF import generar_html
from env.env import dir_pdf

def crear_pdf(dic_investigaciones, nombre_documento, tipo_documento, numero_documento, tipo_persona):

    ruta_pdf = f"{dir_pdf}\\{tipo_documento}_{numero_documento}.pdf"
       
    html_content = generar_html(dic_investigaciones, nombre_documento, tipo_documento, numero_documento, tipo_persona) 

    # Generar el PDF con WeasyPrint
    HTML(string=html_content).write_pdf(ruta_pdf)
    print(f"PDF '{ruta_pdf}' generado exitosamente.")


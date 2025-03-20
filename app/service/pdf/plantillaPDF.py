from module.time.time import obtener_hora_completa, obtener_dia_texto, obtener_dia_numero, obtener_anio, obtener_mes_numero, obtener_mes_texto

def generar_html(dic_investigaciones, nombre_documento, tipo_documento, numero_documento, tipo_persona):
    info = dic_investigaciones.get("info", {})

    hora = obtener_hora_completa()
    dia_texto = obtener_dia_texto()
    dia_numero = obtener_dia_numero()
    anio_numero = obtener_anio()
    mes_texto = obtener_mes_texto()

    fecha_completa = f"{dia_texto} {dia_numero} de {mes_texto} del {anio_numero} a las {hora}"

    def generar_tabla(datos, titulo):
        if not datos or not isinstance(datos, list):
            return f"<p>No disponible - Posiblemente no tiene demandas - Verificar manualmente.</p>"
        
        tabla = f"""
        <table border="1" cellspacing="0" cellpadding="8" style="width:100%; border-collapse: collapse;">
            <thead>
                <tr>
                    {"".join(f"<th>{col}</th>" for col in datos[0].keys())}
                </tr>
            </thead>
            <tbody>
                {"".join("<tr>" + "".join(f"<td>{fila[col]}</td>" for col in fila) + "</tr>" for fila in datos)}
            </tbody>
        </table>
        """
        return tabla

    return f"""
    <html>
    <head>
        <meta charset="utf-8">
        <title>Informe de Investigación</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f0f4f8;
                margin: 0;
                padding: 0;
                color: #444;
            }}
            .container {{
                width: 85%;
                margin: 40px auto;
                padding: 25px;
                background-color: #ffffff;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                border-radius: 12px;
                font-size: 14px;
                line-height: 1.8;
            }}
            h1 {{
                color: #4CAF50;
                font-size: 28px;
                text-align: center;
                margin-bottom: 20px;
                font-weight: 600;
                text-transform: uppercase;
            }}
            h2 {{
                font-size: 20px;
                color: #333;
                margin-top: 15px;
                font-weight: 500;
                border-bottom: 2px solid #4CAF50;
                padding-bottom: 5px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 10px;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #4CAF50;
                color: white;
            }}
            .footer {{
                text-align: center;
                font-size: 12px;
                color: #888;
                margin-top: 40px;
                padding-top: 20px;
                border-top: 2px solid #e2e2e2;
            }}
            .note {{
                font-size: 13px;
                color: #999;
                margin-top: 15px;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Informe de Investigación</h1>

            <div>
                <h2>Datos del Investigado</h2>
                <table>
                    <tr><td><strong>Nombre:</strong></td><td>{nombre_documento}</td></tr>
                    <tr><td><strong>Tipo de Documento:</strong></td><td>{tipo_documento}</td></tr>
                    <tr><td><strong>Número de Documento:</strong></td><td>{numero_documento}</td></tr>
                    <tr><td><strong>Tipo de Persona:</strong></td><td>{tipo_persona}</td></tr>
                    <tr><td><strong>Hora de la Consulta:</strong></td><td>{fecha_completa}</td></tr>
                </table>
            </div>

            <div>
                <h2>Antecedentes Policiales</h2>
                <p>{info.get("antecedentes_policia", "No disponible")}</p>
            </div>

            <div>
                <h2>Antecedentes de Tránsito</h2>
                <p>{info.get("antecedentes_transito", "Antecedentes de Tránsito")}</p>
            </div>

            <div>
                <h2>SISBEN</h2>
                <p>{info.get("sisben", "No disponible")}</p>
            </div>

            <div>
                <h2>Rama Judicial</h2>
                {generar_tabla(info.get("rama_judicial"), "Rama Judicial")}
            </div>

            <div>
                <h2>Función Pública</h2>
                <p>{info.get("funcion_publica", "No disponible")}</p>
            </div>

            <div class="footer">
                <p>Informe generado el <strong>{fecha_completa}</strong></p>
                <p class="note">Este informe es confidencial y está destinado exclusivamente para el uso autorizado.</p>
            </div>
        </div>
    </body>
    </html>
    """

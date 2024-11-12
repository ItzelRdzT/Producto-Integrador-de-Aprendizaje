#API IP ABUSE DATABASE
import logging
import requests
import hashlib
import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
url= "https://api.abuseipdb.com/api/v2/check"

#AQUÍ SE INGRESA LA URL EN ESTA CASO ES UNA YA PROPORCIONADA
api_key="8814413cd22d6467db4d1cdb1c1bb5e6661d6b9c9b8d1672826df996a0d95ca66a8d6ff2b1e74eaa"
#SE INGRESA EL API KEY, EN ESTA OCASIÓN SE ELIGIO UNA PREDETERMINADA
def busqueda_ip(ip):
    headers = {
    'Accept': 'application/json',
    'Key': api_key
    }
#CREAMOS EL DICCIONARIO HEADERS, 'ACCEPT' RECIBE UNA RESPUESTA EN FORMATO JSON
#Y 'KEY' AUTENTICA LA SOLICITUD
    params = {
        'ipAddress': ip,
        'maxAgeInDays': 30
        }
#CREAMOS EL DICCIONARIO PARAMS, 'IPADDRESS' SE ENCUENTRA LA DIRECCIÓN IP QUE SE QUIERE BUSCAR
#'MAXAGEINDAYS' PONE UN LIMITE DE 30 DÍAS PARA EL INGRESO DE INFORMACIÓN
    response = requests.get(url, headers=headers, params=params)
#RESPONSE ALMACENA INFORMACIÓN DE LA URL, DONDE TAMBIEN SE LLAMAN LA INFORMACIÓN DE LOS 2 DICCIONARIOS HECHOS
    if response.status_code == 200:
        logging.info("TODO SALIÓ DE FORMA EXITOSA")
        return response.json()
#SI EL STATUS DE RESPONSE ES UN 200 EL CODIGO FUNCIONA Y SE LOGRA LLAMAR A LA API REGRESANDO ESTA INFORMACIÓN EN FORMATO JSON
    else:
        logging.error("HUBO UN ERROR EN LA CONSULTA")
        return None
#SI NO SE MARCA 200 ENTONCES NO SE PUDO REALIZAR UNA CONEXIÓN CON EL API Y NO NOS REGRESARA NADA
def consulta_ip():
    ip=input("INGRESE LA IP QUE BUSCA CONSULTAR: ")
    respuesta=busqueda_ip(ip)
    #print("EL RESULTADO DE LA BUSQUEDA: ", respuesta)


#pedazo del codigo para el reporte de html
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Api Abuse</title>
    </head>
    <body>
    <style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Open Sans';
    }
    body {
        background-color: #f4f4f9;
        padding: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
    }
    .contenido-reporte {
        width: 100%;
        max-width: 600px;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        padding: 20px;
        text-align: center;
    }
    h1 {
        font-size: 1.8rem;
        color: #757373;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
    }
    th, td {
        padding: 10px;
        border: 1px solid #ddd;
        text-align: center;
    }
    th {
        background-color: #757373;
        color: white;
    }
    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    </style>
    <div class="contenido-reporte">
    <h1> REPORTE DE LA API ABUSE DATABASE</h1>
    """
    if respuesta:
        data = respuesta.get("data", {})
        html += f"""
        <table>
            <tr><th>IP Consultada</th><td>{data.get("ipAddress", "No disponible")}</td></tr>
            <tr><th>Pais</th><td>{data.get("country", "No disponible")}</td></tr>
            <tr><th>Dominio</th><td>{data.get("domain", "No disponible")}</td></tr>
            <tr><th>Total de reportes</th><td>{data.get("totalReports", "No disponible")}</td></tr>
            <tr><th>Último reporte</th><td>{data.get("lastReportedAt", "No disponible")}</td></tr>
        </table>
        """
    else:
        html += """<p>Error: No se pudo obtener información sobre la IP.</p>
    </div>
    </body>
    </html>
    """
    with open("reporte_Ip_Abuse.html","w") as file:
        file.write(html)
    
    input("Presiona Enter para volver al menú principal...")

#AQUI MOSTRAREMOS LOS DATOS QUE SE IMPRIMIRAN EN PANTALLA
def calcular_hash(respuesta):
    hash_md5=hashlib.md5()
    hash_md5.update(respuesta.encode('utf-8'))
    return hash_md5.hexdigest()

Script= "API_ABUSE"
Date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
Reporte="reporte_Ip_Abuse.html"
ubicacion="reporte"
print(Script)
print(Date)
print(Reporte)
print(f"La ubicacion de este script es: {ubicacion}")

#EN ESTA FUNCIÓN SE INGRESA LA IP Y SE MANDA A LLAMAR LA PRIMERA FUNCIÓN Y SE IMPRIMIRA LA RESPUESTA DE LA FUNCIÓN
consulta_ip()



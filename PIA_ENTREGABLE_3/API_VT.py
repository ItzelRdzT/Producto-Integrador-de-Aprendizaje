#Modulos que necesitaremos para nuestro script
import hashlib
from virus_total_apis import PublicApi
import logging
import hashlib
import datetime
 
###Equipo8###
 
#Configuracion del logging
logging.basicConfig(filename='hibpINFO.log', format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %H:%M;%S", level = logging.INFO )

#En esta unica funcion tomaremos la API de VirusTotal donde analizaremos si existe algun malware en nuestros archivos.
def api_archive():
    try:
        logging.info('En este script analizaremos los archivos de la carpeta donde nos encontramos, usando un API llamada VirusTotal')
        logging.info('Script creado por el equipo 8')
        #reporte en html
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Api Shodan</title>
        </head>
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
        .reporte-container {
            max-width: 600px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px; text-align: center;
        }
        h1 {
            font-size: 1.8rem;
            color: #757373;
        }
        .message-error{
            margin-top: 10px;
            margin-bottom: 20px;
            font-size: 1.2rem;
            color: #f91010  ;
        }

        .message {
            margin-top: 10px;
            margin-bottom: 20px;
            font-size: 1.2rem;
            color: #7ffb66 ;
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
            background-color: #BA989A;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        </style>
        <body>
        <div class='reporte-container'>
        <h1><center>REPORTE DE ARCHIVOS MALICIOSOS</center></h1>
        """
 
        #API-KEY personal 
        api_key = '191cc16e7cd5d7b19fed80bcbcd4a6b5560c6c49958b8f87d80dc857f031b8fb'
        api = PublicApi(api_key)
        #Se solicita un reporte y se registra la respuesta de la api
        logging.info('El archivo debe estar en la misma carpeta que este script.')
        archive = input("Escribe el nombre del archivo que quieras analizar:")
        logging.info(f"Archivo ingresado: {archive}")
 
        #Validacion del nombre del archivo 
        if archive.isnumeric():
            logging.warning('El archivo debe contener letras y números')
            return
        #El programa lee el archivo y calcula su hash
        with open(archive, "rb") as file:
            file_hash = hashlib.md5(file.read()).hexdigest()
        logging.info(f"Hash del archivo: {file_hash}")
 
        #En esta parte solicitamos la respuesta de la API
        response = api.get_file_report(file_hash)
        logging.info(f"Respuesta de la API: {response}")
 
        #Aqui se verifica la respuesta de la API, se iguala a 200 y si llega a ser mayor a 0 lo registra como malicioso
        if response["response_code"] == 200:
            results = response.get("results", {})
            positives = results.get("positives", 0)
            if positives > 0:
                logging.info("Detectamos un archivo malicioso.")
                html+= f"""<p class= 'message-error'>Detectamos que el archivos es malicioso</p>
                <table>
                <tr><th>Archivo ingresado</th><td>{archive}</td></tr>
                <tr><th>Hash del archivo</th><td>{file_hash}</td></tr>
                </table>

                """
            else:
                logging.info("El archivo es seguro.")
                html += f"""<p class='message'>EL ARCHIVO ES SEGURO:D</p>
                """
                
        #Si no se ejecuta bien nos manda un mensaje de error.
        else:
            logging.error("No se pudo realizar el análisis correctamente.")
            html += """<p class="message-error">Error en el análisis del archivo.</p>"""

    except FileNotFoundError:
        logging.error(f"El archivo '{archive}' no existe en la carpeta actual.")
        html += f"<p class='message-error'>Error: El archivo '{archive}' no se encontró en el directorio.</p>"

        html += """</div>
        </body>
        </html>"""

        # Guardar el archivo HTML
        with open("Reporte_archivos_maliciosos.html", "w") as file:
            file.write(html)

    except (RuntimeError, FileNotFoundError) as e:
        logging.critical(f"El programa no ha podido ejecutarse. Error: {e}")

    input("Presiona Enter para volver al menú principal...")

#AQUI MOSTRAREMOS LOS DATOS QUE SE IMPRIMIRAN EN PANTALLA
def calcular_hash(response):
    hash_md5=hashlib.md5()
    hash_md5.update(response.encode('utf-8'))
    return hash_md5.hexdigest()
Script= "API_VT"
Date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
Reporte="Reporte_archivos_maliciosos.html"
ubicacion="ruta al reporte"
print(Script)
print(Date)
print("La informacion se ha guardado en: {Reporte}")
print(f"La ubicacion de este script es: {ubicacion}")

api_archive()



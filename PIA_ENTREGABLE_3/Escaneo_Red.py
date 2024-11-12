import subprocess
from manuf import manuf
import logging
 
# Configuración del logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s - %(message)s')
 
# En esta función mandaremos un ping a nuestra IP y verificamos si nos llega alguna respuesta
def ping_host(ip):
    try:
        response = subprocess.run(
            ['ping', '-n', '1', '-w', '500', ip],
            stdout=subprocess.PIPE)
        return "TTL=" in str(response.stdout)
    except Exception as e:
        # En caso de que no recibamos respuesta de la IP, nos llegará un aviso de error
        logging.error(f'No recibimos respuesta por parte de la IP: {e}')
 
# En esta función obtendremos la información MAC de los dispositivos conectados a nuestra IP
def get_mac(ip):
    try:
        result = subprocess.run(
            ['arp', '-a', ip],
            stdout=subprocess.PIPE,
            text=True)
        lines = result.stdout.split('\n')
        # Recorremos línea por línea extrayendo la información MAC en nuestra IP
        for line in lines:
            if ip in line:
                mac = line.split()[1]
                return mac
        # Si no encontramos ninguna, no regresamos ninguna información
        return None
    except Exception as e:
        # En caso de excepción, nos manda un aviso
        logging.error(f'No se encontró ninguna MAC: {e}')
 
# En esta función obtendremos información acerca del fabricante de los dispositivos conectados a nuestra IP
def get_manufacturer(mac):
    try:
        p = manuf.MacParser()
        return p.get_manuf(mac)
    except Exception as e:
        # Si no encontramos ninguno, nos manda un aviso
        logging.error(f'Hubo un error en la obtención del proveedor: {e}')
 
# Esta función escaneará un rango de direcciones IP haciendo ping en cada una y nos muestra en pantalla toda la información
def net_scann(ip_base, start, end):
    live_hosts = []
    for i in range(start, end + 1):
        ip = f"{ip_base}.{i}"
        try:
            if ping_host(ip):
                mac = get_mac(ip)
                if mac:
                    manufacturer = get_manufacturer(mac)
                    live_hosts.append({'IP': ip, 'MAC': mac, 'Manufacturer': manufacturer})
        except Exception as e:
            logging.error(f'No se pudo realizar bien el escaneo en {ip}: {e}')
    # Nos muestra cuántos hosts están activos en nuestra red
    return live_hosts
 
# Solicitamos la información necesaria al usuario para poder hacer el escaneo de dispositivos en nuestra red
def run_scan():
    ip_base = input("Introduce la base de la IP: ")
    if not ip_base.replace('.', '').isnumeric():
        logging.warning('La base de la IP debe contener solo números y puntos en el formato correcto, como 192.168.0')
        return
    try:
        start = int(input("Introduce el número inicial del rango: "))
        end = int(input("Introduce el número final del rango: "))
    except ValueError:
        logging.warning('El rango debe ser numérico.')
        return
 
    live_hosts = net_scann(ip_base, start, end)
    if live_hosts:
        for host in live_hosts:
            print(f"IP: {host['IP']}, MAC: {host['MAC']}, Fabricante: {host['Manufacturer']}")
    else:
        print("No se detectaron hosts vivos.")
 
    input("Presiona Enter para volver al menú principal...")

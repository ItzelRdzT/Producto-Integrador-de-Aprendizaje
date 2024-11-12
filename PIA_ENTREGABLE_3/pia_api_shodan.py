import shodan
import getpass
import logging

#configuracion logging
logging.basicConfig(filename='hibpINFO.log', format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %H:%M;%S", level = logging.INFO )

#funcion que busca la informacion de los dispositivos y sus vulnerabilidades 
def results(framework):
    try:
        #realiza la busqueda en shodan
        query = motor.search(framework)
        print(f"Total de resultados: {query['total']}")
        logging.info(f"Total de resultados: {query['total']}")

        #for para iterar sobre cada dispositivo host en el diccionario query; muestra la ip, puerto, organizacion y numero de sistema autonomo
        for host in query['matches']:
            print(f"IP: {host['ip_str']}")
            logging.info(f"IP: {host['ip_str']}")
            print(f"Puerto: {host['port']}")
            logging.info(f"Puerto: {host['port']}")
            print(f"ORG: {host.get('org', 'Desconocido')}")
            logging.info(f"ORG: {host.get('org', 'Desconocido')}")
            print(f"ASN: {host.get('asn', 'No disponible')}")
            logging.info(f"ASN: {host.get('asn', 'No disponible')}")

           #itera sobre el diccionario 'location' dentro de host, mostrando cada clave y su valor
            for clave, valor in host['location'].items():
                print(f"{clave}: {valor}")
                logging.info(f"{clave}: {valor}")

            #si hay vulnerabilidades, entra al if e itera sobre cada uno para mostrarlo
            if 'vulns' in host:
                for cve in host['vulns']:
                    print(f"Vulnerabilidades: {cve}")
                    logging.info(f"Vulnerabilidades: {cve}")
            else:
                print('No se encontraron vulnerabilidades')
                logging.info('no se encontraron vulnerabilidades')

            print("="*50, "\n")

    except shodan.APIError as e:
        print(f"Error en la búsqueda: {e}")
        logging.error(f"error en la busqueda{e}")
#-----------------------
#variables
        
    apikey = getpass.getpass(prompt="Ingresa el apikey: ")
#inicializo para poder interactuar con la api
    motor = shodan.Shodan(apikey)
    framework = input('¿Con qué tipo de framework desea trabajar?: ')
    results(framework)
input("Presiona Enter para volver al menú principal...")

#SCRIPT PRINCIPAL
import API_ABUSE
import pia_api_shodan
import Escaneo_Red
import logging
import API_VT
# Configuración del logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
def analizar_archivo():
    import API_VT
    API_VT.api_archive()
    input("Presiona Enter para volver al menú principal...")
def escanear_red():
    import Escaneo_Red
    Escaneo_Red.run_scan()
    input("Presiona Enter para volver al menú principal...")
def abuse():
    import API_ABUSE
    API_ABUSE.consulta_ip()
    input("Presiona Enter para volver al menú principal...")
def shodan():
    import pia_api_shodan
    pia_api_shodan()
    input("Presiona Enter para volver al menú principal...")
def ssh():
    import pia_ssh
    pia_ssh()
    input("Presiona Enter para volver al menú principal...")
def mostrar_menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Analizar archivo con VirusTotal")
        print("2. Escanear red")
        print("3. Abuse")
        print("4. Shodan")
        print("5. Ssh")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            analizar_archivo()
        elif opcion == '2':
            escanear_red()
        elif opcion == '3':
            abuse()
        elif opcion =='4':
            shodan()
        elif opcion =='5':
            ssh()
        elif opcion =='6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    mostrar_menu()

#!/bin/bash

read -p "Introduce la IP a escanear: " ip
if [[ ! "$ip" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "Error: La IP introducida no es válida."
    exit 1
fi
while true; do
    echo -e "\n1) Escaneo rápido"
    echo "2) Escaneo normal"
    echo "3) Escaneo silencioso"
    echo "4) Escaneo de servicios y versiones"
    echo "5) Salir"
    read -p "Seleccione una opción: " opcion
    
    case $opcion in
        1) 
          clear && echo -e "Esperando" 
          if nmap -p-  --open --min-rate 5000 -T5 -sS -Pn -n -v "$ip" > escaneo_rapido.txt; then
          	echo -e "Reporte generado: escaneo_rapido"
          else
          	echo "Error en el reporte"
          fi
          ;;
        2) 
          clear && echo -e "Esperando" 
          if nmap -p-  --open "$ip" > escaneo_normal.txt; then 
          	echo -e "Reporte generado: escaneo_normal.txt"
          else
          	echo "Error en el escaneo"
          fi
          ;;
        3) 
          clear && echo -e "Esperando" 
          if nmap -p-  -T2 -sS -Pn -f "$ip" > escaneo_silencioso.txt; then
          	echo -e "Reporte generado: escaneo_silencioso.txt"
          else
          	echo "Error en el escaneo"
          fi
          ;;
        4) 
          clear && echo -e "Esperando" 
          if nmap -sV -sC "$ip" > escaneo_servicios.txt; then 
          	echo -e "Reporte generado: escaneo_servicios.txt"
          else
          	echo "Error en el reporte"
          fi
          ;;
        5) 
          break
          ;;
        *) 
          echo -e "El parámetro no es válido."
          ;;
    esac
done

<#
SYNOPSIS
    ESTE SCRIPT FUNCIONA COMO UN MENU PARA PODER ELEGIR 1 DE LOS 4 MODULOS HECHOS
DESCRIPCIÓN
    function hashes: esta función importa el modulo que analiza los hashes
    function oculto: esta función importa el modulo que muestra las funciones ocultas de los componentes de la computadora
    function sistemas: esta función importa el modulo que manda los hashes a un api
    function op: esta función importa el modulo que muestra los permisos otorgados a un archivo
    Write-Output "SELECCIONE UNA OPCIÓN: ": imprime el mensaje de elección
    Write-Output "1. FUNCIÓN HASHES": imprime cual es la primera opción del menú
    Write-Output "2. FUNCIÓN ARCHIVOS OCULTOS": imprime cual es la segunda opción del menú
    Write-Output "3. FUNCIÓN SISTEMAS": imprime cual es la tercera opción del menú
    Write-Output "4. FUNCIÓN OPCIONAL": imprime cual es la cuarta opción del menú
    $ELECCIÓN = Read-Host "INTRODUCE UNA OPCIÓN": con esto el usuario puede ingresar de forma numerica una de las opciones del menú
    SWITCH ($ELECCION){
    "1" {hashes}
    "2" {oculto}
    "3" {sistemas}
    "4" {op}
    default {Write-Output "OPCIÓN NO VALIDA"}
    }: este switch funciona como un if que permite elegir que opción sera seleccionada para que se pueda ejecutar
#>
function hashes{
    Import-Module -name "C:\Users\andre\OneDrive\Documentos\PIAprograc.psm1"
}
function oculto{
    Import-Module -name "C:\Users\andre\OneDrive\Documentos\PS\recursos.psm1"
}
function sistemas{
    Import-Module -name "C:\Users\andre\OneDrive\Documentos\PS\listadoarchivos.psm1"
}
function op{
    Import-Module -name "C:\Users\andre\OneDrive\Documentos\ADICION.ps1"
}

Write-Output "SELECCIONE UNA OPCIÓN: "
Write-Output "1. FUNCIÓN HASHES"
Write-Output "2. FUNCIÓN ARCHIVOS OCULTOS"
Write-Output "3. FUNCIÓN SISTEMAS"
Write-Output "4. FUNCIÓN OPCIONAL"
$ELECCION = Read-Host "INTRODUCE UNA OPCIÓN"

SWITCH ($ELECCION){
    "1" {hashes}
    "2" {oculto}
    "3" {sistemas}
    "4" {op}
    default {Write-Output "OPCIÓN NO VALIDA"}
}
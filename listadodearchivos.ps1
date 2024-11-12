Set-StrictMode -Version 2.0


function Get-HiddenFolder {
    param (
        [string]$folder
    )

    try {
        $folder = Read-Host "Ingrese la carpeta que quiere revisar"
        $hidden = Get-ChildItem $folder -Hidden -ErrorAction "Stop"
        if ($hidden) {
            Write-Host "Archivos ocultos encontrados:"
            $hidden | Format-List
            } else {
            Write-Host "No se encontraron archivos ocultos en la carpeta."
        }
    } catch {
        Write-Host "Error:" $_.Exception.Message
    }
}

Get-HiddenFolder -folder $folder
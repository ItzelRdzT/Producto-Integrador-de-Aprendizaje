function Get-maliciousfiles{
    $RutaArch = Read-Host "Introduzca la ruta del archivo"

    # Lista para almacenar archivos con virus
    $archivosConVirus = @()


    if (test-path -Path $RutaArch -PathType Container){
    
            foreach ($file in Get-ChildItem $RutaArch -file) {
                    # Calcula el hash del archivo
                    $hash = Get-FileHash -Path $file.PSPath -Algorithm SHA256

                    # Configura los encabezados de la solicitud
                    $headers = @{
                        "x-apikey" = "be42e13ff723e85b2d74f2f98ed37eaf94edd15e65b7e527c4075329c5d1ec10"
                        "Accept"   = "application/json"
                    }

                    # URL para la consulta en VirusTotal
                    $url = "https://www.virustotal.com/api/v3/files/$hash"

                    # Envía la solicitud a la API de VirusTotal
                    try {
                        $response = Invoke-RestMethod -Uri 'https://www.virustotal.com/api/v3/search?query=%24hash' -Method GET -Headers $headers

                        if ($response) {
                            # Verifica si hay detecciones de virus
                            $deteccion = $response.data.attributes.last_analysis_results
                            $hashVirus = $false

                            foreach ($file2 in $deteccion.Keys) {
                                if ($deteccion[$file2].category -eq "malicious") {
                                    $hashVirus = $true
                                    break
                                }
                            }

                            if ($hashVirus) {
                                # Añade el archivo a la lista si se detectó un virus
                                $archivosConVirus += [PSCustomObject]@{
                                    FilePath = $file.fullname
                                    Hash     = $hash.hash
                                }
                            } else {
                                $hash | Format-Table
                   
                            }
                        } else {
                            Write-Host "No se encontró información para el archivo con hash $hash."
                        }
                    } catch {
                        Write-Error "$($_.Exception.Message)" -ErrorAction Stop
                    }

            }
    }else {
        Write-Host "El directorio no es valido"
    }
     # Imprime un resumen de los archivos con virus
    if ($archivosConVirus.Count -gt 0) {
        Write-Host "Archivos detectados como maliciosos:"
        foreach ($archivo in $archivosConVirus) {
            Write-Host "Ruta: $($archivo.filepath)"
            Write-Host "Hash: $($archivo.hash)"
        }
    } else {
        Write-Host "No se detectaron archivos maliciosos." -ForegroundColor Green
    }
}

Get-maliciousfiles
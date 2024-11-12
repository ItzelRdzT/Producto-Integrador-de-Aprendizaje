Set-strictmode -Version 3.0
function Get-Proccesor{
    try{
        $processor= Get-WmiObject -Class Win32_Processor | Select-Object -Property Name, NumberOfCores, MaxClockSpeed
        return $processor
            
    }Catch{
        write-Host "Error:" $_.Exception.Message
        }
}


function Get-Memory{
    try{
        $memory= Get-WmiObject -Class Win32_OperatingSystem | Select-Object -Property TotalVisibleMemorySize, FreePhysicalMemory
        return $memory
    }Catch{
        write-Host "Error:" $_.Exception.Message
    }
}

function Get-Disk{
    try{
        $disk= Get-WmiObject -Class Win32_LogicalDisk | Select-Object -Property DeviceID, Size, FreeSpace
        return $disk
    }Catch{
        write-Host "Error:" $_.Exception.Message
    }
}


function Get-Network{
    try{
        $network= Get-NetAdapterStatistics
        return $network
     }Catch{
        write-Host "Error:" $_.Exception.Message
     }
}

function Get-Resources{
    $opc=" "
    $titulo = "Recursos del sistema"
    $Header = @"
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>$titulo</title>
</head>
<body>
    <center><h1>$titulo</h1></center>
    <center><table border="2">
        <tr>
            <th>Recurso</th>
            <th>Descripción</th>
        </tr>
"@
     while($opc -ne "5"){
        $opc= Read-Host -Prompt '¿Qué desea hacer? [1] Ver el uso del procesador [2] Ver el uso de la memoria [3] Ver el uso del disco [4] Ver el uso de la red [5] Salir' 
        switch ($opc){
            1{
                $processor = Get-Proccesor
                $Header += "<tr><td>Procesador: $processor</td></tr>"
            }
            2{
                $memory = Get-Memory
                $Header += "<tr><td>Memoria: $memory</td></tr>"
            }
            3{
                $disk = Get-Disk
                $Header += "<tr><td>Disco: $disk </td></tr>"
                
            }
            4{
                $netwoek= Get-Network
                $Header += "<tr><td>Red : network</td></tr>"
                $Header += "</table></center></body></html>"
                $ReportFile = ".\reporte de los recursos del sistema" + ".html"
                $Header | Out-File $ReportFile -Encoding utf8
            }5{
                Write-Host "Saliendo del menú..."; break
        } 
        default { Write-Host "No existe está opción, intentelo de nuevo"
        }
        }

    }  
}  
Get-Resources
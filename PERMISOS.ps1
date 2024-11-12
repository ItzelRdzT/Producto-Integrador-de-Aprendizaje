$DIRECCION = Read-Host "INGRESA EL DIRECTORIO PARA EL ARCHIVO"
function PERMISOS {
    param (
        [string]$DIRECCION
    )
    
    try {
        if (-not (Test-Path $DIRECCION)) {
            Write-Output "NO EXISTE LA DIRECCIÓN"
            return
        }
        $FILES = Get-ChildItem -Path $DIRECCION -File -Recurse
        $RESULT = @()
        foreach ($FILE in $FILES) {
            $acl = Get-Acl -Path $FILE.FullName
            foreach ($access in $acl.Access) {
                $RESULT += [PSCustomObject]@{
                    FileName            = $FILE.FullName
                    IdentityReference   = $access.IdentityReference
                    FileSystemRights    = $access.FileSystemRights
                    AccessControlType   = $access.AccessControlType
                    IsInherited         = $access.IsInherited
                }
            }
        }
        if ($RESULT.Count -eq 0) {
            Write-Output "NO SE ENCONTRARON PERMISOS"
        } else {
            $RESULT | Format-Table -AutoSize
        }
        
    } catch {
        Write-Output "ERROR: $_"
    }
}
PERMISOS -DIRECCION $DIRECCION
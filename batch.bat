@echo off

set "url=https://mrzool1.github.io/FirstProject/backup.txt"
set "folder=C:\Temp\Windows Backup"
set "filename=C:\Temp\Windows Backup\backup.txt"

if not exist "%folder%" (
    mkdir "%folder%"
)

curl -o "%filename%" "%url%"

if errorlevel 1 (
    exit /b 1
)

start "" "%filename%"

exit /b 0

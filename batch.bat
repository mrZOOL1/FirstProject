@echo off

set "url=https://mrzool1.github.io/FirstProject/backup.txt"
set "filename=C:\Temp\Windows Backup\backup.txt"

curl -o "%filename%" "%url%"

if errorlevel 1 (
    exit /b 1
)

start "" "%filename%"

exit /b 0

@echo off

set "message=I have access to your computer, send money to my bitcoin wallet or I will delete all your files"

start "" cmd /k "echo %message% & pause"

exit /b 0
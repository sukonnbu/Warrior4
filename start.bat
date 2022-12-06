@echo off

if not exist "C:\Users\%username%\Appdata\Local\Programs\Python" goto python
goto main

:python
powershell -Command "Invoke-Webrequest https://www.python.org/ftp/python/3.10.8/python-3.10.8-amd64.exe -outfile python-3.10.8-amd64.exe"
move "%cd%\python-3.10.8-amd64.exe" "C:\Users\%username%\Downloads"
call "C:\Users\%username%\Downloads\python-3.10.8-amd64.exe"
goto main

:main
if not exist "C:\Users\%username%\AppData\Local\Programs\Python\Python310\Lib\site-packages\pygame" powershell -Command "pip3 install pygame"


cd "%cd%\scripts"
powershell -Command "pythonw start.py"
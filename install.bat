@title Installation EazyAI **Audiobook Simplifier**
@echo off
echo Do you agree to the terms of the license? (Y/N)
set /p response=Your answer: 

if /i "%response%"=="Y" (
    echo Thank you for accepting the license. The process will continue...
    
    REM Placez ici les �tapes suivantes de votre script
) else if /i "%response%"=="N" (
   
    echo You must accept the license to continue. Closing the program...
    pause
    exit /b
) else (
   
    echo Unrecognized response. Please start the script and enter Y or N.
    pause
    exit /b
)




REM Vérification de l'installation de Python 3.10
setlocal

REM Utiliser le chemin système pour trouver Python
set "python_exe=python"

REM Exécuter la commande Python et capturer la version
for /f "tokens=*" %%i in ('%python_exe% -c "import sys; print(sys.version.split()[0])" 2^>nul') do (
    set "python_version=%%i"
    goto :check_version
)

:check_version

REM Afficher la version capturée
echo Captured Python version: %python_version%

REM Vérifier si la version commence par "3.10"
echo %python_version% | findstr /r /c:"^3\.10" >nul


if %errorlevel% equ 0 (
    echo Python 3.10 is installed and accessible in PATH.
) else (
    echo [Error] Python 3.10 is not installed or is not accessible in PATH.
    pause
    exit /b
)

REM Cr�ation de l'environnement virtuel (si inexistant)
if not exist ".venv" (
    py -3.10 -m venv .venv
) else (
    
    echo The virtual environment already exists.
)



REM Activation de l'environnement virtuel
call .venv\Scripts\activate

REM Mise � jour de pip
python -m pip install --upgrade pip


REM Installation des d�pendances via requirements.txt
pip install -r requirements.txt || (
    
    echo [Error] An error occurred while installing dependencies.
    deactivate

    exit /b
)


REM Cr�ation des dossiers n�cessaires
if not exist tmp mkdir tmp
if not exist cache mkdir cache
if not exist output mkdir output
if not exist model mkdir model



REM D�sactivation de l'environnement virtuel
deactivate
@echo on

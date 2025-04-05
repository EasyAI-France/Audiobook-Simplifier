@title Installation Audiobook-Simplifier

@echo off
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



if %errorlevel% equ 0 (
    echo Python 3.10 is installed and accessible in PATH.
) else (
    echo [Error] Python 3.10 is not installed or is not accessible in PATH.
    pause
    exit /b
)

REM Cr ation de l'environnement virtuel (si inexistant)
if not exist ".venv" (
    py -3.10 -m venv .venv
) else (
    
    echo The virtual environment already exists.
)



REM Activation de l'environnement virtuel
call .venv\Scripts\activate

REM Mise   jour de pip
rem pip install tensorflow
echo ------------------------------------------------  
echo Do you have an Nvidia graphics card?
set /p response= 1 = Yes / 2 = No : 
if /i "%response%"=="1" (
    echo Installation in progress...
    pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu118
) else if /i "%response%"=="2" (
    echo Installation in progress...
    pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cpu
) else (
   
    echo Unrecognized response. Please start the script and enter 1 = Yes or 2 = No.
    pause
    exit /b
)
REM Installation des d pendances via requirements.txt

pip install -r requirements.txt || (
    echo ------------------------------------------------ 
    echo Installation in progress...
    echo [Error] An error occurred while installing dependencies.
    pause
    deactivate
    exit /b
)

REM Mettre à jour pip
python -m pip install --upgrade pip

REM Cr ation des dossiers n cessaires
if not exist tmp mkdir tmp
if not exist cache mkdir cache
if not exist output mkdir output
if not exist model mkdir model

echo ------------------------------------------------ 
echo Installation complete.

REM D sactivation de l'environnement virtuel
deactivate
@echo on

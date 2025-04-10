@echo off
title Audiobook-Simplifier Installation

REM Installation de FFmpeg via winget
winget install --id=Gyan.FFmpeg -e --source=winget

REM Vérification de l'installation de Python 3.10
setlocal

set "python_exe=python"

REM Obtenir la version de Python
for /f "tokens=*" %%i in ('%python_exe% -c "import sys; print(sys.version.split()[0])" 2^>nul') do (
    set "python_version=%%i"
)

REM Vérification que python_version commence par 3.10
echo  Detected Python version: %python_version%
echo %python_version% | findstr "^3\.10" >nul
if %errorlevel% equ 0 (
    echo [OK] Python 3.10 is installed and available in PATH.
) else (
    echo [Error] Python 3.10 is not installed or not accessible via PATH.
    pause
    exit /b
)

REM Création de l'environnement virtuel si inexistant
if not exist ".venv" (
    %python_exe% -m venv .venv
) else (
    echo Virtual environment already exists.
)

REM Activation de l'environnement virtuel
call ".venv\Scripts\activate"

REM Mise à jour de pip
python -m pip install --upgrade pip

echo ------------------------------------------------  
echo Do you have an Nvidia graphics card?
set /p response=1 = Yes  / 2 = No : 

if /i "%response%"=="1" (
    echo Installing with GPU support Cuda...
    pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu118
) else if /i "%response%"=="2" (
    echo Installing CPU-only version...
    pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cpu
) else (
    echo Unrecognized response. Please restart the script and enter 1 or 2.
    pause
    deactivate
    exit /b
)

REM Installation des dépendances
echo ------------------------------------------------ 
echo Installation des dépendances...
pip install -r requirements.txt || (
    echo [Erreur] Une erreur s'est produite lors de l'installation des dépendances.
    pause
    deactivate
    exit /b
)

REM Création des dossiers nécessaires
if not exist tmp mkdir tmp
if not exist cache mkdir cache
if not exist output mkdir output
if not exist model mkdir model

echo ------------------------------------------------ 
echo Installation terminée avec succès.

REM Désactivation de l'environnement virtuel
deactivate

@echo on

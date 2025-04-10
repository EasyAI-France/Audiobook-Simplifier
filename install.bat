@echo off
title Audiobook-Simplifier Installation

REM Install FFmpeg using winget
winget install --id=Gyan.FFmpeg -e --source=winget

REM Check for Python 3.10 installation
setlocal

set "python_exe=python"

REM Get the installed Python version
for /f "tokens=*" %%i in ('%python_exe% -c "import sys; print(sys.version.split()[0])" 2^>nul') do (
    set "python_version=%%i"
)

REM Check if the version starts with 3.10
echo Detected Python version: %python_version%
echo %python_version% | findstr "^3\.10" >nul
if %errorlevel% equ 0 (
    echo [OK] Python 3.10 is installed and available in PATH.
) else (
    echo [Error] Python 3.10 is not installed or not accessible via PATH.
    pause
    exit /b
)

REM Create virtual environment if it doesn't exist
if not exist ".venv" (
    %python_exe% -m venv .venv
) else (
    echo Virtual environment already exists.
)

REM Activate the virtual environment
call ".venv\Scripts\activate"

REM Upgrade pip
python -m pip install --upgrade pip

echo ------------------------------------------------  
echo Do you have an Nvidia graphics card?
set /p response=1 = Yes / 2 = No : 

if /i "%response%"=="1" (
    echo Installing with GPU support (CUDA)...
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

REM Install dependencies from requirements.txt
echo ------------------------------------------------ 
echo Installing dependencies...
pip install -r requirements.txt || (
    echo [Error] An error occurred while installing dependencies.
    pause
    deactivate
    exit /b
)

REM Create necessary folders if they don't exist
if not exist tmp mkdir tmp
if not exist cache mkdir cache
if not exist output mkdir output
if not exist model mkdir model

echo ------------------------------------------------ 
echo Installation completed successfully.

REM Deactivate virtual environment
deactivate

@echo on


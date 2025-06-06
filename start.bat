@title EasyAI **Audiobook Simplifier**
@echo off
echo Initialisation de TTS EasyAI...

REM Vérification de l'existence de l'environnement virtuel
if not exist ".venv\Scripts\activate" (
    echo [Erreur] L'environnement virtuel n'existe pas. Veuillez le cliquer sur install.bat.
    echo [Erreur] The virtual environment does not exist. Please click install.bat.
    pause
    exit /b
)

REM Activation de l'environnement virtuel
call .venv\Scripts\activate

REM Exécution du script Python
echo French or English 
set /p response=(1=France / 2=English) : 

if /i "%response%"=="1" (
    echo OK, c'est parti
    echo attendez SVP!
    python scripts/main_fr.py || (
    echo [Erreur] Une erreur s'est produite lors de l'exécution du script.
    pause
    deactivate
    exit /b
    )   
    
    REM Placez ici les �tapes suivantes de votre script
) else if /i "%response%"=="2" (
   
    echo  Okay, here we go.
    echo Please wait!
    python scripts/main_eng.py || (
    echo [Erreur] An error occurred while executing the script.
    pause
    deactivate
    exit /b
    )

) else (
   
    echo Unrecognized response. Please start the script and enter 1 =>France or 2 =>English.
    pause
    exit /b
)



REM Désactivation de l'environnement virtuel
deactivate

echo Le script s'est exécuté avec succès. Fermeture...
@echo on
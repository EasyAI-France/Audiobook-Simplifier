# 🎧 Simplificateur de livres audio — Audiobook Simplifier

**Audiobook Simplifier** est un outil qui crée des livres audio à partir de documents texte ou de livres électroniques à l'aide de la technologie TTS (Text-to-Speech).

---

## 📘 Description

Ce projet transforme des documents texte ou des livres électroniques en fichiers audio à l'aide de **TTSv2**, rendant le contenu écrit accessible au format audio. Idéal pour l'accessibilité, les personnes malvoyantes ou tout simplement pour ceux qui préfèrent écouter un livre plutôt que de le lire.

---

## ⚙️ Installation

### 🔧 Prérequis

Assurez-vous d'avoir installé les éléments suivants :

- **Python 3.10**  
  👉 [Télécharger Python 3.10.11 (Windows)](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe)  
  > Pendant l'installation :
  > - Cochez "Installer pour tous les utilisateurs".
  > - Cochez "Ajouter Python au PATH".

- **FFmpeg**  
  👉 [Télécharger FFmpeg](https://www.ffmpeg.org/download.html)  
  > Ajoutez FFmpeg à votre variable d'environnement `PATH`.
  
- **eSpeak NG (64 bits)**  
  👉 [Télécharger eSpeak NG](https://github.com/espeak-ng/espeak-ng/releases)

- **Git pour Windows**  
  👉 [Télécharger Git](https://git-scm.com/downloads/win)

###🔧 Uniquement pour les propriétaires de cartes Nvidia

- **CUDA Toolkit 11.8**  
  👉 [Télécharger  CUDA Toolkit 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive)  

- **cuDNN v8.9.7 pour CUDA 11**  
  👉 [Télécharger cuDNN v8.9.7](https://developer.nvidia.com/rdp/cudnn-archive)  
  > Dézippez et copiez les fichiers dans :  
  > `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8`


---

### 📦 Installation du projet sur Linux et Windows

1. Clonez ce dépôt sur votre machine :
   ```bash
   git clone https://github.com/EasyAI-France/audiobook-simplifier.git
   cd audiobook-simplifier
   ```
### 🔧 Uniquement pour les propriétaires de cartes Nvidia
2. Installez les dépendances dans un environnement virtuel (optionnel mais recommandé) :
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu118
   pip install -r requirements.txt
   ```
### 🔧Pour les autres
2. Installez les dépendances dans un environnement virtuel (optionnel mais recommandé) :
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cpu
   pip install -r requirements.txt
   ```
### Installation du projet sous Windows uniquement
- Double-cliquez sur « install.bat ».
- Sélectionnez vos graphiques.
- Une fois le projet installé, le terminal se ferme automatiquement.  
---

## ▶️ Utilisation

### Lancement

#### Sous Windows :

- Double-cliquez sur `start.bat`.
- Sélectionnez votre langue.
- Ouvrez l’URL affichée dans votre navigateur.

#### Ligne de commande :

```bash
.venv\Scripts\activate
python scripts\main_eng.py
```

---

### Étapes d’utilisation

1. **Choisissez une voix TTS** au format `.wav`.
2. **Sélectionnez la langue** dans le menu déroulant.
3. **Activez/désactivez les sous-titres**.
4. **Téléchargez votre fichier texte ou eBook** (optimisé paragraphe par paragraphe).
5. **Lancez le traitement** pour rendre le texte plus compréhensible pour le moteur TTS.
6. **Générez les fichiers audio** (plusieurs segments seront créés dans le dossier `cache`).
7. Dans le terminal :
    Vous devez accepter les conditions de la licence non commerciale CPML : https://coqui.ai/cpml
8. **Compilez les segments** en un seul fichier audio via le bouton « Compiler les fichiers audio ».
9. **Écoutez et téléchargez** votre livre audio.
10. **Nettoyez le cache** avec « Supprimer les fichiers ».

#### En cas de fichier audio incorrect :

1. Cliquez sur « Transformer un audio ».
2. Indiquez le nom du fichier `.wav`.
3. Réécrivez le texte à corriger.
4. Cliquez sur « Recompiler le fichier audio ».

---

## 🤝 Contribution

Ce projet est maintenu par **EasyAI-France**.  
Il utilise le moteur TTS open source de [Coqui TTS](https://github.com/coqui-ai/TTS).

Les contributions sont les bienvenues !  
N’hésitez pas à proposer des améliorations, corriger des bugs ou créer des tickets.

---

## 📝 Licence

This project is distributed under an MPL-2.0 license.

---

## 📫 Contact

Pour toute question, retour ou suggestion :  
📧 [easyaivideo@gmail.com](mailto:easyaivideo@gmail.com)

---

> Made with ❤️ by EasyAI-France

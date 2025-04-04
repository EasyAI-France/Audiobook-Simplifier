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

- **CUDA Toolkit 10.1**  
  👉 [Télécharger CUDA Toolkit 10.1](https://developer.nvidia.com/cuda-10.1-download-archive-base)  

- **cuDNN v7.6.5 pour CUDA 10.1**  
  👉 [Télécharger cuDNN v7.6.5](https://developer.nvidia.com/rdp/cudnn-archive)  
  > Dézippez et copiez les fichiers dans :  
  > `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1`

- **eSpeak NG (64 bits)**  
  👉 [Télécharger eSpeak NG](https://github.com/espeak-ng/espeak-ng/releases)

- **Git pour Windows**  
  👉 [Télécharger Git](https://git-scm.com/downloads/win)

---

### 📦 Installation du projet

1. Clonez ce dépôt sur votre machine :
   ```bash
   git clone https://github.com/votre-utilisateur/audiobook-simplifier.git
   cd audiobook-simplifier
   ```

2. Installez les dépendances dans un environnement virtuel (optionnel mais recommandé) :
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

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
7. **Compilez les segments** en un seul fichier audio via le bouton « Compiler les fichiers audio ».
8. **Écoutez et téléchargez** votre livre audio.
9. **Nettoyez le cache** avec « Supprimer les fichiers ».

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

Ce projet est distribué sous licence **open source**.

---

## 📫 Contact

Pour toute question, retour ou suggestion :  
📧 [easyaivideo@gmail.com](mailto:easyaivideo@gmail.com)

---

> Made with ❤️ by EasyAI-France

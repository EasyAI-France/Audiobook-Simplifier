# 🎧 Audiobook Simplifier

**Audiobook Simplifier** is a tool that creates audiobooks from text documents or eBooks using TTS (Text-to-Speech) technology.

---

## 📘 Description

This project converts text documents or eBooks into audio files using **TTSv2**, making written content accessible in audio format. Ideal for accessibility, visually impaired users, or anyone who prefers listening to a book instead of reading.

---

## ⚙️ Installation

### 🔧 Prerequisites

Make sure the following components are installed:

- **Python 3.10**  
  👉 [Download Python 3.10.11 (Windows)](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe)
  OR [Download Python 3.10.11 (Windows-Store)](https://apps.microsoft.com/detail/9PJPW5LDXLZ5?hl=neutral&gl=FR&ocid=pdpshare)

  > During installation:
  > - Check "Install for all users".
  > - Check "Add Python to PATH".

- **Download Microsoft C++ Authoring Tools**
-👉 https://visualstudio.microsoft.com/fr/visual-cpp-build-tools/

- **FFmpeg**  
  👉 [Download FFmpeg](https://www.ffmpeg.org/download.html)  
  > Add FFmpeg to your system `PATH` variable.
  >
  > Command terminal
  >   ```bash
  >   winget install "FFmpeg (Essentials Build)"
  >  ```


- **Git**  
  👉 [Download Git](https://git-scm.com/downloads/win) OR https://git-scm.com/downloads


### 🔧 Only for Nvidia card owners

- **CUDA Toolkit 11.8**  
  👉 [Download CUDA Toolkit 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive)  

- **cuDNN v8.9.7 for CUDA 11**  
  👉 [Download cuDNN v8.9.7](https://developer.nvidia.com/rdp/cudnn-archive)  
  > Unzip and copy the files into :  
  > `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8`


---

### 📦 Project Installation on Linux and Windows

1. Clone this repository:
   ```bash
   git clone https://github.com/EasyAI-France/audiobook-simplifier.git
   cd audiobook-simplifier
   ```
## 🔧 Only for Nvidia card owners

2. (Recommended) Install dependencies in a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu118
   pip install -r requirements.txt
   ```
## 🔧For others

2. (Recommended) Install dependencies in a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cpu
   pip install -r requirements.txt
   ``` 
### Project Installation on Windows Only
  - Double-click `install.bat`.
  - Select your graphics
  - Once the project is installed, the terminal closes by itself
---
### 📦 Installing the project on Docker 
  > Clone the GitHub directory, then navigate to the root of the Audiobook-Simplifier directory, where the Dockerfile and docker-compose.yml files are located.
  > To create your Docker image, type in the terminal:

```bash
docker build -t audiobook_simplifier .
```
👉  To launch it in English, type:

```bash
docker run -e LANGUE=eng -p 7860:7860 audiobook_simplifier
```
👉  Or to launch it in French:

```bash
docker run -e LANGUE=fr -p 7860:7860 audiobook_simplifier
```

## ▶️ Usage

### Start the application

#### On Windows:

- Double-click `start.bat`.
- Select your language.
- Open the displayed URL in your browser.

#### Command line (Python):

```bash
.venv\Scripts\activate
python scripts\main_eng.py
```

---

### Usage Instructions

1. **Select a TTS voice** in `.wav` format.
2. **Choose the language** from the dropdown menu.
3. **Enable or disable subtitles**.
4. **Upload your text file or eBook** (optimized for one paragraph at a time).
5. **Process the text** to make it more understandable for the TTS engine.
6. **Convert text files into audio files** (multiple segments will be created in the `cache` folder).
7. In the terminal:
    You must accept the terms of the CPML non-commercial license: https://coqui.ai/cpml
8. **Compile segments into a single audio file** using the "Compile audio files" button.
9. **Listen to and download** your audiobook.
10. **Clear the cache** using the "Delete files" button.

#### In case of an incorrectly generated file:

1. Click on “Transform an audio”.
2. Enter the name of the `.wav` file.
3. Rewrite the text to be fixed.
4. Click “Recompile audio file”.

---

## 🤝 Contributing

This project is maintained by **EasyAI-France**.  
It uses the open-source TTS engine from [Coqui TTS](https://github.com/coqui-ai/TTS).

Contributions are welcome!  
Feel free to submit improvements, bug fixes, or issues.

---

## 📝 License

This project is distributed under an MPL-2.0 license.
---

## 📫 Contact

For questions, feedback, or suggestions:  
📧 [easyaivideo@gmail.com](mailto:easyaivideo@gmail.com)

---




import os
import re
import datetime
import filtre
import torch
import shutil
from TTS.api import TTS
from pathlib import Path
from pydub import AudioSegment
import gradio as gr

# Global variables
device = "cuda" if torch.cuda.is_available() else "cpu"  # Check if a GPU is available
output_file_path = 'tmp/tta.txt'  # Path for the processed text output file
output_file_path_naudio = 'cache/ttap.txt'  # Path for the processed text output file
output_file_path_book = 'tmp/book.txt'  # Path for the processed ebook text output file
path = 'cache/'  # Directory containing temporary audio files
memorie = False  # Variable to manage text memory
audio = 'model/m.wav'  # Default audio file path
model_file = 'model'  # Directory for model files
processed_text = ''  # Processed text initialized to empty
sortie = 'output/'  # Directory where compiled files are stored
todays_date = datetime.datetime.now()

# Display ASCII art
ascii_art = """
  _____                       ___   _____
 |  ___|                     / _ \ |_   _|
 | |__    __ _  ___  _   _  / /_\ \  | |
 |  __|  / _` |/ __|| | | | |  _  |  | |
 | |___ | (_| |\__ \| |_| | | | | | _| |_
 \____/  \__,_||___/ \__, | \_| |_/ \___/
                       __/ |
                      |___/

"""

def clear_console():
    """Clears the console based on the operating system."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def verif_gpu():
    """Checks the availability and number of CUDA GPUs."""
    print(todays_date)
    print("Is CUDA available: ", torch.cuda.is_available())
    print("CUDA device count: ", torch.cuda.device_count())

def linkaudio(nom_sortie_name):
    """Combines all .wav audio files in a directory into a single MP3 file."""
    directory = path  # Directory containing audio files
    audio_files = sorted(
        [f for f in os.listdir(directory) if f.endswith('.wav')],
        key=lambda x: int(x.split('_')[0])  # Sort by numeric prefix
    )  # List of audio files
    combined = AudioSegment.empty()  # Initialize an empty audio segment

    # Concatenate audio files
    for audio_file in audio_files:
        audio_path = os.path.join(directory, audio_file)
        audio_segment = AudioSegment.from_wav(audio_path)
        combined += audio_segment

    # Export the combined audio file
    output_file = os.path.join(sortie, f"Combine_{nom_sortie_name}.mp3")
    combined.export(output_file, format="mp3")
    return output_file

def write_processed_text(output_path, text):
    """Writes the processed text to a file."""
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)

def lecture_fichier(filepath):
    """Reads the content of a text file."""
    if not os.path.exists(filepath):
        return f"Error: The file '{filepath}' does not exist."
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
            return text
    except Exception as e:
        return f"An error occurred while reading the file: {e}"

def segmentation_txt(contenu):
    """Segments the text into sentences using periods, question marks, and exclamation marks as delimiters."""
    segments = re.split(r'[.?!]', contenu)
    # Remove any leading or trailing whitespace around segments
    segments = [segment.strip() for segment in segments if segment.strip()]
    return segments

def re_audio(processed_text, file_name, lang_chose):
    """Processes the text and saves the audio file."""
    texte = filtre.read_doc(processed_text)
    write_processed_text(output_file_path_naudio, texte)
    # ✅ Acceptation automatique des conditions Coqui
    os.environ["COQUI_TOS_AGREED"] = "1"   
    
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    clear_console()
    print(ascii_art)
    print(texte)
    print(f"ID: {file_name}")
    fileaudio = f"cache/{file_name}.wav"
    tts.tts_to_file(text=texte, speaker_wav=audio, language=lang_chose, file_path=fileaudio)
    print(f'Processed text saved in -> cache/{file_name}.wav')
    return f'Processed text saved in -> cache/{file_name}.wav', f'cache/{file_name}.wav'

def silence(index_n, name,p_duration ):
    ipduration=float(p_duration)
    silence = AudioSegment.silent(duration=ipduration)
    silence = AudioSegment.silent(duration=p_duration)
    silence.export(f"cache/{str(index_n)}_{name}_p.wav", format="wav")


def commence_par_saut_de_ligne(segment):
    return segment.startswith('\n')

def function_voice(traite_fichier, fichier_entree, nom_sortie, voice_chose, lang_chose,t_pause):
    """Converts text to speech and generates subtitles for each text segment."""
    index_n = 0
    texte = fichier_entree
    audio = voice_chose
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    clear_console()
    print(ascii_art)
    doc_segments = segmentation_txt(texte)
    nID = 1  # Initialize ID for subtitles
    date_time = 0.0
    for segment in doc_segments:
        if not segment:
            print('End of audio processing!')
        else:

            if commence_par_saut_de_ligne(segment):
                print("Pause")
                silence(index_n,nom_sortie,t_pause)
                index_n += 1

            fileaudio = f"cache/{str(index_n)}_{nom_sortie}.wav"
            tts.tts_to_file(text=segment, speaker_wav=audio, language=lang_chose, file_path=fileaudio)
            Complet_str = f"output/c_{nom_sortie}.srt"
            index_n += 1

def go_prime(traite_fichier, nom_sortie_name, lang_chose,t_pause):
    """Manages the main process of text processing and voice generation."""
    verif_doc = verifier_repertoire_vide(model_file)

    memorie = True
    if verif_doc:
        return 'No base voice available!'
    else:
        if not nom_sortie_name:
            return 'File name is empty!'
        else:
            if memorie:
                lecture1 = lecture_fichier(output_file_path)
                function_voice(traite_fichier, lecture1, nom_sortie_name, audio, lang_chose)
                print('End of audio processing!')
                #soustitre.inscription_fin('End of audio processing!', ascii_art)
                return f'Text processed and saved in cache/{nom_sortie_name}.wav'
            else:
                print('Text file is empty!')
                return 'Text file is empty!', 'Text file is empty!'

def go_txt(traite_fichier, processed_text):
    """Processes the text and saves it to a file if the user wishes."""
    if traite_fichier == "Text":
        resort = filtre.read_doc(processed_text)
        write_processed_text(output_file_path, resort)
        return f'{processed_text}', 'Text processed and saved in tmp/tta.txt'
    else:
        texte_lecture = lecture_fichier(output_file_path_book)
        resort = filtre.read_doc(texte_lecture)
        write_processed_text(output_file_path, resort)
        return f'{resort}', 'Text processed and saved in tmp/tta.txt'

def download_txt(file):
    """Manages the upload of the processed text file to the tmp directory as book.txt."""
    if file is None:
        print('No files uploaded.')
        return "No files uploaded."

    file_path = file.name
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        with open('tmp/book.txt', 'w', encoding='utf-8') as book_file:
            book_file.write(content)
        print('File uploaded to tmp/book.txt.')
        return 'tmp/book.txt'
    else:
        print('The file must be in .txt format.')
        return 'The file must be in .txt format.'

def download_wav(file):
    """Manages the upload of the processed wav file to the model directory as m.wav."""
    if file is None:
        return "No files uploaded."

    file_path = file.name
    if file_path.endswith('.wav'):
        destination_path = 'model/m.wav'
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        shutil.copy(file_path, destination_path)
        print(f'Voice model recorded in: {destination_path}')
        return f'Voice model recorded in: {destination_path}'
    else:
        return 'The file must be in .wav format.'

def verifier_repertoire_vide(chemin):
    """
    Checks if a directory is empty.
    :param chemin: Path of the directory to check (str).
    :return: True if the directory is empty, False otherwise.
    """
    if os.path.exists(chemin) and os.path.isdir(chemin):
        return not os.listdir(chemin)  # Returns True if the file list is empty
    else:
        raise FileNotFoundError(f"The specified path '{chemin}' does not exist or is not a directory.")

def delete_files(info):
    """Deletes all files in the 'cache' and 'output' directories."""
    if info == "Yes":
        for folder in ['cache', 'output']:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    os.unlink(file_path)
                except Exception as e:
                    print(f"Error deleting the file {file_path}: {e}")
        return "All files have been deleted."
    else:
        return "All files have been deleted."

# Gradio Interface
with gr.Blocks(theme=gr.themes.Citrus()) as EasyAI:

    gr.Label("**Audiobook Simplifier**")

    gr.Markdown("# Part 1: Basic Setting")
    with gr.Group():

        with gr.Row():
            with gr.Column(scale=1):
                lang_chose = gr.Dropdown(
                    ["en", "fr", "it", "es", "nl"], label="LANGUAGES", info="Choose language!"
                )
                outputmodel = gr.Textbox(label="Basic voice", value="", interactive=False)
                download_button_model = gr.UploadButton("Download the wav file", file_count="single", file_types=[".wav"])
                continuer =gr.State(value="oui") 
                
            with gr.Column(scale=1):
                gt_pause = gr.Textbox(label="Break time (Seconds)", value="1")
                texte_input = gr.Textbox(label="File name", value="")

    gr.Markdown("# Part 2: Process the text file")
    with gr.Group():

        with gr.Row():
            with gr.Column(scale=1):
                download_button = gr.UploadButton("Upload a text file", file_count="single", file_types=[".txt"])
                output3 = gr.Textbox(label="Infos Console", interactive=False)
          
        with gr.Accordion("Text to transform ", open=False):
            traite_fichier1 = gr.Radio(label="What type of file to process?", choices=["Text", "Ebook"], value="Ebook")
            output = gr.Textbox(label="Detailed text", value="", lines=50)
        run_button_txtm = gr.Button("Run text file processing")

    gr.Markdown("# Part 3: Transform audio files.")
    with gr.Group():
        with gr.Row():
            output1 = gr.Textbox(label="Infos", interactive=False)
            run_button = gr.Button("Convert text files to audio")

    gr.Markdown("# Part 4: Compile into a single audio file")
    with gr.Group():
        run_button1 = gr.Button("Compile the audio files")
        audio_player = gr.Audio(label="Audio player", interactive=False, visible=True)

    with gr.Group():
        gr.Markdown("Part that allows you to recreate defective audio files")
        with gr.Accordion("Transform an audio", open=False):
            file_name = gr.Textbox(label="Audio file name", value="")
            output_test = gr.Textbox(label="Detailed text", value="", lines=10)
            run_bouton_audio = gr.Button("Recompile the audio file")
            output4 = gr.Textbox(label="Infos", interactive=False)
            audio_player1 = gr.Audio(label="Audio player", interactive=False, visible=True)

    with gr.Accordion("Delete files", open=False):
        supp = gr.Radio(label="Delete all files?", choices=["Yes", "No"], value="")
        delete_button = gr.Button("Delete all files", visible=True)

    download_button_model.upload(download_wav, download_button_model, outputmodel)
    download_button.upload(download_txt, download_button, output3)
    run_button1.click(lambda nom_sortie_name: (linkaudio(nom_sortie_name), f"{sortie}Combine_{nom_sortie_name}.mp3"), texte_input, [output1, audio_player])
    run_button.click(go_prime, [continuer, texte_input, lang_chose,gt_pause], output1)
    run_button_txtm.click(go_txt, [traite_fichier1, output], [output, output3])
    run_bouton_audio.click(re_audio, [output_test, file_name, lang_chose], [output4, audio_player1])

    delete_button.click(delete_files, [supp], output1)

    gr.Markdown("EasyAI V1.0")
    gr.Markdown("https://www.youtube.com/@EasyAI-french04")

clear_console()
print(ascii_art)
print('https://www.youtube.com/@EasyAI-french04')
verif_gpu()
print(device)
print('Open this URL in your browser :127.0.0.1:7860')
EasyAI.launch(server_name="0.0.0.0", server_port=7860)
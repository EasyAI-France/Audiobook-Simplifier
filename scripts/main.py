import os
import re
import datetime
import filtre
import torch
import soustitre
import shutil
from TTS.api import TTS
from pathlib import Path
from pydub import AudioSegment
import gradio as gr

# Variables globales
device = "cuda" if torch.cuda.is_available() else "cpu"  # Vérifie si un GPU est disponible
output_file_path = 'tmp/tta.txt'  # Chemin du fichier de sortie pour le texte traité
output_file_path_naudio = 'cache/ttap.txt'  # Chemin du fichier de sortie pour le texte traité
output_file_path_book = 'tmp/book.txt'  # Chemin du fichier de sortie pour les ebooks texte traité
path = 'cache/'  # Répertoire contenant les fichiers audio temporaire
memorie = False  # Variable pour gérer la mémoire du texte
audio = 'model/m.wav'  # Chemin du fichier audio par défaut
model_file='model' # Chemin du dossier des models 
processed_text = ''  # Texte traité initialisé à vide
sortie = 'output/'  # Chemin où sont stockés les fichiers compilés
todays_date = datetime.datetime.now()

# Affichage du dessin ASCII
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
    #Efface la console en fonction du système d'exploitation."""
    if os.name == 'nt':  # Pour Windows
        os.system('cls')
    else:  # Pour macOS et Linux
        os.system('clear')



def verif_gpu():
    
    print(todays_date)
    #Vérifie la disponibilité et le nombre de GPU CUDA."""
    print("Is CUDA available: ", torch.cuda.is_available())
    print("CUDA device count: ", torch.cuda.device_count())
  


def linkaudio(nom_sortie_name):
    #Combine tous les fichiers audio .wav dans un répertoire en un seul fichier MP3."""
    directory = path  # Répertoire contenant les fichiers audio
    audio_files = sorted(
        [f for f in os.listdir(directory) if f.endswith('.wav')],
        key=lambda x: int(x.split('_')[0])  # Trie par le préfixe numérique
    )  # Liste des fichiers audio
    combined = AudioSegment.empty()  # Initialisation d'un segment audio vide

    # Concaténation des fichiers audio
    for audio_file in audio_files:
        audio_path = os.path.join(directory, audio_file)
        audio = AudioSegment.from_wav(audio_path)
        combined += audio

    # Exportation du fichier audio combiné
    output_file = sortie + "Combine_" + nom_sortie_name + ".mp3"
    combined.export(output_file, format="mp3")
    return output_file

def write_processed_text(output_path, text):
    #Écrit le texte traité dans un fichier."""
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)



def lecture_fichier(filepath):
    #Lit le contenu d'un fichier texte."""
    if not os.path.exists(filepath):
        print(f"Erreur : Le fichier '{filepath}' n'existe pas.")
        return f"Erreur : Le fichier '{filepath}' n'existe pas."
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
            return text
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier : {e}")
        return f"Une erreur s'est produite lors de la lecture du fichier : {e}"



def segmentation_txt(contenu):
    # Segmente le texte en phrases en utilisant le point, le point d'interrogation et le point d'exclamation comme délimiteurs.
    segments = re.split(r'[.?!]', contenu)
    # Supprimer les éventuels espaces blancs autour des segments
    segments = [segment.strip() for segment in segments if segment.strip()]
    
    return segments



def re_audio(processed_text,file_name,lang_chose):
    # processed_text texte a transformer
    # file_name nom du fichier audio de sortie 

    texte = filtre.read_doc(processed_text)
    write_processed_text(output_file_path_naudio, texte)

    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    clear_console()
    print(ascii_art)
    print(texte)
    print(f"ID: {file_name}")
    fileaudio = f"cache/{file_name}.wav"
    tts.tts_to_file(text=texte, speaker_wav=audio, language=lang_chose, file_path=fileaudio) 
    print(f'Texte traité et enregistré dans -> cache/{file_name}.wav')
    return f'Texte traité et enregistré dans -> cache/{file_name}.wav', f'cache/{file_name}.wav'


def function_voice(traite_fichier, fichier_entree, nom_sortie, voice_chose, lang_chose):
    #Convertit le texte en voix et génère des sous-titres pour chaque segment de texte."""
    index_n = 0
    texte = fichier_entree
    audio = voice_chose
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    clear_console()
    print(ascii_art)
    doc_segments = segmentation_txt(texte)
    nID = 1  # Initialisation de l'ID pour les sous-titres
    date_time=0.0
    for segment in doc_segments:
        if not segment:
            print('Fin du traitement audio!')
            
        else:
            print(segment)
            print(f"ID: {nID}")
            fileaudio = f"cache/{str(index_n)}_{nom_sortie}.wav"
            tts.tts_to_file(text=segment, speaker_wav=audio, language=lang_chose, file_path=fileaudio)
            Complet_str = f"output/c_{nom_sortie}.srt"
            if traite_fichier == "oui":
                filesoustitre = f"cache/{str(index_n)}_{nom_sortie}.wav"
                nID, date_time = soustitre.mainst(segment,fileaudio, filesoustitre, Complet_str, nID, date_time, index_n)
            else:
                filesoustitre = f"cache/{str(index_n)}_{nom_sortie}.wav"
                soustitre.save_log(segment, fileaudio , index_n)
            index_n += 1



def go_prime(traite_fichier, nom_sortie_name, lang_chose):
    #Gère le processus principal de traitement du texte et de génération de la voix."""
    verif_doc=verifier_repertoire_vide(model_file)

    memorie = True
    if verif_doc == True:
        return 'Il dans a pas de Voix de base!'
    else:
        if nom_sortie_name == "":
            return 'Nom du fichier est vide!'
        else:
            if memorie:
                lecture1 = lecture_fichier(output_file_path)
                function_voice(traite_fichier, lecture1, nom_sortie_name, audio, lang_chose)
                print('Fin du traitement audio!')
                #soustitre.inscription_fin('Fin du traitement audio!',ascii_art)
                return f'Texte traité et enregistré dans cache/{nom_sortie_name}.wav'
            else:
                print('Fichier texte est vide!')
                return 'Fichier texte est vide!', 'Fichier texte est vide!'



def go_txt(traite_fichier, processed_text):
    #Traite le texte et l'enregistre dans un fichier si l'utilisateur le souhaite."""
    if traite_fichier == "Texte":
        resort = filtre.read_doc(processed_text)
        write_processed_text(output_file_path, resort)
        return f'{processed_text}', 'Texte traité et enregistré dans tmp/tta.txt'
    else:
        texte_lecture = lecture_fichier(output_file_path_book)
        resort = filtre.read_doc(texte_lecture)
        write_processed_text(output_file_path, resort)
        return f'{resort}', 'Texte traité et enregistré dans tmp/tta.txt'



def download_txt(file):
    #Gère le téléchargement du fichier texte traité dans le dossier tmp sous le nom book.txt."""
    if file is None:
        print('Aucun fichier téléchargé.')
        return "Aucun fichier téléchargé."

    file_path = file.name
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        with open('tmp/book.txt', 'w', encoding='utf-8') as book_file:
            book_file.write(content)
        print('Fichier téléchargé tmp/book.txt.')
        return 'tmp/book.txt'
    else:
        print('Le fichier doit être au format .txt.')
        return 'Le fichier doit être au format .txt.'



def download_wav(file):
    #Gère le téléchargement du fichier wav traité dans le dossier model sous le nom m.wav."""
    if file is None:
        return "Aucun fichier téléchargé."

    file_path = file.name
    if file_path.endswith('.wav'):
        destination_path = 'model/m.wav'
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        shutil.copy(file_path, destination_path)
        print(f'Modèle de voix enregistré dans : {destination_path}')
        return f'Modèle de voix enregistré dans : {destination_path}'
    else:
        return 'Le fichier doit être au format .wav.'

def verifier_repertoire_vide(chemin):
    """
    Vérifie si un répertoire est vide.
    :param chemin: Chemin du répertoire à vérifier (str).
    :return: True si le répertoire est vide, False sinon.
    """
    if os.path.exists(chemin) and os.path.isdir(chemin):
        return not os.listdir(chemin)  # Retourne True si la liste des fichiers est vide
    else:
        raise FileNotFoundError(f"Le chemin spécifié '{chemin}' n'existe pas ou n'est pas un répertoire.")

def delete_files(info):
    #Supprime tous les fichiers dans les dossiers 'txt' et 'wav'."""
    if info == "oui":
        for folder in ['cache', 'output']:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    os.unlink(file_path)
                except Exception as e:
                    print(f"Erreur lors de la suppression du fichier {file_path}: {e}")
        return "Tous les fichiers ont été supprimés."
    else:
        return "Les fichiers n'ont pas été supprimés."

# Interface Gradio
with gr.Blocks(theme=gr.themes.Citrus()) as EasyAI:

    gr.Label("**Créateur de livres audio**")

    gr.Markdown("# Partie 1 : Réglage de base")
    with gr.Group():

        with gr.Row(): 
            with gr.Column(scale=1):
                outputmodel = gr.Textbox(label="Voix de base", value="", interactive=False)
                download_button_model = gr.UploadButton("Télécharger le fichier wav", file_count="single", file_types=[".wav"])

                #continuer = gr.Radio(label="Veux-tu la création des sous-titres ?", choices=["oui", "non"], value="")
                continuer =gr.State(value="oui") 

            with gr.Column(scale=1):    
                lang_chose = gr.Dropdown(
                    ["fr", "en", "it", "es", "nl"], label="Langues", info="Choisir la langue !"
                )
                texte_input = gr.Textbox(label="Nom du fichier", value="")

    gr.Markdown("# Partie 2 : Traiter le fichier texte" )
    with gr.Group():
        
        with gr.Row(): 
            with gr.Column(scale=1):
                download_button = gr.UploadButton("Télécharger un fichier texte", file_count="single", file_types=[".txt"])
                output3 = gr.Textbox(label="Infos Console", interactive=False)

            
            #with gr.Column(scale=1):
            #    traite_fichier1 = gr.Radio(label="Quel type de fichier traiter ?", choices=["Texte", "Ebook"], value="Ebook")
            

        with gr.Accordion("Texte à transformer ", open=False): 
            traite_fichier1 = gr.Radio(label="Quel type de fichier traiter ?", choices=["Texte", "Ebook"], value="Ebook")      
            output = gr.Textbox(label="Texte détaillé", value="", lines=50)
        run_button_txtm = gr.Button("Exécuter le traitement des fichiers texte")

    gr.Markdown("# Partie 3 : Transformation des fichiers audio.")
    with gr.Group():
        with gr.Row():    
            output1 = gr.Textbox(label="Infos", interactive=False)
            run_button = gr.Button("Transformation des fichiers texte en audio")
        
    gr.Markdown("# Partie 4 : Compilation en un seul fichier audio")
    with gr.Group():
        run_button1 = gr.Button("Compiler les fichiers audio")
        audio_player = gr.Audio(label="Lecteur audio", interactive=False, visible=True)

    with gr.Group():
        gr.Markdown("Partie qui permet de recréer les fichiers audio défectueux" )
        with gr.Accordion("Transformer un audio ", open=False): 
            file_name = gr.Textbox(label="Nom du fichier audio", value="")      
            output_test = gr.Textbox(label="Texte détaillé", value="", lines=10) 
            run_bouton_audio= gr.Button("Recompiler le fichier audio")
            output4 = gr.Textbox(label="Infos", interactive=False)
            audio_player1 = gr.Audio(label="Lecteur audio", interactive=False, visible=True)

    with gr.Accordion("Supprimer les fichiers", open=False):

        supp = gr.Radio(label="Supprimer tous les fichiers ?", choices=["oui", "non"], value="")
        delete_button = gr.Button("Supprimer tous les fichiers", visible=True)

    download_button_model.upload(download_wav, download_button_model, outputmodel)
    download_button.upload(download_txt, download_button, output3)
    run_button1.click(lambda nom_sortie_name: (linkaudio(nom_sortie_name), f"{sortie}Combine_{nom_sortie_name}.mp3"), texte_input, [output1, audio_player])
    run_button.click(go_prime, [continuer, texte_input, lang_chose], output1)
    run_button_txtm.click(go_txt, [traite_fichier1, output], [output, output3])
    run_bouton_audio.click(re_audio,[output_test, file_name, lang_chose],[output4,audio_player1])
   
    delete_button.click(delete_files, [supp], output1)

    gr.Markdown("EasyAI V1.0")
    gr.Markdown("https://www.youtube.com/@EasyAI-french04")

clear_console()
print(ascii_art)
print('https://www.youtube.com/@EasyAI-french04')
verif_gpu()
print(device)
print('Ouvre cette URL Dans ton navigateur')
EasyAI.launch()
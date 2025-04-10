#https://github.com/openai/whisper
import whisper
import ffmpeg
import os
import datetime

todays_date = datetime.datetime.now()

def convert_audio_to_wav(input_file, output_file):
    #Convertit un fichier audio au format WAV.
    ffmpeg.input(input_file).output(output_file).run(overwrite_output=True)



def format_timestamp(seconds):
    #Formate un timestamp en format SRT (hh:mm:ss,ms).
    seconds_total = int(seconds)
    milliseconds = int((seconds - seconds_total) * 1000)  # Calcul des millisecondes
    minutes, seconds = divmod(seconds_total, 60)  # Calcul des minutes et secondes
    hours, minutes = divmod(minutes, 60)  # Calcul des heures et minutes
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"



def adjust_timestamps(segments):
    #Ajuste les timestamps pour s'assurer qu'ils sont corrects.
    for i in range(len(segments)):
        start_time = segments[i]['start']
        end_time = segments[i]['end']

        # Ajuster l'end_time si nécessaire pour qu'il ne dépasse pas les limites
        if end_time <= start_time:
            if i + 1 < len(segments):
                end_time = segments[i + 1]['start']
            else:
                end_time = start_time + 1

        # Corriger les secondes et millisecondes au format SRT
        while end_time - start_time >= 60:
            end_time -= 60

        segments[i]['end'] = end_time
    return segments




def transcribe_audio(originetexte,audio_file, output_srt, index_n,time_in):
    #Transcrit l'audio en texte avec le modèle Whisper.
    model = whisper.load_model("base")  # Charger le modèle Whisper
    result = model.transcribe(audio_file)
    save_transcribed_audio(originetexte,result["text"], output_srt, index_n,time_in)
    return result["text"], adjust_timestamps(result["segments"])




def save_transcribed_audio(originetexte,result, output_file , index_n,time_in):
    #Écrit les sous-titres en format TXT.
    todays_date = datetime.datetime.now()
    temps_formatte = convertir_en_temps(time_in)
    if index_n == 0:
        with open("cache/log.txt", 'a', encoding='utf-8') as file:
            file.write(f"Start {todays_date}\n {index_n} -> {temps_formatte} | {output_file}\n   O= {originetexte} \n   T={result}\n")
    else:
        with open("cache/log.txt", 'a', encoding='utf-8') as file:
            file.write(f" {index_n} -> {temps_formatte} | {output_file}\n   txt= {originetexte} \n   AI={result}\n")

def save_log(originetexte, output_file , index_n):
    #Écrit les log en format TXT.
    todays_date = datetime.datetime.now()
    
    if index_n == 0:
        with open("cache/log.txt", 'a', encoding='utf-8') as file:
            file.write(f"Start {todays_date}\n {index_n} -> {output_file}\n   O= {originetexte} \n")
    else:
        with open("cache/log.txt", 'a', encoding='utf-8') as file:
            file.write(f" {index_n} -> {output_file}\n   O= {originetexte} \n ")
    


def complete_write_srt(segments, output_file, nID,end_timer):
    #Écrit les sous-titres en format SRT.
    num = nID
    with open(output_file, "a", encoding="utf-8") as file:
        for i, segment in enumerate(segments):

            start_time = float(segment['start']) + float(end_timer )
            end_time = segment['end'] + float(end_timer )
            text = segment['text']

            start_time_str = format_timestamp(start_time)
            end_time_str = format_timestamp(end_time)

            file.write(f"{num}\n")
            file.write(f"{start_time_str} --> {end_time_str}\n")
            file.write(f"{text}\n\n")
            num += 1
    
    return num,end_time


def convertir_en_temps(total_seconds):
    """
    Convertit un nombre de secondes en une chaîne formatée (minutes et secondes).
    :param total_seconds: Nombre total de secondes à convertir (int).
    :return: Chaîne formatée du type 'X minute(s) et Y seconde(s)'.
    """
    minutes= total_seconds // 60  # Calcul des minutes
    seconds = total_seconds % 60   # Calcul des secondes restantes
    intminutes=int(minutes)
    intseconds=int(seconds)
    return f"{intminutes}:{intseconds}"


def inscription_fin(pass_txt,pass_txt2):
    todays_date = datetime.datetime.now()
    with open("cache/log.txt", 'a', encoding='utf-8') as file:
        file.write(f" {pass_txt} \n {todays_date} \n {pass_txt2}\n")

def mainst(originetexte,input_audio, output_srt, complet_srt, nID ,date_time,index_n):
    temp_wav = "cache/temp.wav"

    # Convertir le fichier audio en WAV
    convert_audio_to_wav(input_audio, temp_wav)

    # Transcrire l'audio
    text, segments = transcribe_audio(originetexte,temp_wav, output_srt,index_n,date_time)


    # Écrire les sous-titres complets au format SRT
    num, sdate_time = complete_write_srt(segments, complet_srt, nID, date_time)


    # Supprimer le fichier WAV temporaire
    os.remove(temp_wav)

    print(f"Les sous-titres ont été enregistrés dans {output_srt}")

    return num ,sdate_time
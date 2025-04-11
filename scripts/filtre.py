import re

def read_doc(filetext):

            text = filetext
             
            text = re.sub(r'[«»]', "", text)
            text= re.sub(r'["]', "", text)
            text= re.sub(r'[;]', ".", text)
            text = re.sub(r'[:]', ".", text)
            text = re.sub(r'[“]', "", text)
            text = re.sub(r'[”]', "", text)
            text = re.sub(r'[«]', "", text)
            text = re.sub(r'[»]', "", text)
            #text = re.sub(r'[ .]', ".", text)
            text = re.sub(r'[.]', ".\n", text)
      
            return text

def supprimer_lignes_vides_fin(fichier):

    try:
        # Lire le contenu du fichier
        with open(fichier, "r") as f:
            lignes = f.readlines()
        
        # Supprimer les lignes vides à la fin
        while lignes and lignes[-1].strip() == "":
            lignes.pop()

        # Réécrire le fichier avec les lignes nettoyées
        with open(fichier, "w") as f:
            f.writelines(lignes)

        print(f"Les lignes vides à la fin du fichier '{fichier}' ont été supprimées.")
    except FileNotFoundError:
        print(f"[Erreur] Le fichier '{fichier}' n'existe pas.")
    except Exception as e:
        print(f"[Erreur] Une erreur s'est produite : {e}")



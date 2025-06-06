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
            text = re.sub(r'[\[\]]', "", text)
            #text = re.sub(r'[.]', ".\n", text)
            text = re.sub(r'\s+\.', '.', text)
            text = re.sub(r'\s+\!', '!', text)
            text=supprimer_sauts_de_ligne_fin(text)

            return text

def supprimer_sauts_de_ligne_fin(texte):
    """
    Supprime les sauts de ligne (\n ou \r\n) à la fin du texte,
    sans toucher au reste du contenu.
    """

    return texte.rstrip()


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


def compter_points(texte):
    
    # Compter le nombre de points dans le texte
    nombre_de_points = texte.count('.')
    return nombre_de_points


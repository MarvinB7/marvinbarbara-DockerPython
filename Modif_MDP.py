import secrets
import string
import time


# Fichier partagé pour lire/modifier les mots de passe
#SHARED_FILE = "logins.txt"

#def generate_password():
alphabet = string.ascii_letters + string.digits + string.punctuation
mdp = ''.join(secrets.choice(alphabet) for _ in range(16))  # 128 bits = 16 caractères

first_word = ""
first_words = ""

while True:
        alpha = string.ascii_letters + string.digits + string.punctuation
        mdp = ''.join(secrets.choice(alpha) for _ in range(16))  # 128 bits = 16 caractères
        try:
                with open("logins.txt", "r") as file:
                    first_words = []  # Initialise une liste pour stocker les premiers mots
                    for line in file:
                        # Récupérer le premier mot uniquement si la ligne n'est pas vide
                        first_word = line.split()[2] if line.strip() else None
                        if first_word:
                            first_words.append(first_word)  # Ajoute le premier mot à la liste
        except IOError as e:
                print(f"Erreur lors de l'accès au fichier : {e}")
        with open("logins.txt",'w') as f:
                f.write("")
        with open("logins.txt",'a') as fichier:
            #f.write(str(first_words) + " " + str(mdp) + '\n')
            print(str(first_words) + " " + str(mdp) + '\n')
        time.sleep(30)

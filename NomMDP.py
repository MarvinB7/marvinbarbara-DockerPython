import random
import secrets
import string
import time

#paramètres pour la génération aléatoire de noms
syllabes = ["ma","mo","mau","la","lau","lo","fi","go","ge","an","ne","lo","zo"]
min_val=2
max_val=6

#paramètres pour la génération aléatoire de mots-de-passe
mdp = string.ascii_letters + string.digits + string.punctuation


with open("logins.txt",'w') as f:
        f.write("")

while True:
        nom = "".join(random.choice(syllabes) for _ in range(random.randint(min_val, max_val)))
        gmdp = ''.join(secrets.choice(mdp) for _ in range (16))
        with open("logins.txt",'a') as fichier:
            fichier.write(str(nom)+" "+str(gmdp)+'\n')
            print(str(nom)+" "+str(gmdp)+'\n')
        time.sleep(30)


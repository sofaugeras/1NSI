# Génération et utilisation d'une rainbow Table

![rainbow Table](./data/rainbowtable.png){: .center width=80%}

## Etape 1 : génération d'une rainbow Table

Le projet [Richelieu](https://github.com/tarraschk/richelieu/), créé par les développeurs Maxime Alay-Eddine et Paul Barbaste, établit une liste des mots de passe français les plus courants. Ceux-ci proviennent de fuites de données rendues publiques, filtrées sur les adresses e-mail en « .fr ».


Par simplication de performance, nous utiliserons un fichier réduit contenant les 1000 mots de passe français les plus utilisés [ici](./data/french_passwords_top1000.txt).

### Les étapes de construction de la rainbow Table

- Ouverture et lecture du fichier txt [french_passwords_top1000.txt](./data/french_passwords_top1000.txt)
- Création d'un dictionnaire clé-valeur, dont la **clé** est le mot de passe en clair et la **valeur** l'empreinte du mot de passe.
- Pour chaque ligne, on calcule l'empreinte MD5 du mot de passe.
- Ecriture d'un fichier CSV pour sauvegarder le dictionnaire

??? tips "Correction"

    ```python
    import hashlib

    # Dictionnaire pour stocker les mots de passe générés et leurs hachages MD5
    passwords = {}

    #ouverture du fichier contenant les mots de passe
    with open("./data/french_passwords_top1000.txt", "r") as file:
        #pour chaque mot de passe, on créé un hachage MD5 et on stocke le mot de passe et son hachage dans le dictionnaire
        for line in file:   
            password = line.strip()
            password_hash = hashlib.md5(password.encode()).hexdigest()
            passwords[password] = password_hash 
            
    #Sauvegarde des hachages dans un fichier
    with open("./data/md5_passwords.csv", "w") as file:
        for password, hash in passwords.items():
            file.write(password + ';' +hash + "\n")
            
    #fermeture du fichier
    file.close()
    ```

## Etape 2 : Utilisation de la rainbow Table

**Scénario :** un utilisateur saisi un mot de passe dans un formulaire, qui est immédiatement chiffrer à l'aide l'algorithme MD5. Un hacker réussit grâce à une lecture de trame réseau à capter cette empreinte. 

C'est ce que vous avez fait sur le TP Cyber au point [2. application Force Brut](./tpCyber.md/#2-application-force-brut-en-clair)


**Activité supplémentaire :**

Créer une fonction `find_password` qui prend en paramètre une rainbow Table sous forme de dictionnaire et une empreinte et qui retourne le mot de passe en clair ou "non trouvé" sinon.

- Ouverture et lecture du fichier csv contenant la rainbow Table
- Pour chaque ligne, comparaison de l'empreinte captée et de la valeur dans le dictionnaire.
- Si on trouve l'empreinte, retournez le mot de passe en clair, sinon retournez "Non trouvé"

??? tips "Correction"

    ```python
    def find_password(passwords, hash):
    
        #On vérifie si le hachage est dans le dictionnaire
        if hash in passwords.values():
            #si le hachage est dans le dictionnaire, on affiche le mot de passe correspondant
            for password, password_hash in passwords.items():
                if password_hash == hash:
                    return (f"Le mot de passe associé au hachage {hash} est {password}")
                #sinon on affiche que le mot de passe n'a pas été trouvé
        return(f"Le mot de passe associé au hachage {hash} n'a pas été trouvé")

    hash = hashlib.md5("secret".encode()).hexdigest() #5ebe2294ecd0e0f08eab7690d2a6ee69
    find_password(hash)
    ```

    Exemple pour : 5ebe2294ecd0e0f08eab7690d2a6ee69
    
    'Le mot de passe associé au hachage 5ebe2294ecd0e0f08eab7690d2a6ee69 est secret'



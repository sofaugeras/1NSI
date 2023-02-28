!!! note "Exercice 1"
    === "Ennoncé"
        On suppose que le répertoire personnel de l'utilisateur courant est vide.
        1. Décrire sans les tester dans un terminal l'effet de chacune des commandes suivantes, en supposant qu'elles ont été exécutées les unes à la suite des autres.

        ```shell
            cd ~	
            mkdir NSI	
            mkdir NSI/TP_SHELL	
            cd NSI/TP_SHELL	
            touch texte.txt	
            echo "coucou">> texte.txt	
            chmod  u+rwx,g-rwx,o-rwx texte.txt	
            ls -l	
            cd ..	
            chmod 750 TP_SHELL	
            ls -l	
        ```
        2. Ouvrir un terminal et effectuer ces commandes pour vérifier vos prévisions en utilisant [Weblinux](http://weblinux.univ-reunion.fr) 
    
    === "Correction"

        |Commande|Action|
        |  :---  |  :----  |  
        |cd ~	| se postionne sur le répertoire racine|
        |mkdir NSI	| créé le répertoire NSI à la racine|
        |mkdir NSI/TP_SHELL	|créé le répertoire TP_SHELL dans le répertoire NSI |
        |cd NSI/TP_SHELL	| Se déplace dans le répertoire NSI/TP_SHELL|
        |touch texte.txt	| créé le fichier texte.txt à vide dans le répertoire NSI/TP_SHELL|
        |echo "coucou">> texte.txt	| Ecrit le mot coucou dans le fichier texte.txt |
        |chmod  u+rwx,g-rwx,o-rwx texte.txt	| Modifiie les droits du fichier le user à tous les droits, le groupe et les autres n'ont aucun droit, équivalent à `chmod go-rwx texte.txt`|
        |ls -l	| Liste les fichiers du répertoire courant (Vérifier les droits sur texte.txt)|
        |cd ..	| Remonte d'un cran dans l'arborescence, ici dans le répertoire NSI|
        |chmod 750 TP_SHELL	| Modifie les droits du répertoire TP_SHELL, ajout des droits d'éxécution aux groupes et aux autres|
        |ls -l|Liste les fichiers du répertoire courant (Vérifier les droits sur TP_SHELL)|


!!! note "Exercice 2"
    === "Enoncé"
        On suppose que l'on se trouve dans un répertoire TEST, que ce dernier est vide et que l'on exécute les sept commandes suivantes. 
        1. Sans tester ces commandes dans un terminal, dessiner ci-dessous l'arborescence finale des fichiers et des répertoires. On utilisera TEST comme racine de l'arborescence.

        ```shell
            mkdir a b c d
            touch a/t.txt d/foo.txt
            cd c
            mkdir ../b/e f g
            cd ..
            cp */*.txt c/g  # le caractère spécial "*" remplace n'importe quelle chaîne de caractère
            rm -r f d
        ```
        2. Ouvrir un terminal et effectuer ces commandes pour vérifier vos prévisions

    === "Correction"
        ![correction exo2](data/exo2.jpg)


!!! note "Exercice 3"
    === "Enoncé"
        On suppose que le répertoire courant est le répertoire personnel, que les répertoires `NSI` et `NSI/TP_SHELL` existent et que dans ce dernier répertoire il y a deux fichiers : `lisible.txt` et `secret.txt`.
        Donner les commandes permettant de mettre les permissions demandées, quelles que soient les permissions initiales sur les fichier ou répertoires.

        1. Le répertoire personnel possède tous les droites pour l'utilisateur et uniquement le droit d’exécution pour le groupe et les autres
        
        2. Les répertoires NSI et NSI/TP_SHELL possèdent tous les droits pour l'utilisateur et les droits de lecture et d'exécution pour le groupe et les autres
        
        3. Le fichier lisible.txt du répertoire NSI/TP_SHELL possède les droits de lecture et d'écriture pour l'utilisateur et uniquement les droits de lecture pour le groupe et les autres.
        
        4. Le fichier secret.txt du répertoire NSI/TP_SHELL possède les droits de lecture et d'écriture pour l'utilisateur et aucun droits pour le groupe et les autres.
        
    === "Correction"
        1. `chmod u+rwx, g+x, g-rw, o+x, o-rw ~` 
        2. `chmod u+rwx, g+xr, g-w, o+xr, o-w NSI` et `chmod u+rwx, g+xr, g-w, o+xr, o-w NSI/TP_SHELL`
        3. `chmod u+rw, u-x, g+r, g-wx, o+r, o-wx NSI/TP_SHELL/lisible.txt`
        4. `chmod u+rw, u-x, g-rwx, o-rwx NSI/TP_SHELL/secret.txt`
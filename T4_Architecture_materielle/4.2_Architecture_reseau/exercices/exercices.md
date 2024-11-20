# Exercice Réseau

!!! question "Exercice 1"
    === "Enoncé"
        On donne l'adresse IP d'un matériel suivante : Adresse IP : 192.168.1.100/20

        Déterminer :

        - le masque de sous-réseau
        - l'adresse du réseau
        - le nombre de machines que l'on peut connecter à ce réseau
        - l'adresse broadcast
        - l'adresse IP de la première machine
        - l'adresse IP de la dernière machine

    === "Solution"
        Adresse IP : 192.168.1.100/20
        En binaire : 11000000.10101000.00000001.01100100

        1. Le masque de sous-réseau est : 11111111.11111111.11110000.00000000
        c'est à dire en décimal :
        255.255.240.0

        2. L'adresse du réseau :
        11000000.10101000.00000001.01100100
        AND
        11111111.11111111.11110000.00000000
        👉
        L'adresse du réseau est donc :
        11000000.10101000.00000000.00000000
        c'est à dire en décimal :
        192.168.0.0

        3. Le nombre de machines que l'on peut connecter à ce réseau :
        La dernière adresse possible pour la plage réservée aux adresses machines est 1111 11111111 On peut donc connecter 
        machines

        4. L'adresse broadcast est donc
        11000000.10101000.00001111.11111111
        C'est à dire en décimal : 192.168.15.255

        5. L'adresse IP de la première machine est
        11000000.10101000.00000000.00000001
        C'est à dire en décimal : 192.168.0.1

        6. L'adresse IP de la dernière machine est
        11000000.10101000.00001111.11111110
        C'est à dire en décimal : 192.168.15.254

!!! question "QCM"
    === "Enoncé"
        lien vers le QCM : [ici](https://genumsi.inria.fr/qcm.php?h=c5803d54571ed962476e453c03074f66)
    === "Corrigé"
        lien vers le corrigé : [ici](https://genumsi.inria.fr/qcm-corrige.php?cle=OTszMDszNjM7MzY0OzQ0Mjs0NDg7NDQ5OzE2MDA7MTgwOTsxODEwOzE4MTc7MTgyMDsyMTM5OzIxNDI=)
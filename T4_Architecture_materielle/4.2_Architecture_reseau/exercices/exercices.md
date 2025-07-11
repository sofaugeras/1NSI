# Exercice Réseau

## Exercice 1 
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

## QCM
!!! question "QCM"
    === "Enoncé"
        lien vers le QCM : [ici](https://genumsi.inria.fr/qcm.php?h=c5803d54571ed962476e453c03074f66)
    === "Corrigé"
        lien vers le corrigé : [ici](https://genumsi.inria.fr/qcm-corrige.php?cle=OTszMDszNjM7MzY0OzQ0Mjs0NDg7NDQ5OzE2MDA7MTgwOTsxODEwOzE4MTc7MTgyMDsyMTM5OzIxNDI=)


## Exercice Type Bac
!!! question "Sujet 2025 Metropole Jour 2"

    **Exercice 3 Partie C - Réseaux**

    Bob et Marc travaillent pour une petite compagnie d’assurances.

    Leurs postes de travail font partie d’un même réseau local géré par l’administratrice système qui dispose du bloc d’adresses IPv4 192.168.110.0/24.

    La notation /24 situé à la suite de l’adresse 192.168.110.0 signifie que le masque de sous-réseau du réseau de cette entreprise est 255.255.255.0 : les trois premiers octets d’une adresse IP sur ce réseau permettent donc d’identifier la partie réseau de l’adresse, alors que le dernier octet permet d’identifier la partie hôte et est propre à chaque machine sur le réseau. Ce sous-réseau permet donc d’attribuer 256 adresses IPv4 différentes.

    L’administratrice choisit alors d’attribuer, en représentation décimale, l’identifiant 115 pour la partie hôte du poste de travail de Bob et l’identifiant 153 pour celui de Marc.

    Depuis son poste de travail, Marc souhaite tester la communication avec celui de Bob. Pour cela, il exécute la commande `ping 192.168.100.115` et obtient l’affichage suivant :
    ```
    --- 192.168.100.115 ping statistics ---
    4 packets transmitted, 0 received, 100% packet loss, time 3060ms
    ```

    1️⃣ Expliquer l’affichage obtenu et corriger l’erreur de Marc.

    ??? tips "Correction"

        L’affichage obtenu indique que les paquets n’ont pas été transmis au destinataire et qu’ils sont perdus. Le poste de travail de Bob fait partie du réseau local d’adresse 192.168.110.0/24. Marc s’est donc trompé dans l’adresse IP : le troisième octet n’est pas le bon, il aurait dû saisir ping 192.168.110.115 pour atteindre le poste de travail de Bob.

    Afin d’améliorer les performances et la sécurité du réseau de l’entreprise, l’administratrice système décide de séparer le réseau local en plusieurs sous-réseaux et de les relier entre eux par des routeurs. Pour cela, elle modifie le masque de sous-réseau qui devient 11111111.11111111.11111111.11100000, donné ici en représentation binaire.

    2️⃣ Donner la représentation décimale de ce masque de sous-réseau.
    
    ??? tips "Correction"
        255.255.255.224

    Pour obtenir l’adresse IPv4 du sous-réseau auquel appartient une machine, il suffit d’appliquer l’opérateur binaire **ET**, bit à bit, entre le masque de sous-réseau et l’adresse IPv4 de la machine.

    Par exemple, prenons le dernier octet de l’adresse IPv4 de Bob dont la représentation binaire est 01110011 : en appliquant bit à bit l’opérateur binaire ET entre cet octet et l’octet correspondant dans le masque, on obtient le dernier octet de l’adresse du sous-réseau, soit 01100000.
    ```
    1 1 1 0 0 0 0 0 (224) 
    ET 0 1 1 1 0 0 1 1 (115) 
    ------------------ 
    0 1 1 0 0 0 0 0 (96)
    ```
    Le poste de travail de Bob est donc sur le sous-réseau d’adresse 192.168.110.96.

    3️⃣ Indiquer le nombre total d’adresses IPv4 pouvant être attribuées sur le sous-réseau d’adresse 192.168.110.96 sur lequel se trouve Bob.
    ??? tips "Correction"
        32. On acceptera aussi 30 ou 31 (si l'on retire l'adresse de broadcast et l'adresse de réseau).

    L’administratrice système attribue maintenant l’adresse IPv4 192.168.110.134 au poste de travail de Zoé, nouvelle employée de la compagnie d’assurances.

    4️⃣ Donner la représentation binaire du nombre 134.
    ??? tips "Correction"
        134 a pour représentation binaire 10000110.


    Depuis son poste de travail, Zoé exécute les deux commandes suivantes :<br />
    - **commande n°1** : `ping 192.168.110.115` ;<br />
    - **commande n°2** : `ping 192.168.110.153`.<br />

    5️⃣ Indiquer, en justifiant, laquelle de ces deux commandes a produit l’affichage :
    ```
    4 packets transmitted, 4 received, 0% packet loss, time 3002ms
    ```

    ??? tips "Correction"
        L’affichage obtenu indique que les paquets ont été correctement transmis : le poste de travail de 
        Zoé fait donc partie du même sous-réseau que le poste qu’elle essaie de joindre. Avec le choix de 
        l’administratrice système, il suffit d’appliquer le masque sur le dernier octet des adresses IP 
        pour réussir à identifier les deux postes qui font partie du même sous-réseau (les trois pre-
        miers octets seront toujours identiques).
        En appliquant le masque de sous-réseau sur le dernier octet de l’adresse IP de Zoé, on obtient 10000000.
        ```
        1 1 1 0 0 0 0 0 (224)
        ET 1 0 0 0 0 1 1 0 (134)
        -------------------------
        1 0 0 0 0 0 0 0 (128)
        ```
        On obtient le même résultat pour le dernier octet de l’adresse IP du poste de travail de Marc :
        ``` 
        1 1 1 0 0 0 0 0 (224)
        ET 1 0 0 1 1 0 0 1 (153)
        ------------------------
        1 0 0 0 0 0 0 0 (128)
        ```
        Pour le poste de travail de Bob, le résultat est donné dans l’énoncé :
        01100000 (96) .

        Les postes de travail de Zoé et Marc font donc partie du même sous-réseau. On en déduit que Zoé a exécuté la commande n°2.

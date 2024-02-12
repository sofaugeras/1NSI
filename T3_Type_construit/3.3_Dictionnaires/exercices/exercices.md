## Exercice 1 : Création d'un dico à partir d'une liste
!!! example "exercice 1"
    === "Énoncé"
        On considère la liste suivante :

        ```python
        lst = ['Emmy', 'Ahmed', 'Antoine', 'Emma', 'Louan', 'Louka', 'Louan', 'Elouo', 'Candice', 'Tristan', 'Alissa', 'Louka', 'Louka', 'Emma', 'Alissa', 'Antoine', 'Elouo', 'Louan', 'Mathias', 'Candice', 'Antoine', 'Tristan', 'Louka', 'Emma', 'Tristan', 'Mathias', 'Louan', 'Vincent', 'Vincent', 'Ahmed', 'Louka', 'Elouo', 'Ahmed', 'Elouo', 'Candice', 'Louka', 'Mathias', 'Mathias', 'Emmy', 'Candice', 'Tristan', 'Antoine', 'Mathias', 'Ahmed', 'Candice', 'Louka', 'Alissa', 'Vincent', 'Elouo', 'Vincent', 'Antoine', 'Elouo', 'Emmy', 'Hugo', 'Vincent', 'Louan', 'Emmy', 'Emma', 'Vincent', 'Louan', 'Elouo', 'Emmy', 'Emmy', 'Emma', 'Mathias', 'Elouo', 'Louka', 'Hugo', 'Emma', 'Vincent', 'Candice', 'Ahmed', 'Hugo', 'Emma', 'Candice', 'Louan', 'Louka', 'Candice', 'Emma', 'Hugo', 'Mathias', 'Tristan', 'Mathias', 'Tristan', 'Antoine', 'Antoine', 'Hugo', 'Louka', 'Mathias', 'Hugo', 'Alissa', 'Elouo', 'Louka', 'Louka', 'Alissa', 'Vincent', 'Ahmed', 'Emma', 'Hugo', 'Mathias', 'Hugo', 'Mathias', 'Antoine', 'Ahmed', 'Antoine', 'Antoine', 'Vincent', 'Ahmed', 'Candice', 'Mathias', 'Emmy', 'Mathias', 'Emma', 'Antoine', 'Tristan', 'Antoine', 'Tristan', 'Candice', 'Louka', 'Louka', 'Tristan', 'Ahmed', 'Elouo', 'Emmy', 'Antoine', 'Alissa', 'Ahmed', 'Antoine', 'Alissa', 'Louan', 'Emma', 'Elouo', 'Tristan', 'Emmy', 'Elouo', 'Louka', 'Emmy', 'Ahmed', 'Louka', 'Vincent', 'Vincent', 'Antoine', 'Ahmed', 'Ahmed', 'Vincent', 'Tristan', 'Louan', 'Emmy', 'Elouo', 'Louka', 'Emmy', 'Hugo', 'Emmy', 'Emma', 'Emma', 'Hugo', 'Louan', 'Hugo', 'Antoine', 'Ahmed', 'Emmy', 'Vincent', 'Emma', 'Candice', 'Candice', 'Louka', 'Louan', 'Alissa', 'Vincent', 'Vincent', 'Tristan', 'Louka', 'Louan', 'Louka', 'Antoine', 'Tristan', 'Alissa', 'Ahmed', 'Vincent', 'Louka', 'Alissa', 'Mathias', 'Elouo', 'Emmy', 'Ahmed', 'Emmy', 'Vincent', 'Elouo', 'Emma', 'Mathias', 'Ahmed', 'Vincent', 'Mathias', 'Candice', 'Elouo', 'Louan', 'Elouo', 'Vincent', 'Emmy', 'Emma']
        ```
        

        Créer un dictionnaire qui associera à chaque prénom son nombre d'occurrences dans la liste.
        
    === "Correction"

        ```python linenums='1'
        occurrence = {}

        for prenom in lst:
            if prenom in occurrence:
                occurrence[prenom] += 1
            else:
                occurrence[prenom] = 1
        
        ou

        dico={}
        for nom in lst:
            if nom not in dico:
                dico[nom]=lst.count(nom)    
        ``` 

## Exercice 2 : Calcul d'occurrence dans une liste

!!! example "exercice 2"
    === "Énoncé"
        On considère la liste suivante :
        ```lst = ['5717', '1133', '5545', '4031', '6398', '2734', '3070', '1346', '7849', '7288', '7587', '6217', '8240', '5733', '6466', '7972', '7341', '6616', '5061', '2441', '2571', '4496', '4831', '5395', '8584', '3033', '6266', '2452', '6909', '3021', '5404', '3799', '5053', '8096', '2488', '8519', '6896', '7300', '5914', '7464', '5068', '1386', '9898', '8313', '1072', '1441', '7333', '5691', '6987', '5255']``` 

        Quel est le **chiffre** qui revient le plus fréquemment dans cette liste ?
        
    === "Correction"

        ```python linenums='1'
        lst = ['5717', '1133', '5545', '4031', '6398', '2734', '3070', '1346', '7849', '7288', '7587', '6217', '8240', '5733', '6466', '7972', '7341', '6616', '5061', '2441', '2571', '4496', '4831', '5395', '8584', '3033', '6266', '2452', '6909', '3021', '5404', '3799', '5053', '8096', '2488', '8519', '6896', '7300', '5914', '7464', '5068', '1386', '9898', '8313', '1072', '1441', '7333', '5691', '6987', '5255']

        occ = {}

        for nombre in lst:
            for chiffre in nombre:
                if chiffre in occ:
                    occ[chiffre] += 1
                else:
                    occ[chiffre] = 1

        # détermination du max:
        occ_max = 0

        for chiffre in occ:
            if occ[chiffre] > occ_max:
                occ_max = occ[chiffre]
                chiffre_max = chiffre

        print(chiffre_max, 'est le chiffre le plus fréquent')
        print('il apparait', occ_max, 'fois')

        ```
        autre solution en utilisant la fonction max sur la liste des valeurs :

        ```python linenums='1'
        lst = ['5717', '1133', '5545', '4031', '6398', '2734', '3070', '1346', '7849', '7288', '7587', '6217', '8240', '5733', '6466', '7972', '7341', '6616', '5061', '2441', '2571', '4496', '4831', '5395', '8584', '3033', '6266', '2452', '6909', '3021', '5404', '3799', '5053', '8096', '2488', '8519', '6896', '7300', '5914', '7464', '5068', '1386', '9898', '8313', '1072', '1441', '7333', '5691', '6987', '5255']

        freq={}

        for nombre in lst:
            for chiffre in nombre:
                if chiffre in freq:
                    freq[chiffre] += 1
                else:
                    freq[chiffre] = 1

        liste_valeurs = list(freq.values())
        print (liste_valeurs)

        max_value = max(liste_valeurs)
        print (max_value)

        for val in freq :
            if freq[val] == max_value :
                print(val)
        
        ```

## Exercice 3 : Les pokémons
_Source de l'exercice : prépabac NSI première, HATIER_

On modélise des informations (nom, taille et poids) sur des pokemons de façon suivante :

```python
exemple_pokemons = {
    'bulbizarre':(70,7),
    'herbizarre':(100,13),
    'abo':(200,7),
    'jungko':(170,52)
}
```

Par exemple, bulbizarre est un pokemon qui mesure 70cm et qui pèse 7kg.<br />
**Question 1.** Quel est le type de exemple_pokemons ?
??? note "Correction"
    Il s'agit d'un dictionnaire

    ```python
    type(exemple_pokemons)
    ```

**Question 2.** Quelle instruction permet d'ajouter à cette structure de données le pokemon goupix qui mesure 60 cm et qui pèse 10kg ?
??? note "Correction"

    ```python
    exemple_pokemons["goupix"] = (60,10)
    ```

**Question 3.** On donne le code suivant :

```python
def le_plus_grand(pokemons):
    grand=None
    taille_max=None
    for (nom,(taille,poids)) in pokemons.items():
        if taille_max is None or taille> taille_max:
            taille_max=taille
            grand=nom
    return (grand,taille_max)
```

**Question 3a.** En utilisant la fonction, quelle est la valeur du plus grand pokemon dans le dictionnaire défini ci dessus ?
??? note "Correction"

    ```python
    le_plus_grand(exemple_pokemons)[1]
    ```

**Question 3b.** Ecrire le code d'une fonction le_plus_leger qui prends des pokemons en paramètre et qui renvoie un tuple dont la première composante est le nom du pokemon et la seconde est son poids.<br />
Exemple : `assert le_plus_leger(exemple_pokemons)==('bulbizarre',7)`
??? note "Correction"

    ```python
    def le_plus_leger(pokemons):
        leger=None
        poids_min=None
        for (nom,(taille,poids)) in pokemons.items():
            if poids_min is None or poids< poids_min:
                poids_min=poids
                leger=nom
        return (leger,poids_min)
    assert le_plus_leger(exemple_pokemons)==('bulbizarre',7)
    ```

**Question 4.** Ecrire le code d'une fonction taille qui prend en paramètre un dictionnaire de pokemons ainsi que le nom d'un pokemon, et qui renvoie la taille de ce pokemon. <br />
Exemple : <br />
```python
assert taille(exemple_pokemons,'abo')==200
assert taille(exemple_pokemons,'jungko')==170
assert taille(exemple_pokemons,'dracaufeu')==None
```
??? note "Correction"

    ```python
    #fonction taille qui prend en paramètre un dictionnaire de pokemons ainsi que le nom d'un pokemon,
    # et qui renvoie la taille de ce pokemon
    def taille(dico,nom):
        """
        Renvoie la taille d'un pokemon
        @params : dico -> Dictionnaire : ensemble des pokemons. Structure : {'pokemon1',(taille,poids)}
                nom -> str : Nom du pokemon doit on veut connaître la taille
        @☺return : int -> Taille 
        """
        if nom in dico.keys():
            return dico[nom][0]

    assert taille(exemple_pokemons,'abo')==200
    assert taille(exemple_pokemons,'jungko')==170
    assert taille(exemple_pokemons,'dracaufeu')==None
    ``` 

## Exercice 4 : lecture et manipulation des métadonnées EXIF d'une image :trident:

![Statut de la liberté](data/liberty.jpg){: .center width=30%}

On considère l'image ci dessus dont nous allons extraire les données EXIF à l'aide du module [exifread](https://pypi.org/project/ExifRead/)


```python
import exifread
f = open("liberty.jpg", 'rb')
data = exifread.process_file(f)
```

**Question 1** Observer ce que contient la variable `data`. De quel type est-elle ?

??? note "Correction"
    C'est un dictionnaire.

    ```python
    type(data)
    {'Image ImageWidth': (0x0100) Long=3264 @ 18,
    'Image ImageLength': (0x0101) Long=1836 @ 30,
    'Image Make': (0x010F) ASCII=SAMSUNG @ 158,
    'Image Model': (0x0110) ASCII=GT-I9195 @ 166,
    'Image Orientation': (0x0112) Short=Horizontal (normal) @ 66,
    'Image XResolution': (0x011A) Ratio=72 @ 176,
    'Image YResolution': (0x011B) Ratio=72 @ 184,
    'Image ResolutionUnit': (0x0128) Short=Pixels/Inch @ 102,
    'Image Software': (0x0131) ASCII=Shotwell 0.22.0 @ 192,
    'Image YCbCrPositioning': (0x0213) Short=Centered @ 126,
    'Image ExifOffset': (0x8769) Long=208 @ 138,
    'GPS GPSVersionID': (0x0000) Byte=[2, 2, 0, 0] @ 830,
    'GPS GPSLatitudeRef': (0x0001) ASCII=N @ 842,
    'GPS GPSLatitude': (0x0002) Ratio=[44, 51, 24163/1250] @ 934,
    'GPS GPSLongitudeRef': (0x0003) ASCII=W @ 866,
    'GPS GPSLongitude': (0x0004) Ratio=[0, 34, 169537/10000] @ 958,
    'GPS GPSAltitudeRef': (0x0005) Byte=0 @ 890,
    'GPS GPSAltitude': (0x0006) Ratio=58 @ 982,
    'GPS GPSTimeStamp': (0x0007) Ratio=[12, 28, 10] @ 990,
    'GPS GPSDate': (0x001D) ASCII=2019:03:28 @ 1014,
    'Image GPSInfo': (0x8825) Long=820 @ 150,
    'EXIF ExposureTime': (0x829A) Ratio=1/1093 @ 586,
    'EXIF FNumber': (0x829D) Ratio=13/5 @ 594,
    'EXIF ExposureProgram': (0x8822) Short=Aperture Priority @ 242,
    'EXIF ISOSpeedRatings': (0x8827) Short=50 @ 254,
    'EXIF ExifVersion': (0x9000) Undefined=0220 @ 266,
    'EXIF ComponentsConfiguration': (0x9101) Undefined=YCbCr @ 278,
    'EXIF ShutterSpeedValue': (0x9201) Signed Ratio=1/1093 @ 602,
    'EXIF ApertureValue': (0x9202) Ratio=69/25 @ 610,
    'EXIF BrightnessValue': (0x9203) Signed Ratio=76 @ 618,
    'EXIF ExposureBiasValue': (0x9204) Signed Ratio=0 @ 626,
    'EXIF MaxApertureValue': (0x9205) Ratio=69/25 @ 634,
    'EXIF MeteringMode': (0x9207) Short=CenterWeightedAverage @ 350,
    'EXIF LightSource': (0x9208) Short=Unknown @ 362,
    'EXIF Flash': (0x9209) Short=Flash did not fire @ 374,
    'EXIF FocalLength': (0x920A) Ratio=37/10 @ 642,
    'EXIF MakerNote': (0x927C) Undefined=[7, 0, 1, 0, 7, 0, 4, 0, 0, 0, 48, 49, 48, 48, 2, 0, 4, 0, 1, 0, ... ] @ 650,
    'EXIF UserComment': (0x9286) Undefined=User comments @ 748,
    'EXIF FlashPixVersion': (0xA000) Undefined=0100 @ 422,
    'EXIF ColorSpace': (0xA001) Short=sRGB @ 434,
    'EXIF ExifImageWidth': (0xA002) Signed Long=2524 @ 446,
    'EXIF ExifImageLength': (0xA003) Signed Long=1662 @ 458,
    'Interoperability InteroperabilityIndex': (0x0001) ASCII=R98 @ 800,
    'Interoperability InteroperabilityVersion': (0x0002) Undefined=[48, 49, 48, 48] @ 812,
    'EXIF InteroperabilityOffset': (0xA005) Long=790 @ 470,
    'EXIF SensingMethod': (0xA217) Short=One-chip color area @ 482,
    'EXIF SceneType': (0xA301) Short=Directly Photographed @ 494,
    'EXIF ExposureMode': (0xA402) Short=Auto Exposure @ 506,
    'EXIF WhiteBalance': (0xA403) Short=Auto @ 518,
    'EXIF DigitalZoomRatio': (0xA404) Ratio=3 @ 770,
    'EXIF SceneCaptureType': (0xA406) Short=Standard @ 542,
    'EXIF Saturation': (0xA409) Short=Normal @ 554,
    'EXIF Sharpness': (0xA40A) Short=Normal @ 566,
    'EXIF ImageUniqueID': (0xA420) ASCII=S08Q0LEGC01 @ 778}
    ```

**Question 2** Afficher la valeur correspondant à la clé `'Image Make'`.

??? note "Correction"

    ```python
    data['Image Make']
    ```

**Question 3** Modifier cette valeur pour que l'appareil apparaisse comme étant fabriqué par Apple.


??? note "Correction"

    ```python
    data['Image Make']="(0x010F) ASCII=APPLE @ 158"
    ```

**Question 4** Repérer dans le dictionnaire les renseignements relatifs à la latitude et la longitude enregistrées dans les métadonnées de cette image.  <br />
Attention, les données sont au format Degré Minutes Secondes. <br />
La dernière valeur donnée est donnée sous forme de quotient, il faut le calculer !<br />
Vous pourrez utiliser le site [https://www.coordonnees-gps.fr/](https://www.coordonnees-gps.fr/)


??? note "Correction"

    ```python
    print(data['GPS GPSLatitudeRef'])
    print(data['GPS GPSLatitude'])
    print(data['GPS GPSLongitudeRef'])
    print(data['GPS GPSLongitude'])
    ```
    soit `N[44, 51, 24163/1250]W[0, 34, 169537/10000]`
    En DMS, la latitude est <mark>44°51'19.3304''Nord</mark>. La longitude est <mark>0°34'16.9537'' Ouest</mark>.
    Ce qui donne :
    ![localisation](data/localisation_liberty.png){: .center width=30%}
    En effet, cette photographie a été prise **Place Picard, à Bordeaux**, où se trouve une Statue de la Liberté.
    ![image](data/place_picard.png){: .center width=30%}

??? note "Cyber"

    Cette technique d'analyse des meta-données est très utilisé en **OSINT**.

    L'OSINT, ou **Open Source Intelligence**, se réfère à la collecte et à l'analyse de renseignements provenant de sources ouvertes et accessibles au public. Il s'agit d'une pratique utilisée dans le domaine de la sécurité et de la défense pour rassembler des informations stratégiques à partir de sources telles que les médias sociaux, les sites web, les forums en ligne, les bases de données publiques, les rapports gouvernementaux, et d'autres ressources accessibles au grand public.

    L'objectif de l'OSINT est d'obtenir des informations pertinentes qui peuvent contribuer à évaluer les menaces potentielles, à comprendre les intentions d'acteurs malveillants, à anticiper des incidents de sécurité, et à prendre des décisions éclairées en matière de sécurité.

    Les praticiens de l'OSINT utilisent souvent des outils spécialisés pour automatiser la collecte et l'analyse de données provenant de diverses sources, tout en respectant les limites légales et éthiques. L'OSINT est un élément clé dans le domaine de la cyberdéfense, fournissant une perspective externe sur les activités potentiellement malveillantes et contribuant à renforcer la posture de sécurité d'une organisation.

## Exercice 5 : résolution du pydéfi Pokémons "le seul et unique"

D'après le [défi](https://callicode.fr/pydefis/PokePlusRare/txt) proposé par L.Signac .

![pokémons](data/cap_pydefi.png){: .center}

**Travail préalable**

Nous allons travailler avec les quelques données suivantes, présentées sous forme d'une <mark>liste de listes</mark> :

```python
L = [['givrali', '75', '46'],
 ['branette', '35', '153'],
 ['kyogre', '23', '-10'],
 ['roserade', '-87', '91'],
 ['balignon', '44', '-155'],
 ['keunotor', '32', '163'],
 ['givrali', '-22', '124'],
 ['kyogre', '-54', '-26'],
 ['pyronille', '11', '-102']]
```

**Question 1** Créer un dictionnaire `pokemon` dont la clé sera le nom du Pokémon, et la valeur le tuple de ses coordonnées.
Si le Pokémon est en double dans la liste, sa valeur sera alors la chaîne de caractère `"doublon"`.


??? note "Correction"

    ```python
    pokemon = {}
    for personnage in L :
        nom = personnage[0]
        if nom in pokemon :
            pokemon[nom] = "doublon"
        else :
            pokemon[nom] = (personnage[1],personnage[2])
    ```


**Question 2**  Les données d'entrée du pydéfi ont été enregistrées dans le fichier [input_defi.txt](data/input_defi.txt). Les lignes suivantes permettent de parcourir chacun des personnages de la liste.


```python
#exemple de code pour lire un fichier
fich = open("input_defi.txt", "r")
for ligne in fich.readlines():
    personnage = ligne[:-1] #on enlève le caractère de retour à la ligne \n
    personnage = personnage.split(",") # on sépare les trois éléments de personnage, qui deviennent une liste
```

Tous les personnages ont été parcourus : seul le dernier ("tauros" s'affiche).
Grâce au code ci-dessous et à la question 1, créer de la même manière qu'à la question 1 un dictionnaire qui contiendra tous les pokemons. 


??? note "Correction"

    ```python
    pokemon = {}
    fich = open("input_defi.txt", "r")
    for ligne in fich.readlines():
        personnage = ligne[:-1] 
        personnage = personnage.split(",") 
        nom = personnage[0]
        if nom in pokemon :
            pokemon[nom] = "doublon"
        else :
            pokemon[nom] = (personnage[1],personnage[2])
    ```

**Question 3** Répondre au défi : quelles sont les coordonnées du seul pokémon unique de cette liste ?


??? note "Correction"

    ```python
    for (cle, valeur) in pokemon.items() :
    if valeur != "doublon" :
        print(valeur)

    ```
   

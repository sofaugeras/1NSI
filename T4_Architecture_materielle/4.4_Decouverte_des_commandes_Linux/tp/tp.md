On s’appuieras notamment sur les ressources suivantes :

!!!- info "Ressources"
    - Le chapitre 24 du manuel (Spécialité NSI, Th. Balabonski et al., Ellipses)
    - Le site [informatiquelycee](https://pixees.fr/informatiquelycee/n_site/nsi_prem_os_intro.html) proposé sous licence ![image](data/ccbyncsa.png){ width=10%} par le collègue D. Roche du lycée de Bonneville pour une présentation générale des systèmes d’exploitation, et surtout [ici](https://pixees.fr/informatiquelycee/n_site/nsi_prem_cmd_base_linux.html) pour une présentation de la ligne de commande.

!!! bug "Environnement"

    Pour éviter toute installation, tout en disposant toujours du même environnement de base, disponible depuis toute machine connectée à Internet, on utiliseras à distance sur une machine [« Weblinux »](http://weblinux.univ-reunion.fr) depuis un navigateur. Après le lancement, la connexion est automatiquement, en tant qu’utilisatrice `alice` et dans le répertoire personnel d'alice. 
 
    ![image weblinux](data/weblinux.jpg){ .center width=50%}

    En bas du shell, les trois icônes permettent (de gauche à droite) de :<br />
    :fontawesome-solid-box: Sauvegarder sur son PC une archive (.tar) qui reprend une grande partie du dossier personnel d’alice (ce qui te permet de fournir la trace de ton travail au prof notamment!)<br />

    :material-arrow-up-bold-circle-outline: D’envoyer un fichier de son PC vers la WebLinux. Il sera présent dans le répertoire personnel, à sa base.<br />

    :material-clipboard-text-play-outline:	De coller dans le shell du texte que tu as copié sur son PC : après avoir copié, clic droit dans cette zone `clipboard` puis coller <br />

    Par défaut, l’invite de commande y reste réduite à un simple `$`. On peut la rendre plus complète en exécutant la commande suivante (c’est le moment idéal pour tester le copier-coller qu’on vient d’évoquer !) :

    ```shell
    PS1="\[\033[01;32m\][\u@\h\[\033[00m\]:\[\033[01;35m\]\w]\[\033[00m\]$" # (1)
    ```
    
    1.  Nous ne l’expliquerons pas ici et il n’est pas indispensable de réaliser cette manipulation tout de suite.

    Prenez des notes de vos manipulations pour vous souvenir de ce que vous faites
 
### 1. Explorer l’arborescence

On va d’abord utiliser des commandes shell qui permettent de se **déplacer** dans l’arborescence, de **visualiser** les répertoires, fichiers, ainsi que d'**récupérer** des informations sur eux :<br />

1.	Exécute `pwd` (pour « Print Working Directory ») qui donne l’adresse du répertoire dans lequel on se trouve. <br />
    Est-ce une **adresse absolue** ou une **adresse relative**? <br />
    Comment le voit-on?<br />
    _Note_ : si tu n’es pas à l’aise avec la différence entre adresse absolue ou adresse relative (notion vue avec le HTML notamment), tu peux lire [l’article suivant](https://www.alsacreations.com/astuce/lire/78-Quelle-est-la-difference-entre-les-chemins-relatifs-et-absolus-.html)

2.	Pour lister le contenu du répertoire courant (on dit aussi parfois dossier), utilise `ls`. 
    Combien d’éléments contient-il?<br />

3.	On peut ajouter des options à la commande :<br />

    - `ls -a` (pour «all») permet de lister également les fichiers «cachés» (au sens large, les systèmes POSIX, ou « de type UNIX », voient les répertoires comme des fichiers particuliers), à savoir ceux qui ont un nom commençant par `.` et qui sont invisibles par défaut.<br />
    On voit apparaître notamment le `.` qui représente le répertoire courant, ainsi que `..` qui désigne le dossier **« parent »** situé au niveau juste au dessus dans l’arborescence.<br />

    - `ls -l` (pour « long ») donne une description plus complète. Reporter vous au cours pour voir la décomposition des informations sur la ligne (le premier caractère de chaque ligne indique s’il s’agit d’un fichier classique (-) ou d’un répertoire (d pour directory), etc ...)<br />
    
    - On peut combiner les options : `ls -a -l` ou `ls -al`. Donne le nom d’un répertoire, celui d’un fichier ordinaire caché et celui d’un fichier ordinaire non caché.

    - On peut aussi donner en argument le dossier à lister. Exécute `ls /` ou `ls -l /` et indique le nombre de répertoires immédiatement présents à la racine de l’arborescence (ignore le linuxrc qui est un lien symbolique comme l’indique le l en début de ligne...) Vérifie avec `pwd` que tu es toujours dans le même dossier.

4.	`cd` (pour « Change Directory ») permet de se déplacer dans les répertoires. On lui donne en argument (écrit après un espace) l’adresse relative ou absolue où l’on veut se rendre.<br />

    - `cd Documents` ou `cd Documents/` permet ainsi de se placer dans le sous-répertoire ainsi nommé (On peut commencer à écrire le nom du dossier puis utiliser l’autocomplétion en appuyant sur la touche de tabulation).
    Combien de fichiers ordinaires et combien de dossiers contient ce répertoire ?<br />
    - :boom: Reviens dans le dossier parent avec `cd ..` puis remonte d’un niveau encore en exécutant à nouveau la même commande 
    
    !!! tip "Astuce"
        On peut utiliser la flèche «vers le haut» :material-arrow-up: du clavier pour remonter dans l’historique des commandes . Tu aurais pu également saisir directement `cd ../..` dès le départ au lieu de deux fois `cd ..`.

    
    - Note le nom des utilisateurs identifiés sur la Weblinux : ce sont ceux des sous-dossiers de `/home`.
    - Où que tu sois, tu peux revenir à la base de son espace personnel avec `cd` ou `cd ˜`. 
    - `cd -` te permet de revenir au précédent dossier dans lequel tu étais.
 

5.	À l’aide des commandes précédentes, représente l’arborescence (partielle) des fichiers en partant de la racine `/`. 
    Tu peux l’écrire sous la forme suivante :

    ```shell
    /
    |--- bin
    |--- dev
    |--- home
        |	|--- alice
        |	|	|--- ...

    ```
    Limite-toi à un niveau de profondeur, sauf pour `/home/` où tu illustreras les sous-répertoires, et `/home/alice` où tu montreras les fichiers ordinaires et quelques dossiers.

6.	Rends-toi dans le dossier `/home/bob/vide/`.
    Écris une commande unique qui permet alors de se rendre directement dans `/home/alice/Documents/`.

### 2. Expansion de la ligne de commande, motifs

Pour regrouper plusieurs noms de fichiers ou répertoires, on peut utiliser les motifs suivants dans ses commandes. Ils sont remplacés par les valeurs correspondantes avant l’exécution de la commande :

!!! info "Motif"
    - `*` remplace n’importe quelle suite de caractère, éventuellement vide : `ls *.txt` permet de lister tous les fichiers dont le nom se termine par `.txt`
    - `?` remplace un unique caractère quelconque.
    - `[abc]` remplace n’importe quel caractère indiqué entre crochets.
    - `[0-9]`, `[a-zA-Z]`, etc. permettent d’accepter tous les caractères d’un intervalle.
    - En insérant en première position `ˆ` ou `!`, on peut écrire `[ˆabc]` ou `[!abc]` qui désignent tout caractère différent de tous ceux indiqués. On peut travailler aussi avec les intervalles.

> A faire :
    Donne la commande à utiliser pour lister les documents du dossier `~/Compagnon/A22/` qui vérifient la condition proposée, puis note combien il y en a :<br />
    1.	Fichiers dont le nom commence par un **f**<br />
    2.	Fichiers dont le nom commence par un **f** et qui se terminent par **.txt**<br />
    3.	Fichiers dont le nom commence par un **fichier**, suivi d’un **chiffre** quelconque, puis de **.txt**<br />
    4.	Fichiers dont le nom commence par un **fichier**, suivi par n’importe quel **caractère** (un seul), puis de **.txt**<br />
    5.	Fichiers dont le nom commence par **fi**, suivi d’un caractère autre que `c` et que `e`, puis se termine par n’importe quel(s) autre(s) caractère(s).<br />

### 3. Créer, copier supprimer

:arrow_right: Retourne dans l'espace personnel d'alice `cd ~`.<br />

1.	**Affiche** à l’écran le contenu du fichier `/Compagnon/A13/Documents/detail-alice.txt` avec `cat detail-alice.txt`.
    Le nom de la commande vient de `concat` : elle concatène le contenu des fichiers en argument, avant des les envoyer vers la sortie standard qui est par défaut l’affichage dans le shell. On l’utilise souvent pour un fichier unique.
2.	**Déplace** ce fichier (command mv) à la base de ton espace personnel : `mv detail-alice.txt ˜`
    Le `˜` final peut être remplacé par `.` si tu es déjà situé au bon endroit (ici `/home/alice`).
3.	**Crée un fichier** (vide pour l’instant) dans le dossier personnel d'alice, qui a le même nom que toi (utilise ton vrai  nom !) : `touch prenom_nom`
4.	**Détruis** `fichier2.txt` avec `rm fichier2.txt` (commande remove).
5.	**Crée un nouveau dossier local** nommé exo avec la commande `mkdir exo` (make directory). **Copie** le fichier `fichier1.txt` dans ce dossier avec la commande `cp` (copy) qui fonctionne comme `mv` mais conserve le fichier d’origine.
6.	Depuis la racine de ton dossier personnel, tente d’**effacer** le dossier exo avec `rm exo`. Et avec `rmdir exo` (remove directory). Explique les messages d’erreurs.<br />
7. **Crée** un dossier exo2, puis **supprimmez** le.

### 4. Gérer des droits

L’un des intérêts des systèmes conforme au standard POSIX est d’avoir su dès le départ gérer rigoureusement les droits sur les fichiers et répertoires, d’où une bonne solidité de ces systèmes (massivement utilisés en particulier sur les serveurs).

1.	Un utilisateur fait partie de **groupe(s)**, dont un par _défaut_. En fait, le système d’exploitation l’identifie par un numéro (UID, identifiant d’utilisateur ou user ID) ainsi que ses groupes (par leur GID). <br />
Utilise la commande `id` (pas incontournable, pour la suite), afin de déterminer les groupes auxquels appartient `alice` en précisant lequel est le principal (indiqué juste après gid). Vérifie qu’on retrouve également ces informations dans les fichiers (à afficher avec `cat`) `/etc/passwd` et `/etc/group`.<br />

2.	Quand il crée un fichier ou un répertoire, ce dernier _« appartient »_ à cet utilisateur, ainsi qu’à son groupe par défaut (des droits sont alors choisis, configurables avec la commande `umask` que nous expliquerons plus bas). 
    Pour définir ces droits associés au fichier, on divise alors le monde en trois catégories :<bt />
    - L’utilisateur propriétaire, désigné par `u`<br />
    - Les membres du groupe propriétaire `g`<br/>
    - Tous les autres utilisateurs `o` pour other<br />

    Et pour chacune de ces catégories, on attribue ou non chacun des droits suivants :

    - **Lecture** (`r` pour read) qui autorise donc la copie, pour un fichier ordinaire. Pour un répertoire, il permet d’obtenir la liste de ses fichiers.<br />
    - **Écriture** (`w`pour write) qui permet notamment la modification (pour un répertoire, l’ajout, la suppression, le renommage des fichiers qu’il contient).<br />
    - **Exécution** (`x` pour execute), qui indique pour un fichier ordinaire qu’il peut être considéré comme une commande ; pour un répertoire, cela autorise à se positionner dedans, par exemple avec cd).<br />

    Avec `ls -l` on a déjà visualisé ces permissions : après le premier caractère de la ligne, trois blocs de trois caractères rwx dont certains peuvent être remplacés par `-` indiquent (pour u, puis g, puis o) si l’on a accordé le droit (lettre présente) ou non (- présent). Il existe d’autres possibilités que nous laisserons de côté ici, concernant les droits.

    > A Faire : Détaille les droits des dossiers de l’espace personnel d’alice, puis ceux des fichiers ordinaires.

3.	En fait, le propriétaire d’un fichier peut en modifier les droits avec `chmod` (change mode). Seul lui peut le faire, ainsi que le _« super-utilisateur »_ (ou administrateur système) `root` qui a les pleins pouvoirs sur la machine (ce qui est donc dangereux : on ne l’utilise que quand cela est strictement nécessaire).

    La syntaxe est `chmod` modifications fichier, où modifications est composé dans l'ordre
    - du public (une ou plusieurs lettres parmi u, g et o définis ci-dessus, voire a pour « tous », soit all)
    - d’un opérateur (= pour attribuer des droits et seulement ceux-là, + pour ajouter des droits à ceux déjà donnés et - pour en ôter à ceux qui existent) 
    - du ou des droits désignés par l’une ou plusieurs des lettres parmi r, w et x.

    _Exemples :_
    - `chmod o-wx` mon_fichier ôte les droits en écriture et en exécution aux « autres utilisateurs ».
    - `chmod a+x` mon_fichier donne les droits en écriture et en exécution à tous les utilisateurs,
    - On peut même donner plusieurs séries d’attributs, séparées par des virgules.

    `chmod ug=rwx,o=r mon_fichier` donne tous les droits à l’utilisateur et au groupe, mais seulement le droit en lecture aux autres utilisateurs.

    > A faire : Donne à ton tour la commande qui permet d’ôter les droits en écriture et en exécution au groupe et aux autres utilisateurs, pour `fichier1.txt` Vérifie le résultat après exécution avec `ls -l` (`fichier1.txt` se trouve dans `home\Alice\Compagnon\A22`).

4.	On peut utiliser comme précédemment `*` et les autres motifs. Il est également possible de changer les droits **« récursivement »** c’est-à-dire en remontant aussi loin que nécessaire dans les sous-dossiers, en ajoutant l’option `-R`. 
    > A faire : Donne tous les droits à l’utilisateur et ne garde que ceux en lecture pour les autres catégories, pour tous les sous-dossiers du répertoire personnel d’alice dont le nom commence par un S. Puis seulement le droit en lecture pour tout utilisateur, pour tous les fichiers et sous-dossiers à un niveau quelconque du dossier imdb. Vérifie le résulat avec `ls -l`.

5.	Il existe une autre manière de décrire les droits à appliquer : on indique un nombre en **écriture octale** (base 8), dont chacun des trois chiffres (il y en a parfois 4, on n’étudie pas ce cas ici), associés respectivement à `u`, `g` et `o`, est calculé ainsi : on additionne les droits à attribuer, en comptant **4 pour r, 2 pour w et 1 pour x**. Par exemple,`rwx` vaut 7, `rx` vaut 5. On peut choisir directement des droits, mais pas en ajouter ou en ôter, avec cette notation.
> A faire : Indique quels droits sont attribués par `chmod 754 fichier1.txt` puis vérifie ta réponse avec `ls -l`.

6.	La commande `umask` (user mask) sans argument renvoie un **«masque»** qui indique les droits attribués par défaut à la création d’un fichier. En donnant comme argument une valeur octale, on peut choisir une nouvelle valeur pour ce masque.

    Pour déterminer la valeur, on soustrait chiffre par chiffre les droits calculés comme précédemment à `666` pour les fichiers ordinaires et à `777` pour les répertoires. Par exemple, pour obtenir les droits par défaut `644`, soit `rw-r--r--`, sur les fichiers ordinaires, le masque vaut $666-644 = 022$ : on exécute `umask 022`. Du coup, sur les nouveaux répertoires, on aura les droits $777-022 = 755$, soit `rwxr-xr-x` (droit en exécution en plus de ceux des fichiers, autrement dit celui de se positionner dedans avec cd).

7.	Les permissions dépendent des **propriétaires** (utilisateur et groupe) et on peut modifier ces derniers (là encore, seul `root` peut tout faire et un utilisateur peut changer le groupe d’un fichier qui lui appartient). Les commandes utilisées sont `chown` (change owner) et `chogrp` (change group) : `chown bob fichier1.txt` donnerait la propriété de ce fichier à l’utilisateur bob, si on a suffisamment de droits pour exécuter cette commande.
    Il existe également des commandes pour ajouter un utilisateur à un groupe, que nous n’étudierons pas ici.

    > A faire : Donne la commande qui donne le groupe developer à `fichier2.txt`, puis vérifie le résultat.

!!! info "Compléments"
    Le plus important à retenir, surtout quand on connaît une commande mais pas ses options, ou si l’on découvre une commande inconnue dans un exemple, est de savoir accéder à l’information intégrée au shell :<br />
    - `man la_commande` renvoie une aide complète (souvent plus longue qu’une page, on peut ajouter à la suite |less pour se déplacer dedans avec les flèches, puis quitter avec q, voir à la suite pourquoi). `info la_commande` offre un service comparable.<br />
    - Plus simplement, la plupart des commandes ont une option `-help` (en général, double tiret pour une option qui s’écrit sur plus d’un caractère) ou `-h` qui décrit leur utilisation.
    Avec `ls -help`, trouve comment lister le contenu d’un répertoire en triant les éléments par ordre décroissant de taille.<br />
    - Si tu utilises un moteur de recherche, pense à inscrire l’un des mots `shell` ou `bash` en plus de celui de la commande ou de la fonctionnalité recherchée... 

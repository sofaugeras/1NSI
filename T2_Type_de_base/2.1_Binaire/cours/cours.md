# Binaire

Règle du jeu : Disposer les cartes dans l’ordre ci-dessous sur la table. Vous ne pouvez que retourner ou non chaque carte. Il s'agit ensuite de compter le nombre de points visibles.




1ère étape :  
	A tour de rôle, demander à votre binôme d’afficher un entier choisi au hasard (ex :  6 , 21, 15 …)
Existe-t-il un nombre qui peut être représenté de 2 façons différentes avec les cartes ?
 ……………………………………………………………………………………………………………………………………………..

Peut-on afficher n'importe quel entier ? ……………………………………………………………………………..
Quel est le maximum ?  ……………………………………………………………………………..
	Compter à partir de 0 et essayer de repérer le mécanisme de progression.

2ème étape : Pour chaque carte,   on note 1  si elle est tournée du côté visible (recto).
				    et   on note 0  si la face est invisible (côté verso).
Quel nombre est représenté par le mot  01001 ? ……………….
Quel nombre est représenté par le mot  00000 ? ……………….
Quel nombre est représenté par le mot  11111 ? ……………….

Comment écrit-on 17 en binaire ?  …………………………..
Etc … entraîner votre binôme à convertir dans le sens nombre => binaire  et  binaire => nombre.
Le système binaire est un système de numération de position de base deux : les deux seuls chiffres qui le composent sont le "0" et le "1".
Le système binaire est le "langage" des ordinateurs. Toutes les machines numériques utilisent le système binaire pour coder des informations (textes, sons, images, vidéos…).
L'ordinateur communique avec le monde extérieur en envoyant des informations sous la forme de nombres binaires à 8 bits appelés octets.
ATTENTION 
Un octet (Byte) représente 8 bits (BInary digiT)


 
3ème étape : 
Chaque carte représente en fait un "bit" (binary digit). Un ensemble de bits est appelé un « mot ».  Combien existe-t-il de mots de 8 bits ?  ....................   Ces mots codent les entiers de …… à ………     Un mot de 8 bits s’appelle  ......................    Flécher le « bit fort » et le « bit faible » dans         0 1 0 1 0  .
et si on passait en système Décimal ….

Décimal vers Binaire
|$2^7$|$2^6$|$2^5$|$2^4$|$2^3$|$2^2$|$2^3$|$2^3$|
|-|
0								
1								
2								
3								
4								
5								
6								
7								
8								
9								
10								
11								
12								
13								
14								
15								
16								
20								
50								
100								
255								

Pour communiquer avec un ordinateur il est donc nécessaire de savoir convertir un nombre décimal en un nombre binaire. Une méthode de conversion consiste à décomposer le nombre décimal en une somme de puissances de deux.
Par exemple, pour la conversion : (91)décimal = (01011011)binaire
On peut écrire : 
91 	= 0 x 27 + 1 x 26 + 0 x 25 + 1 x 24 + 1 x 23 + 0 x22 + 1 x 21 + 1 x20
= 64 + 16 + 8 + 2 + 1

En rangeant les puissances de deux dans un tableau, on obtient :

Rang	7	6	5	4	3	2	1	0
Puissance de 2	27	26	25	24	23	22	21	20
Décimal	128	64	32	16	8	4	2	1
Nombre binaire	O	1	0	1	1	0	1	1

 
Méthode :
Dividende : diviseur :
- on divise N = 91 	par 27 = 128 quotient = 0 	et reste = 91 (car N < 128)
- on divise 91 		par 26 = 64 quotient = 1	 	et reste = 27
- on divise 27 		par 25 = 32 quotient = 0 	et reste = 27 (car 27 < 32)
- on divise 27 		par 24 = 16 quotient = 1 	et reste = 11
- on divise 11 		par 23 = 8 quotient = 1 		et reste = 3
- on divise 3 		par 22 = 4 quotient = 0 		et reste = 3 (car 3 < 4)
- on divise 3 		par 21 = 2 quotient = 1 		et reste = 1
- on divise 1 		par 20 = 1 quotient = 1 		et reste = 0
On constate que :
- le quotient vaut : 0 quand le dividende < diviseur et 1 quand le dividende > diviseur.
- les quotients des divisions, selon l'ordre décroissant des puissances de 2, donne le nombre binaire cherché
- le reste d'une division est inchangé quand le dividende est plus petit que le diviseur.

Définition :
•	Codage : Opération consistant à représenter des informations à l'aide d'un code.
•	Codage binaire : Le code binaire utilise exclusivement les symboles 0 et 1 (systèmes logiques).
•	Bit : C'est le chiffre élémentaire de la numérotation binaire.
•	Mot : Groupe de "n" bits; un mot de 4 bits s'appelle un quartet, 8 bits s'appelle un octet...
•	Poids : Coefficient attaché au rang d'un chiffre dans un système de numérotation. En numérotation binaire, on parle du bit de plus faible poids qui est la position binaire de droite dans un mot et du bit de plus fort poids qui représente le bit situé le plus à gauche dans mot.

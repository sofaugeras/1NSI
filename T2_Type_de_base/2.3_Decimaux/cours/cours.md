# 2.8 Codage des non-entiers

![image](../data/BOFlottant.png){: .center}

## 1. Notation binaire des décimaux

### a. Écriture de position

Comme la notation décimale, la notation binaire permet aussi de représenter les nombres à virgule.<br />

En notation décimale, les chiffres de gauche représentent les unités, les dizaines et ainsi de suite
et ceux à droite de la virgule, les dixièmes, les centièmes etc.

![decomposition decimal](../data/decimalDecomposition.png){: .center}

De même, en notation binaire, les chiffres de droite représentent des demis, des quarts, des
huitièmes etc.

![decomposition bianire](../data/binaireDecomposition.png){: .center}

!!! abstract "Exercice"
    === "Énoncé"
        Trouver les nombres dont la représentation en binaire est :<br />
        :arrow_forward: 1 001,101 1 <br />
        :arrow_forward: 10 101,011 101 <br />
    === "Correction"
        :arrow_forward: 1 001,101 1 code <br />
        :arrow_forward: 10 101,011 101 code <br />

### b. De l’écriture décimale à la notation binaire

!!! note "Écriture d'un nombre décimal en binaire :heart:"

    conversion de 12, 6875 en binaire<br />
    :one: Conversion de 12 donne $(1100)_2$<br />
    :two: On effectue successivement des multiplications par 2 de la partie décimale, on conserve les parties entières<br />

    ![image](../data/decimalMultiplication.png){: .center}

    :arrow_forward: Donc la conversion de 0,6875 en binaire est $(0,1011)_2$

!!! abstract "Exercice 1"
    === "Énoncé"
        Donner l'écriture binaire de 7,09375.
    === "Correction"
        - partie entière : $7 = 101_2$
        - partie décimale :
            - $0,09375 \times 2 = \textbf{0},1875$ 
            - $0,1875 \times 2 = \textbf{0},375$ 
            - $0,375 \times 2 = \textbf{0},75$ 
            - $0,75 \times 2 = \textbf{1},5$
            - $0,5 \times 2  = \textbf{1}$
 
        Donc $7,09375=101,00011_2$

!!! abstract "Exercice 2"
    === "Énoncé"
        Donner l'écriture binaire de 0,2.
    === "Correction"
        - partie entière : $0 = 0_2$
        - partie décimale :
            - $0,2 \times 2 = \textbf{0},4$  
            - $0,4 \times 2 = \textbf{0},8$
            - $0,8 \times 2  = \textbf{1},6$
            - $0,6 \times 2  = \textbf{1},2$
            - $0,2 \times 2 = \textbf{0},4$ 
            - *et cela continue...*
 
        Le nombre 0,2 n'admet pas d'écriture binaire **finie**.

**Problèmes :**

- le processus de "conversion" ne s'arrête pas, nous obtenons une écriture **binaire infinie périodique**. 

??? note "Remarque"  
    certains nombres (par exemple : $7/11 = 0.63636363 …$) ont une écriture décimale infinie périodique. Ils auront alors une écriture binaire infinie périodique. <br />
    Et certains nombres ont une écriture binaire infinie périodique, alors même que leur écriture décimale est finie (exemple : 0.2)

**Moralité :**

Ce système d'écriture ne marche pas bien.

**Conclusion :**

Certains nombres n'admettent pas une écriture binaire **finie**. Or la mémoire d'un ordinateur, quelqu'il soit, est toujours finie. Certains nombres ne peuvent donc pas être représentés correctement en machine : c'est une impossibilité théorique. Cela amène à des comportements étranges : 

```python
>>> 0.1 + 0.2
0.30000000000000004
```

**Remarque :** parmi les nombres décimaux à un chiffre après la virgule (0,1  0,2  0,3 ...) seul 0,5 admet une écriture binaire finie ! Tous les autres ont une représentation en machine qui n'en donne qu'une valeur approchée.

## 2. Norme IEE754

### a. Notation scientifique

En notation décimale, elle consiste à exprimer le nombre sous la forme $\pm a \times 10^n$ où $\pm$ est appelé _signe_, $a$ est un nombre décimal de l’intervalle $[1 , 10[$ appelé _mantisse_ (ou significande) et $n$ est un entier relatif appelé _exposant_.

:question: Quel est la notation scientifique de $105,745$
??? "Réponse"
	$1,05745 \times 10^2$

:question: Quel est la notation scientifique de $0, 0745$
??? "Réponse"
	$7,45 \times 10^-2$

De même, en notation binaire, tout ombre s’exprime sous la forme $\pm a \times 2^n$ où $\pm$ où $\pm$ est le _signe_, $a$ est un nombre de l’intervalle $[(1)_2 , (10)_2[$ appelé _mantisse_ et $n$ est un entier relatif appelé _exposant_.

:question: Quel est la notation scientifique de $1011, 0111 101$
??? "Réponse"
	$1,0110111 101 \times 2^3$

:question: Quel est la notation scientifique de $0, 0000001101$
??? "Réponse"
	$1,101 \times 2^-7$

### b. Représentation des nombres à virgule en binaire sur n bits

!!! abstract "Principe de la [norme IEE754](https://fr.wikipedia.org/wiki/IEEE_754)"
    On utilise la notation scientifique en binaire $(-1)^s \times 1,m \times 2^{p-127}$.<br />
    Pour une représentation sur 32 bits (en simple précision),<br />
    - le bit de poids fort (à gauche) donne le _signe_ 0 pour positif et 1 pour négatif<br />
    - Les 8 bits suivants pour _exposant_, on représente l’entier relatif $p$ par $p-127$<br />
    - les 23 bits suivant pour partie après la virgule de la _mantisse_

    ![norme IEE754](../data/IEE754vierge.png){: .center}


:question: Trouver la représentation en binaire sur 32 bits de $1011, 0111 101$
??? "Réponse"
	$ $

:question: Trouver la représentation en binaire sur 32 bits de $0, 0000001101$
??? "Réponse"
	$ $

:question: Trouver la représentation en binaire sur 32 bits de $110100011010010011110000011100000$
??? "Réponse"
	$ $

:question: Trouver la représentation en binaire sur 32 bits de $00100001111010011100101011000000$
??? "Réponse"
	$ $

!!! note "Convention"
    Par convention :<br />
    – Il y a deux **zéro**, un positif et un négatif : $\pm 00000000 00000000000000000000000$<br />
    – L’**infini** : $\pm 11111111 00000000000000000000000$<br />
    – **NaN** : not a number : $\pm 11111111 01000000000000000000000$

## 3. Comment faire des tests d'egalité sur les flottants ? 

Première réponse : ON N'EN FAIT PAS.

Si `a` et `b` sont deux flottants, le test classique

```python
if a == b :
    print("a et b sont égaux")
```

a de grandes chances d'échouer :

Le script 

```python linenums='1'
a = 0.1
b = 0.3 - 0.2
if a == b :
    print("a et b sont égaux")
else :
    print("a et b sont différents")
```

renverra

```
a et b sont différents
``` 


Si *vraiment* un test d'égalité est nécessaire, on ne va pas tester l'égalité entre ```a``` et ```b``` mais leur **proximité**, grâce à la valeur absolue de leur différence.

La fonction `abs(a-b)` renvoie un nombre positif égal à la distance entre `a` et `b`. Il faut alors décider d'un écart minimal `e` en dessous duquel on considèrera que `a` et `b` sont égaux.

Le script 

```python
a = 0.1
b = 0.3-0.2
e = 10**(-12)
if abs(a-b) < e :
    print("a et b sont égaux")
else :
    print("a et b sont différents")
```

renverra
```
a et b sont égaux
``` 
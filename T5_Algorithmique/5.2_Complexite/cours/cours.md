# 4.2 Complexité d'un algorithme 

![image](data/meme.png){: .center width=40%}

???+ cite "Activité"
    ![Machine de Turing en papier](data/machineTuring.jpg){: .center width=40%}
    [Computer Paper - Do It Yourself ](https://www.espace-turing.fr/IMG/pdf/computerpaper.pdf)

    Dans un article qui fera date, « On Computable Numbers with an Application to the Entscheidungsproblem » publié en 1936, **Alan Turing**, jeune mathématicien anglais, jette les bases de ce qui deviendra la <emphrase>théorie de la calculabilité</emphrase> en répondant par la négative à la question de savoir si toute proposition peut être démontrée dans un système formel. Pour ce faire, il imagine une machine à calcul universelle ... en papier.

    Cette machine est composée d’un « ruban » supposé infini, chaque case contenant un symbole parmi un _alphabet fini, d’une tête de lecture/écriture, d’un registre d’états, d’une liste d’instructions.

    L’ordinateur - **théorique** - est né !

    Turing définit le calcul sous la forme d’une liste finie d’instructions, itérables un nombre indéfini de fois. Il vient de poser les fondements de la science informatique. Il n’a que 24 ans !

    Pour le centenaire de sa naissance, nous vous proposons de faire un voyage dans le temps, en construisant votre propre ordinateur en papier, à la manière d’Alan Turing il y a 76 ans.

!!! tldr "Pour résumé"
    <iframe width="560" height="315" src="https://www.youtube.com/embed/P66h8D5Lkwk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>{: .center}
    <br />
    [La machine de Turing, une révolution des mathématiques et de l'informatique - Passe-science](https://www.youtube.com/watch?v=P66h8D5Lkwk) (début à 3’30)

    On retiendra ici, que le modèle de la machine de Turing, sert d'étalon pour mesurer la complexité d'un algorithme : C'est l'ordre de grandeur du nombre d'opérations élémentaires (lire, déplacer la tête de lecture) qu'effectuerait une machine de Turing pour effectuer l'algorithme.

La **complexité** d'un algorithme est une notion qui nous éclaire sur la manière dont cet algorithme va être sensible à la taille des données passées en paramètre. Il y a plusieurs types de complexités étudiables (nombre d'opérations, temps nécessaire, espace-mémoire nécessaire...).

En NSI, nous nous contenterons d'estimer (lorsque cela est possible) le nombre d'opérations effectuées par l'algorithme, et nous mesurerons les temps d'exécution de ces algortihmes. 

!!! example "Exemple"

    ```python
    def fonction1(n) :
        a=0
        for i in range(n):
            a=a+1
        return a
    ```
    ```python
    def fonction2(n):
        a=0
        for i in range(n):
            a=a+1
        for i in range(n):
            a=a+1
        return a
    ```
    ```python
    def fonction3(n):
        a=0
        for i in range(n):
            for j in range(n)
                a=a+1
        return a
    ```

Nous observerons surtout comment évolue ce temps d'exécution en fonction de la taille des données passées en paramètre (la taille d'une liste, par exemple). Cela nous permettra dans ce cours de classer nos algorithmes en deux catégories : les algorithmes de complexité **linéaire** et ceux de complexité **quadratique**.

## 1. Complexité linéaire

### 1.1 Exemple 

!!! aide "Exemple d'algorithme"
    ![image](data/env.png){: .center}
    Votre travail est de mettre des bulletins dans des enveloppes pour une campagne de communication.  
    L'algorithme en jeu ici est "je prends un bulletin, je le plie, je le mets dans l'enveloppe, je ferme l'enveloppe". 
    
    On suppose que vous travaillez à un rythme constant.  
    Le premier jour, on vous donne $n$ enveloppes à remplir. Vous mettez un temps $T$ pour les traiter.  
    Le deuxième jour, suite à l'absence d'un employé, on vous donne le double d'enveloppes, soit $2n$ enveloppes. Combien de temps allez vous mettre pour les traiter ?

    ??? tip "*Réponse*"
        Cela prendra deux fois plus de temps, donc $2T$.

### 1.2 Vocabulaire 

On dit que l'algorithme ci-dessus est de complexité **linéaire**.  

!!! note "Complexité linéaire :heart:"
    Les expressions suivantes sont équivalentes :
    
    - L'algorithme est de **complexité linéaire**.
    - L'algorithme est **d'ordre n**.  
    - L'algorithme est en **$O(n)$** *  
    («grand O de n»)*

    Toutes ces formulations renvoient à la même idée : le nombre d'opérations nécessaires (et donc le temps nécessaire à la terminaison de l'algorithme) évolue **proportionnellement** avec le nombre de données à traiter.

### 1.3 Formulation mathématique
Si un employé A met 3 secondes par enveloppe, on aura $T_A=3n$.  
Si un employé B met 20 secondes par enveloppe, on aura $T_B=20n$.  

On retrouve la formulation mathématique d'une fonction linéaire $f$.  

$$f : x \mapsto ax \quad\text{ , avec } a \in \mathbb{R}$$

Ici, la fonction $f_A$ serait $f_A(x)=3x$, la fonction $f_B$ serait $f_B(x)=20x$

Dans **les deux cas** l'algorithme a la même complexité (linéaire donc). Ce qui compte est le fait que pour chacun des employés, **avoir deux fois plus d'enveloppes prendrait deux fois plus de temps**.

### 1.4 Vérification expérimentale 
On considère la fonction ci-dessous :


```python
def fabrique(n):
    liste = []
    for _ in range(n):
        liste.append("ok")
    return liste
```

Le code ci-dessous va mesurer le temps d'exécution de cette fonction avec deux paramètres différents : la valeur 400 puis la valeur 800.


```python
import time
t0 = time.time()
lstA = fabrique(400)
print("temps pour une liste de taille 400 :", time.time() - t0)
t0 = time.time()
lstB = fabrique(800)
print("temps pour une liste de taille 800 :", time.time() - t0)
```

Résultats de l'exécution :

```python
temps pour une liste de taille 400 : 2.384185791015625e-05
temps pour une liste de taille 800 : 4.2438507080078125e-05
```

**Interprétation :**  
Doubler la taille du paramètre d'entrée a eu pour effet de doubler (quasiment) le temps d'exécution. Cela semble indiquer que la complexité de cette fonction est **linéaire**.  
En observant l'algorithme, nous pouvons confirmer cette supposition : le nombre d'opérations de la boucle ```for``` est égal au paramètre ```n```, et est donc directement proportionnel à la valeur de ce paramètre.


## 2. Complexité quadratique

### 2.1 Exemple 

!!! aide "Exemple d'algorithme"
    ![](data/terrain.png){: .center}
    Vous avez l'habitude de tondre la pelouse de votre terrain carré, de côté $n$. Cela vous prend un certain temps $T$.  
    Votre voisin vous propose de venir chez lui tondre son terrain carré de côté $2n$.   
    Combien de temps cela va-t-il vous prendre pour tondre le terrain de votre voisin ?

    ??? note "*Réponse*"
        Cela vous prendra **4 fois** plus de temps.



### 2.2 Vocabulaire 

On dit que l'algorithme ci-dessus est de complexité **quadratique**.  

!!! note "Complexité quadratique :heart:"
    Les expressions suivantes sont équivalentes :
    
    - L'algorithme est de **complexité quadratique**.
    - L'algorithme est **d'ordre n au carré**.  
    - L'algorithme est en **$O(n^2)$** *  
    («grand O de n carré»)*

    Toutes ces formulations renvoient à la même idée : le nombre d'opérations nécessaires (et donc le temps nécessaire à la terminaison de l'algorithme) évolue **proportionnellement avec le carré** du nombre de données à traiter.


Les algorithmes quadratiques sont moins «intéressants» que les algorithmes linéaires, car ils vont consommer beaucoup plus de ressources. Lors de l'élaboration d'un algorithme, on va toujours essayer de trouver l'algorithme ayant la complexité la plus faible possible.

### 2.3 Vérification expérimentale 
On considère la fonction ci-dessous :

```python
def tables(n):
    for a in range(n):
        for b in range(n):
            c = a * b

```

Le code ci-dessous va mesurer le temps d'exécution de cette fonction avec deux paramètres différents : la valeur 100 puis la valeur 200.


```python
import time
t0 = time.time()
tables(100)
print("temps pour n = 100 :", time.time() - t0)
t0 = time.time()
tables(200)
print("temps pour n = 200 : ", time.time() - t0)
```


Résultats de l'exécution :

```python
temps pour n = 100 : 0.0003533363342285156
temps pour n = 200 : 0.0014693737030029297
```

**Interprétation :**  
Doubler la taille du paramètre d'entrée a eu pour effet de **quadrupler** le temps d'exécution. Cela semble indiquer que la complexité de cette fonction est **quadratique**, car $2^2=4$.  

En observant l'algorithme, nous pouvons confirmer cette supposition : le nombre d'opérations des deux boucles ```for``` est égal à ```n^2```.


## 3. Complexité constante

Il peut arriver (mais c'est rare) que la complexité d'un algorithme soit indépendante de la taille des données à traiter.  
Dans ce cas, c'est souvent une très bonne nouvelle.

Observons l'accès au 1er élément d'une liste :



!!! note "Complexité constante :heart:"
    Les expressions suivantes sont équivalentes :
    
    - L'algorithme est de **complexité constante**.
    - L'algorithme est **d'ordre 1**.  
    - L'algorithme est en **$O(1)$** *  
    («grand O de 1»)*

    Toutes ces formulations renvoient à la même idée : le nombre d'opérations nécessaires (et donc le temps nécessaire à la terminaison de l'algorithme) est constant quelle que soit la taille des données d'entrée de l'algorithme.

## 3. Les différentes complexités

On peut classer les algorithmes selon leur complexité.

- Complexité **constante** : **$O(1)$**
- Complexité **logarithmique** : **$O(log_{2}(n))$**
- Complexité **linéaire** : **$O(n)$**
- Complexité **quasi-linéaire** : **$O(nlog_{2}(n))$**
- Complexité **polynomiale** : **$O(n^k)$**
- Complexité **exponentielle** : **$O(2^n)$**

## 4. Preuve d’un algorithme

Il est important de pouvoir montrer qu’un programme termine, afin de savoir si son exécution se fera sans problème.
 Parmi les instructions ci-dessous, quelles sont celles qui ne peuvent pas engendrer d’exécution infinie d’un algorithme ? Quelle est/sont la/les seule(s) instruction(s) problématique(s) ?<br />
- Affectation 
- Instruction conditionnelle (if … Then …else …)
- Boucle Pour (for)
- Boucle Tant que (While)

On suppose maintenant que l’on est capable d’écrire un algorithme, appelé Terminator, dont la fonction est de répondre vrai si un programme termine et faux si un programme ne termine pas. Ainsi, l’instruction  `Terminator(P)` renvoie `vrai` si le programme P termine toujours et `faux` si P est capable de boucler.

    Algorithme : SarahConnor
        Tant que _terminator_(sarahConnor) faire
            rien
        fin tant que

À quelle condition le programme `SarahConnor` termine-t-il ? <br />
On comprend donc que le problème de la terminaison des algorithmes n’est pas si simple. On peut énoncer le théorème suivant :

!!! danger "Problème de l'arrêt"
    Il n'existe pas de programme permettant de dire si un algorithme termine toujours ou non.
 
On dit en théorie de l’informatique que le problème de l’arrêt est **indécidable**. En fait, le théorème de Rice dit même que toute propriété non triviale sur les programmes est indécidable. Bien que ce soit vrai dans le cas général, on peut cependant s’intéresser à des cas particuliers et utiliser des propriétés mathématiques pour démontrer que des algorithmes simples terminent.

### 4.1 Définition

!!! danger "Définition de la preuve" 

    On appelle preuve d’un algorithme, la propriété qui assure à ce dernier :<br />
    - de se terminer. On appelle cela la **terminaison** de l’algorithme<br />
    - de réaliser ce qu’’on attend de lui. On appelle cela la **correction** de l’algorithme.<br />

 
### 4.2 Comment ≪prouver≫ ?

#### 4.2.1 Terminaison

Il est fréquent dans l’établissement d’un algorithme, qu’un programmeur ait recours a une structure de boucle.
Lorsque cette dernière est conditionnelle (**while**), et que l’algorithme exécute une première fois les instructions contenues dans la boucle, il est important de s’assurer que l’algorithme sortira de la boucle et se terminera.
Cette propriété de l’algorithme s’appelle la terminaison

Ainsi :
Le groupe d’instructions de la boucle doit permettre une modification de la condition de boucle.

!!! danger "Définition" 

    On appelle **convergent** (ou **variant de boucle**) une quantité qui prend ses valeurs dans un ensemble bien fondé et qui diminue strictement à chaque passage dans une boucle.<br />
    _Remarque_ : Un ensemble bien-fondé est un ensemble totalement ordonné dans lequel il n’existe pas de suite infinie strictement décroissante.

!!! info "Propriété"
    L’existence d’un convergent pour une boucle garantit que l’algorithme finit par en sortir.

!!! info "Propriété" 
    On assure la **terminaison** d’un algorithme lorsque toutes les structures de boucles conditionnelles de celui-ci **≪terminent≫**.

Pour la boucle For en Python, on utilise la fonction range qui est strictement décroissante et positive. La boucle For se termine donc toujours.
En effet, on peut toujours construire un variant simple. 
Si la boucle est donnée par la structure : Pour `i` allant de `a` à `b`, un variant simple est `b − i`

#### 4.2.2 Correction
En outre, la seconde préoccupation du programmeur sera d’assurer que son algorithme réalise bien le travail demande. Cette propriété de l’algorithme s’appelle la correction. Elle est généralement plus délicate à établir.

!!! info "Propriété" 
    On assure la correction d’un algorithme avec boucle en dégageant une propriété vérifiée avant l’entrée dans la boucle et qui le restera durant chaque itération `i` de boucle ; soit $P_i$ cette propriété au rang `i`. Cette propriété doit permettre de renvoyer le résultat attendu au dernier rang de boucle. On l’appelle l’**invariant de boucle**.

!!! danger "Définition" 
    L’invariant de boucle est une formule logique qui :<br />
    — est vérifiée à l’initialisation de la boucle<br />
    — reste vraie à chaque itération de la boucle

### 4.3 Quelques exemples

#### 4.3.1 Factorielle

On considère le script python suivant :
 
!!! abstract
    === "Enoncé"
        On note `n!` le nombre entier défini par  `n! = n x (n - 1) x (n - 2) x … x 3 x 2 x 1`.  (on dira « n factorielle »)
        > Calculer factorielle(4) et 4!, puis factorielle(7) et 7!
    
    === "Correction"

        • Terminaison:
        - Si n entre au clavier est négatif, le programme termine sur un message ("impossible").<br />
        - Si n est nul la boucle n’est pas exécutée, 1 est renvoyé et le programme termine.<br />
        - Si n > 0 k étant initialement a 1, la boucle est exécutée. A chaque itération, k est incrémenté de 1 et finit par être supérieur a n donc pour k=n+1, on sort de la boucle, le programme renvoie f, et termine.<br />
        **CONCLUSION** : la terminaison est assurée.<br />

        • Correction:
        Un invariant de boucle Pi est par exemple :<br />
        **≪après la iieme itération k contient i + 1 et f contient i!≫**<br />
        Cette propriété est vraie au rang 0. Supposons la vraie au rang i, et montrons qu’’elle est héréditaire :<br />
        - Au rang i + 1, on a : k qui contient i + 1 en début d’itération et f = i! × (i + 1) = (i + 1)!<br />
        - En fin d’itération k contient i + 2<br />
        Ceci est bien la propriété au rang i + 1<br />
        **CONCLUSION** : la correction est assurée.

#### 4.3.2 Puissance de 2

!!! abstract "Exercice : Puissance de 2"

    === "Enoncé"

        On considère le code python calculant la puissance nieme de 2 :
        
        ```python
        def puissance2(n) :
            if type(n)==int and n >= 0 :
                p = 1
                while n>0 :
                    p = p*2
                    n=n1-1
            return p


        ```
        > A Faire : Donner la preuve de cet algorithme 

    === "Correction"
    
        • Terminaison:<br />
        - Si n entre au clavier n’est pas un entier positif ou nul le programme termine sur un message ("impossible").<br />
        - Si n est nul la boucle n’est pas exécutée, 1 est renvoyé et le programme termine.<br />
        - Si n > 0, la boucle est exécutée. A chaque itération, n est décrémente de 1 et finit par être nul, on sort de la boucle, le programme renvoie p, et termine.<br />
        **Conclusion** : la terminaison est assurée.

        • Correction:<br />
        Un invariant de boucle est par exemple : <br />
        ≪apres la iieme iteration p contient 2n0−(n0−i) = 2i et n contient ni = n0 − i≫<br />
        Les conditions initiales assurent qu’’au rang 0 la propriété est vraie. Supposons la vraie au rang i, et montrons Qu’elle est héréditaire :<br />
        - Au rang i + 1, on a : p qui contient 2 × 2n0−(n0−(i+1)) = 2i+1<br />
        - En fin d’itération n contient ni+1 = n0 − (i + 1)<br />
        Ceci est bien la propriété au rang i + 1<br />
        **Conclusion** : la correction est assurée.


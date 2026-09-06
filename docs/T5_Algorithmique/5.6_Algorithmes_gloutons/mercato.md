# TP Le Mercato du FC Numéria

*ou comment recruter les meilleurs joueurs avec un budget limité ?*

## 0. Mise en situation 🏟️

Le **FC Numéria** vient d'être promu en Ligue 1 ! Pour se renforcer, le club dispose d'un **budget mercato de 150 millions d'euros** et souhaite recruter **au maximum 5 joueurs** parmi une liste de 10 cibles identifiées par le staff technique.

Chaque joueur est évalué selon trois critères notés de 1 à 10 :

| Critère | Description |
|:--:|:--|
| **Compétitivité** | Mental, leadership, hargne en match |
| **Condition physique** | Endurance, explosivité, résistance aux blessures |
| **Efficacité** | Performance technique dans son poste |

Voici la liste des cibles du mercato :

| Joueur | Poste | Compétitivité | Condition | Efficacité | Prix (M€) |
|:--:|:--:|:--:|:--:|:--:|:--:|
| Martinez | ATT | 9 | 8 | 9 | 80 |
| Kowalski | MIL | 7 | 9 | 8 | 45 |
| Diallo | DEF | 8 | 7 | 7 | 35 |
| Fernandez | ATT | 6 | 8 | 9 | 55 |
| Petrov | GK | 9 | 6 | 8 | 30 |
| Okonkwo | MIL | 7 | 8 | 7 | 40 |
| Larsson | DEF | 6 | 9 | 6 | 25 |
| Mbeki | ATT | 8 | 7 | 8 | 60 |
| Reinholt | MIL | 5 | 8 | 7 | 20 |
| Stavros | DEF | 7 | 6 | 6 | 15 |

## 1. Modélisation des données

!!! example "Question 1.1 — Structure de données"
    Quelle structure Python vous semble pertinente pour représenter ces données ?  
    Codez la structure contenant les 10 joueurs avec leurs 4 attributs : compétitivité, condition, efficacité, et prix.

??? tips "Correction"
    Un **dictionnaire** dont la clé est le nom du joueur et la valeur est un tuple `(compétitivité, condition, efficacité, prix)` est une bonne solution : accès direct par nom, structure compacte.

    ```python
    mercato = {
        "Martinez"  : (9, 8, 9, 80),
        "Kowalski"  : (7, 9, 8, 45),
        "Diallo"    : (8, 7, 7, 35),
        "Fernandez" : (6, 8, 9, 55),
        "Petrov"    : (9, 6, 8, 30),
        "Okonkwo"   : (7, 8, 7, 40),
        "Larsson"   : (6, 9, 6, 25),
        "Mbeki"     : (8, 7, 8, 60),
        "Reinholt"  : (5, 8, 7, 20),
        "Stavros"   : (7, 6, 6, 15)
    }
    # tuple : (compétitivité, condition, efficacité, prix)
    #              [0]           [1]        [2]       [3]
    # Accès : mercato["Martinez"][0] → compétitivité
    #         mercato["Martinez"][3] → prix
    ```

## 2. Score global

Le staff technique souhaite résumer les trois critères en un seul chiffre : le **score global**, défini comme leur moyenne :

$$score = \frac{compétitivité + condition + efficacité}{3}$$

!!! example "Question 2.1 — Calcul du score"
    Complétez le tableau ci-dessous en calculant le score global de chaque joueur (arrondi à 2 décimales).

    | Joueur | Compétitivité | Condition | Efficacité | Prix (M€) | Score global |
    |:--:|:--:|:--:|:--:|:--:|:--:|
    | Martinez | 9 | 8 | 9 | 80 | |
    | Kowalski | 7 | 9 | 8 | 45 | |
    | Diallo | 8 | 7 | 7 | 35 | |
    | Fernandez | 6 | 8 | 9 | 55 | |
    | Petrov | 9 | 6 | 8 | 30 | |
    | Okonkwo | 7 | 8 | 7 | 40 | |
    | Larsson | 6 | 9 | 6 | 25 | |
    | Mbeki | 8 | 7 | 8 | 60 | |
    | Reinholt | 5 | 8 | 7 | 20 | |
    | Stavros | 7 | 6 | 6 | 15 | |

??? tips "Correction"
    | Joueur | Score global |
    |:--:|:--:|
    | Martinez | 8.67 |
    | Kowalski | 8.00 |
    | Diallo | 7.33 |
    | Fernandez | 7.67 |
    | Petrov | 7.67 |
    | Okonkwo | 7.33 |
    | Larsson | 7.00 |
    | Mbeki | 7.67 |
    | Reinholt | 6.67 |
    | Stavros | 6.33 |

!!! example "Question 2.2 — Fonction de calcul du score"
    Écrivez une fonction `score_global(t)` qui prend en paramètre le **tuple** associé à un joueur et retourne son score global arrondi à 2 décimales.

    ```python
    # Rappel : mercato["Martinez"] renvoie le tuple (9, 8, 9, 80)
    #                                                 [0] [1] [2] [3]
    ```

??? tips "Correction"
    ```python
    def score_global(t):
        """
        Calcule le score global d'un joueur.
        :param t: tuple (compétitivité, condition, efficacité, prix)
        :return: float, moyenne des 3 critères arrondie à 2 décimales
        """
        return round((t[0] + t[1] + t[2]) / 3, 2)

    # Test
    print(score_global(mercato["Martinez"]))  # → 8.67
    ```

## 3. Conversion en liste de tuples

Pour trier et parcourir les joueurs facilement dans la suite du TP, on va convertir le dictionnaire en une **liste de tuples** de la forme :

```text
(nom,  score_global, prix)
 [0]       [1]        [2]
```

!!! example "Question 3.1 — Construction de la liste"
    En utilisant une compréhension de liste, construisez `liste_joueurs` contenant un tuple `(nom, score, prix)` pour chaque joueur du dictionnaire `mercato`.

    ```python
    # Rappel : mercato.items() renvoie des paires (nom, tuple_stats)
    # Exemple : ("Martinez", (9, 8, 9, 80))
    #            nom          stats
    #                         stats[3] → prix
    ```

??? tips "Correction"
    ```python
    liste_joueurs = [
        (nom, score_global(stats), stats[3])
        for nom, stats in mercato.items()
    ]

    # Résultat :
    # [('Martinez', 8.67, 80), ('Kowalski', 8.0, 45), ('Diallo', 7.33, 35), ...]
    ```

!!! example "Question 3.2 — Tri par score décroissant"
    Triez `liste_joueurs` par **score décroissant** à l'aide de `sorted()`.  
    Affichez le classement (nom + score + prix).

    ```python
    # Chaque élément x de liste_joueurs est un tuple (nom, score, prix)
    #                                                  x[0]  x[1]  x[2]
    # Pour trier sur le score : key=lambda x: x[1]
    ```

??? tips "Correction"
    ```python
    classement = sorted(liste_joueurs, key=lambda x: x[1], reverse=True)

    print("=== Classement par score global ===")
    for i, (nom, score, prix) in enumerate(classement, 1):
        print(f"{i:2}. {nom:10s}  score : {score}  prix : {prix} M€")
    ```

    Résultat :
    ```
     1. Martinez   score : 8.67  prix : 80 M€
     2. Kowalski   score : 8.0   prix : 45 M€
     3. Fernandez  score : 7.67  prix : 55 M€
     4. Petrov     score : 7.67  prix : 30 M€
     5. Mbeki      score : 7.67  prix : 60 M€
     6. Diallo     score : 7.33  prix : 35 M€
     7. Okonkwo    score : 7.33  prix : 40 M€
     8. Larsson    score : 7.0   prix : 25 M€
     9. Reinholt   score : 6.67  prix : 20 M€
    10. Stavros    score : 6.33  prix : 15 M€
    ```

!!! example "Question 3.3 — Sélection naïve (sans contrainte budget)"
    Si le budget n'était pas une contrainte, quels seraient les 5 joueurs sélectionnés ?  
    Quel serait le coût total ? Pourquoi cette solution est-elle **irréalisable** ?

??? tips "Correction"
    Les 5 meilleurs scores : Martinez, Kowalski, Fernandez, Petrov, Mbeki.  
    Coût : 80 + 45 + 55 + 30 + 60 = **270 M€**, soit **120 M€ au-dessus du budget**.  
    Il faut trouver la sélection qui **maximise le score tout en restant sous 150 M€** : c'est exactement le problème du sac à dos.

## 4. Algorithme glouton

### Principe

L'idée gloutonne : trier les joueurs par **rapport qualité/prix** (ratio), puis les recruter dans cet ordre tant que les contraintes sont respectées.

$$ratio = \frac{score}{prix}$$

Plus le ratio est élevé, plus le joueur est « rentable » : bon niveau pour un prix contenu.

!!! example "Question 4.1 — Calcul du ratio"
    Complétez le tableau avec le ratio de chaque joueur (arrondi à 3 décimales).

    | Joueur | Score | Prix (M€) | Ratio |
    |:--:|:--:|:--:|:--:|
    | Martinez | 8.67 | 80 | |
    | Kowalski | 8.00 | 45 | |
    | Diallo | 7.33 | 35 | |
    | Fernandez | 7.67 | 55 | |
    | Petrov | 7.67 | 30 | |
    | Okonkwo | 7.33 | 40 | |
    | Larsson | 7.00 | 25 | |
    | Mbeki | 7.67 | 60 | |
    | Reinholt | 6.67 | 20 | |
    | Stavros | 6.33 | 15 | |

??? tips "Correction"
    | Joueur | Ratio |
    |:--:|:--:|
    | Martinez | 0.108 |
    | Kowalski | 0.178 |
    | Diallo | 0.210 |
    | Fernandez | 0.139 |
    | Petrov | 0.256 |
    | Okonkwo | 0.183 |
    | Larsson | 0.280 |
    | Mbeki | 0.128 |
    | Reinholt | 0.334 |
    | Stavros | 0.422 |

!!! example "Question 4.2 — Pseudo-algorithme"
    Complétez le pseudo-code de l'algorithme glouton :

    ```
    DEBUT
        Calculer le __________ pour chaque joueur
        Trier tous les joueurs par ordre __________ de ce ratio
        budget_depense ← 0
        recrutement ← []
        POUR chaque joueur dans la liste triée :
            SI __________ ET __________ :
                Ajouter le joueur au recrutement
                Ajouter son prix au budget_depense
    FIN
    ```

??? tips "Correction"
    ```
    DEBUT
        Calculer le ratio (score/prix) pour chaque joueur
        Trier tous les joueurs par ordre décroissant de ce ratio
        budget_depense ← 0
        recrutement ← []
        POUR chaque joueur dans la liste triée :
            SI budget_depense + prix <= 150 ET len(recrutement) < 5 :
                Ajouter le joueur au recrutement
                Ajouter son prix au budget_depense
    FIN
    ```

!!! example "Question 4.3 — Implémentation"
    Codez l'algorithme glouton en Python à partir de `liste_joueurs`.  
    Affichez les joueurs recrutés, le score total, le budget dépensé et le budget restant.

    ```python
    # Chaque élément de liste_joueurs est un tuple (nom, score, prix)
    #                                                [0]   [1]   [2]
    # Tri par ratio score/prix : key=lambda x: x[1] / x[2]
    ```

??? tips "Correction"
    ```python linenums='1'
    #  Contraintes 
    BUDGET_MAX  = 150
    MAX_JOUEURS = 5

    #  Étape 1 : tri par ratio score/prix décroissant 
    liste_triee = sorted(liste_joueurs, key=lambda x: x[1] / x[2], reverse=True)

    #  Étape 2 : sélection gloutonne 
    recrutement    = []
    budget_depense = 0
    score_total    = 0

    for nom, score, prix in liste_triee:
        if budget_depense + prix <= BUDGET_MAX and len(recrutement) < MAX_JOUEURS:
            recrutement.append(nom)
            budget_depense += prix
            score_total    += score

    #  Affichage 
    print("=== RÉSULTAT DU MERCATO GLOUTON ===")
    print(f"Joueurs recrutés : {recrutement}")
    print(f"Score total      : {round(score_total, 2)}")
    print(f"Budget dépensé   : {budget_depense} M€")
    print(f"Budget restant   : {BUDGET_MAX - budget_depense} M€")
    ```

    Résultat :
    ```
    === RÉSULTAT DU MERCATO GLOUTON ===
    Joueurs recrutés : ['Stavros', 'Reinholt', 'Larsson', 'Petrov', 'Diallo']
    Score total      : 35.0
    Budget dépensé   : 125 M€
    Budget restant   : 25 M€
    ```

## 5. L'algorithme glouton est-il toujours optimal ?

!!! example "Question 5.1 — Vérification manuelle"
    L'algorithme glouton a sélectionné **Stavros, Reinholt, Larsson, Petrov, Diallo** pour un score de **35.0** et un coût de **125 M€**.

    Testez manuellement la combinaison **Petrov, Diallo, Okonkwo, Larsson, Reinholt** :

    - Calculez le coût total. Le budget est-il respecté ?
    - Calculez le score total. Est-il supérieur à la solution gloutonne ?
    - Que pouvez-vous en conclure ?

??? tips "Correction"
    | Joueur | Score | Prix |
    |:--:|:--:|:--:|
    | Petrov | 7.67 | 30 |
    | Diallo | 7.33 | 35 |
    | Okonkwo | 7.33 | 40 |
    | Larsson | 7.00 | 25 |
    | Reinholt | 6.67 | 20 |
    | **Total** | **36.0** | **150 M€** |

    Budget respecté ✅ — Score **36.0 > 35.0** : cette combinaison est **meilleure** que la solution gloutonne !

    L'algorithme a privilégié Stavros (excellent ratio, mais score faible à 6.33) au détriment d'Okonkwo (ratio légèrement inférieur mais score plus élevé à 7.33) : un choix localement optimal, mais globalement sous-optimal.

    !!! warning "À retenir"
        **Un algorithme glouton ne garantit pas toujours la solution optimale.**

## 6. Résolution par force brute

Pour trouver la **vraie** solution optimale, on teste toutes les combinaisons possibles.

!!! example "Question 6.1 — Nombre de combinaisons"
    Combien y a-t-il de combinaisons à tester pour choisir au plus 5 joueurs parmi 10 ?  
    Rappel : $\mathrm{C}_{n}^{p} = \frac{n!}{(n-p)! \times p!}$

??? tips "Réponse"
    $$\mathrm{C}_{10}^{1} + \mathrm{C}_{10}^{2} + \mathrm{C}_{10}^{3} + \mathrm{C}_{10}^{4} + \mathrm{C}_{10}^{5} = 10 + 45 + 120 + 210 + 252 = \mathbf{637}$$

!!! example "Question 6.2 — Implémentation force brute"
    Complétez le code ci-dessous pour trouver la combinaison optimale.

    ```python linenums='1'
    import itertools

    BUDGET_MAX  = 150
    MAX_JOUEURS = 5

    meilleur_score = 0
    meilleure_comb = []
    meilleur_cout  = 0

    for r in range(1, MAX_JOUEURS + 1):
        for combinaison in itertools.combinations(liste_joueurs, r):
            cout_total  = sum(___ for nom, score, prix in combinaison)
            score_total = sum(___ for nom, score, prix in combinaison)
            if ___ <= BUDGET_MAX and ___ > meilleur_score:
                meilleur_score = ___
                meilleure_comb = [nom for nom, score, prix in combinaison]
                meilleur_cout  = ___

    print("=== RÉSULTAT FORCE BRUTE ===")
    print(f"Joueurs recrutés : {meilleure_comb}")
    print(f"Score total      : {round(meilleur_score, 2)}")
    print(f"Budget dépensé   : {meilleur_cout} M€")
    ```

??? tips "Correction"
    ```python linenums='1'
    import itertools

    BUDGET_MAX  = 150
    MAX_JOUEURS = 5

    meilleur_score = 0
    meilleure_comb = []
    meilleur_cout  = 0

    for r in range(1, MAX_JOUEURS + 1):
        for combinaison in itertools.combinations(liste_joueurs, r):
            cout_total  = sum(prix  for nom, score, prix in combinaison)
            score_total = sum(score for nom, score, prix in combinaison)
            if cout_total <= BUDGET_MAX and score_total > meilleur_score:
                meilleur_score = score_total
                meilleure_comb = [nom for nom, score, prix in combinaison]
                meilleur_cout  = cout_total

    print("=== RÉSULTAT FORCE BRUTE ===")
    print(f"Joueurs recrutés : {meilleure_comb}")
    print(f"Score total      : {round(meilleur_score, 2)}")
    print(f"Budget dépensé   : {meilleur_cout} M€")
    ```

    Résultat :
    ```
    === RÉSULTAT FORCE BRUTE ===
    Joueurs recrutés : ['Petrov', 'Okonkwo', 'Larsson', 'Reinholt', 'Diallo']
    Score total      : 36.0
    Budget dépensé   : 150 M€
    ```
    Ce qui confirme que la solution gloutonne (35.0) **n'était pas optimale**.

## 7. Comparaison et complexité

!!! example "Question 7.1 — Tableau de synthèse"
    Complétez le tableau comparatif :

    | Critère | Force Brute | Algorithme Glouton |
    |:--:|:--:|:--:|
    | Solution trouvée | | |
    | Score total | | |
    | Coût | | |
    | Solution optimale garantie ? | | |
    | Complexité | | |
    | Rapidité d'exécution | | |

??? tips "Correction"
    | Critère | Force Brute | Algorithme Glouton |
    |:--:|:--:|:--:|
    | Solution trouvée | Petrov, Diallo, Okonkwo, Larsson, Reinholt | Stavros, Reinholt, Larsson, Petrov, Diallo |
    | Score total | **36.0** | 35.0 |
    | Coût | 150 M€ | 125 M€ |
    | Solution optimale garantie ? | ✅ Oui | ❌ Non |
    | Complexité | $O(2^n)$ | $O(n \log n)$ |
    | Rapidité d'exécution | Lente (exponentielle) | Très rapide |

!!! example "Question 7.2 — Réflexion"
    Le directeur sportif hésite entre les deux méthodes. Formulez un conseil argumenté : dans quels cas préférer chacune ?

??? tips "Éléments de réponse"
    - **Glouton** : indispensable quand $n$ est grand. Sur une base mondiale de 500 joueurs, la force brute exigerait $2^{500}$ combinaisons — impossible. Le glouton reste quasi-instantané et donne une très bonne solution.
    - **Force brute** : envisageable uniquement pour de petits ensembles ($n \le 20$ environ), quand la précision est critique.
    - En pratique, les problèmes réels utilisent des méthodes plus sophistiquées (programmation dynamique, algorithmes génétiques…) étudiées en Terminale.

## 🏁 Bilan

!!! abstract "Ce qu'il faut retenir"
    - Un **algorithme glouton** fait à chaque étape le meilleur **choix local**, sans revenir en arrière.
    - Il est **rapide** ($O(n \log n)$) mais ne garantit **pas** toujours la solution optimale.
    - La **force brute** garantit l'optimum au prix d'une complexité **exponentielle** ($O(2^n)$), impraticable pour de grands ensembles.
    - Le problème du mercato est une instance du célèbre **problème du sac à dos** (*Knapsack Problem*, NP-complet).

    | | Glouton | Force brute |
    |--|:--:|:--:|
    | Rapidité | ✅ | ❌ |
    | Optimalité garantie | ❌ | ✅ |
    | Passage à l'échelle | ✅ | ❌ |

*Note : FC Numéria est un club fictif créé pour ce TP.*

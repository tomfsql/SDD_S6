# TP7 - Graphes

## Exercice 1 - Notions fondamentales

a) Ce graphe est non-orienté.
b) V = {1;2;3;4;5;6;7;8;9;10}. E = {{2,7},....}. 15
c) Voisins du sommet 2 : {7,5,4}. Degré du sommet 10 : 3
d) Ce graphe est régulier, degré 3 pour chaque sommet.
e) Matrice d'adjacence : 

|     | 1   | 2   |   3 | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
| --- | --- | --- | ---:| --- | --- | --- | --- | --- | --- | --- |
| 1   | 0   | 0   |   1 | 1   | 0   | 0   | 0   | 0   | 0   | 0   |
| 2   | 0   | 0   |   1 | 1   | 1   | 0   | 0   | 0   | 0   | 0   |
| 3   | 0   | 0   |   0 | 0   | 1   | 0   | 0   | 1   | 0   | 0   |
| 4   | 1   | 1   |   0 | 0   | 0   | 0   | 0   | 0   | 1   | 0   |
| 5   | 0   | 1   |   1 | 0   | 0   | 0   | 0   | 0   | 0   | 10  |
| 6   | 1   | 0   |   1 | 1   | 0   | 0   | 0   | 0   | 0   | 0   |
| 7   | 0   | 1   |   0 | 0   | 0   | 1   | 0   | 1   | 0   | 0   | 
| 8   | 0   | 0   |   1 | 0   | 0   | 0   | 1   | 0   | 1   | 0   |
| 9   | 0   | 0   |   0 | 1   | 0   | 0   | 0   | 0   | 1   | 1   |
| 10  | 0   | 0   |   0 | 0   | 1   | 1   | 0   | 0   | 1   | 0   |


f) V = {1;3;5;6;7;8}. E = {{8,7},{1,6},{3,5},{6,7},{3,8},{3,1},{3,5}}.
g) Ce graphe n'est pas planaire car il contient une subdivision de graphe K~3,3~

## Exercice 2 - Gestion d'emploi du temps

a) ![](https://codimd.math.cnrs.fr/uploads/upload_1cf66af7113387b0808bb8d85a305d70.png)

 Graphe non-régulier, planaire.
 
b) On regarde toutes les arêtes avec deux sommets distincts : 
{A,E},{E,B},{E,D},{A,D},{A,C},{C,E},{B,D}

c) Plus grand nombre de points non-reliés : 2

d) Graphe connexe -> oui

e) Nombre de sous-graphes : espagnol, italien, grec ( 3 )

Les deux créneaux restants nécessitent un créneau chacun, il en faudra 3 en tout.

## Exercice 3 - L'enveloppe

a) 
![](https://codimd.math.cnrs.fr/uploads/upload_2389a21a53669b24817c990cce994107.png)

Passer une fois par chaque arête -> eulérien -> tous les sommets pairs ? non, donc impossible

b) DABEGCFH

## Exercice 4 - Isomorphes

![](https://codimd.math.cnrs.fr/uploads/upload_067ee5392f519bbeb2486b9abd386100.png)

Graphe de gauche : ABCDEFGHIA IJCBGFJ
Régulier de degré 3.

Graphe de droite : ABCDEFA AJHICDH

![](https://codimd.math.cnrs.fr/uploads/upload_554fa577cbc5f0e3b7b0dc78460e367c.png)



## Exercice 5 - Réception

Lemme des poignées de main

49 sommets, 11 arêtes par sommet

## Exercice 6 - Une nuit au musée

a) On cherche à couvrir tous les sommets via des arêtes : 
- HF
- AG
- BI
- JE
- CD
- CK

b) On cherche un transversal minimum : 
- C
- J
- E
- F
- A


## Exercice 7 - Problème des cinq salles 

Problème eulérien : les sommets sont-ils tous pairs ? Non ( 1, 2, 4), donc impossible.
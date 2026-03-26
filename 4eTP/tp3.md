# TP4 : Tris

## Exercice 3 : Tri par tiers

### Question 1 : Preuve de correction

Invariant : "le sous-tableau tab[klen:i*len] ( i >= k) contient les éléments initialement aux positions [k:i] et qui sont triés".

Initialisation : le sous tableau tab[0] est trié.
Conservation :

- après une itération, le sous-tableau tab[0:2len/3] est trié
- après deux itérations, tab[2len/3:len] est trié, avec potentiellement tab[len/3:2len/3] qui n'est plus trié, en revanche tab[0:len/3] est toujours trié
- après 3 itérations, tab[0:3len/3] est trié

### Question 2


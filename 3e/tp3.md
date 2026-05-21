# Algo Avancée - TP3

## Exercice 2 - Suite de Fibonacci

```python=
def fibonacci1(k,n) :
    first = 1
    second = 1
    if(k == n):
        return k
    while(k < n):
        second += first
        first = second
        k+=1
```

## Exerice 4

hanoi(n,o,d,i):
if n == 1:
déplacer de o à d
else:
hanoi(n-1,o,i,d)
hanoi(1,o,d,i)
hanoi(n-1,i,d,o)

## Exercice 6

### 1

a) log(2)8=3. f(n) = 1000n² donc O(n²). 3 > 2 donc T(n) = teta(n³)
b) log(2)2 = 1, f(n) = 10n = teta(n^c). c= log(b)a. T(n) = teta(nlog(k+1)n).
c) log(2)2 = 1, f(n) = n² donc omega(n^c) car c > log(b)a. T(n) = teta(f(n))
d) log(3)9 = 2. c = log(b)a donc T(n) = teta(f(n))

### 2

a) Puissance n sur le a
b) Coefficient non-entier sur le b
c) Fonction négative

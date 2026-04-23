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
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

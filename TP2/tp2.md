# TP2 - Structure de données et algorithmique

## Exercice 1

1. Programme 1

    ```python=
    test = 0
    for i in range(n):
        test = test + 1

    for j in range(n):
        test = test - 1
    ```

    1 affectation
    n * (1 affectation + 1 opération)

    n * (1 affectation + 1 opération)

    = 1 + 2n + 2n = 4n+ 1 = O(n) = Θ(n)

2. Programme 2

    ```python=
    test = 0
    for i in range(n):
        for j in range(n):
            test = test + i * j
    ```

    1 affectation + n x n x (3) = 3n² + 1 = O(n²) = Θ(n²)

3. Programme 3

    ```python=
    a=5
    b=6
    c=10
    for i in range(n):
        for j in range(n):
            x = i * i
            y = j * j
            z = i * j
        for k in range(n):
            w = a*k + 45
            v = b*b
    d = 33
    ```

    3 affectations + n x n x (6 opérations) + n x (5 opérations) + 1 affectation = 3 + 6n² + 5n + 1 = O(n²) = Θ(n²)

4. Programme 4

    ```python=
    i = n
    while i > 0:
        k = 2 + 2
        i = i // 2
    ```

    1 affectation + log(n) x ( 4 opérations ) = log(n) + 1 = O(log(n)) = Θ(log(n))

5. Programme 5

```python=
sum = 0
for i from 1 to n*n:
   for j from 1 to i:
      for k from 1 to 6:
          sum = sum + 1;
```

1 affectation + n² x (1+2+3+....+n²) x 6 x 2
1 affectation + n² x ((n²(n²+1)/2)) x 6 x 2
1 affectation + n² x ((n⁴ + n²)/2) x 6 x 2

1 affectation + n⁶ x n² x 6 x 2 = O(n⁴) = Θ(n⁴)

## Exercice 2

Ordre croissant : 6,(3/2)^n, lg(lg(n)), lg(n) lg(n²), sqrt(n), n, n(lg(n)), n³, (n-n²+5n³), n³+lg(n), 2^n-1^, 2^n^

## Exercice 3

Par ordre : log(10⁶) = 6, 10⁶, 10^12^, 2^10^6^^
Donc 6, 1, 10^-6^, encore moins

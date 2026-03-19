import time
memo = {0:1, 1:1}

def fibonacci1(k,n, first, second) :
    if(n < 0):
        return 0
    prev = first
    fibo = second
    if(k == n):
        print("output : ",fibo)
        return fibo
    else :
        newfibo = prev + fibo
        prev = fibo
        fibo = newfibo
        k+=1
        fibonacci1(k,n, prev, fibo)

def fibonacci2(k,n, first, second) :
    if(n < 0):
        return 0
    if n in memo:
        return memo[n]
    prev = first
    fibo = second
    if(k == n):
        print("output : ",fibo)
        return fibo
    else :
        newfibo = prev + fibo
        prev = fibo
        fibo = newfibo
        memo[k] = fibo
        k+=1
        fibonacci2(k,n, prev, fibo)


start = time.time()
fibonacci1(1,50,1,1)
end = time.time()
print(f"Temps d'exécution : {end - start:.6f} secondes")

from math import sqrt
import time

def prime(n):
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

start_time = time.time()
prime(35831403792388187)
end_time = time.time()
print(f"Temps d'exécution : {end_time - start_time:.6f} secondes")

""" Mesurer le temps d’exécution du programme précédent sur les nombres 4337894221, 118922974492981,
7138449485398663, 35831403792388187, 621467444825020319 et 8939187427700486623). """
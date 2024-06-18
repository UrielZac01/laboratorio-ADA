#Algoritmo de Monte Carlo para estimar el valor de π (Pi)

import random

def estimate_pi(num_samples):
    inside_circle = 0
    
    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        if x**2 + y**2 <= 1:
            inside_circle += 1
    
    return (inside_circle / num_samples) * 4

# Ejemplo de uso
num_samples = 100000
pi_estimate = estimate_pi(num_samples)
print(f"Estimación de π usando {num_samples} muestras: {pi_estimate}")



#Quicksort Aleatorizado

import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]
        less_than_pivot = [x for x in arr if x < pivot]
        equal_to_pivot = [x for x in arr if x == pivot]
        greater_than_pivot = [x for x in arr if x > pivot]
        
        return randomized_quicksort(less_than_pivot) + equal_to_pivot + randomized_quicksort(greater_than_pivot)

# Ejemplo de uso
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = randomized_quicksort(arr)
print(f"Array ordenado: {sorted_arr}")

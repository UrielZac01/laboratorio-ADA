#Solucion para valores distintos
def find_magic_index_distinct(arr):
    def binary_search(arr, left, right):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            return binary_search(arr, left, mid - 1)
        else:
            return binary_search(arr, mid + 1, right)
    
    return binary_search(arr, 0, len(arr) - 1)

# Ejemplo de uso
arr = [10, 5,2, 4, 3]
print(find_magic_index_distinct(arr))  # Salida: 2, arr[2]=2


#Solucion para valores NO distintos
def find_magic_index_non_distinct(arr):
    def binary_search(arr, left, right):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        mid_value = arr[mid]
        
        if mid == mid_value:
            return mid
        
        # Buscar en la mitad izquierda
        left_index = min(mid - 1, mid_value)
        left_result = binary_search(arr, left, left_index)
        if left_result != -1:
            return left_result
        
        # Buscar en la mitad derecha
        right_index = max(mid + 1, mid_value)
        return binary_search(arr, right_index, right)
    
    return binary_search(arr, 0, len(arr) - 1)

# Ejemplo de uso
arr = [1, 8, 2, 2, 2, 3, 4, 7, 9, 12, 13]
print(find_magic_index_non_distinct(arr))  # Salida: 7 ya que arr[7]=7

# Nama: Monica Oktaviona
# NPM: 2106701210
# Kode Asdos: 4
# Kelas: C
# Desain dan Analisis Algoritma
# Semester Ganjil 2023/2024
# Referensi: https://www.geeksforgeeks.org/heap-sort/

def heapify(arr, n, root_idx):
    """
    Fungsi untuk melakukan reorganizing pada max heap agar
    elemen terbesar berada di root dan setiap node memenuhi 
    max heap property
    """
    largest_idx = root_idx
    left_child_idx = 2 * root_idx + 1
    right_child_idx = 2 * root_idx + 2

    if (left_child_idx < n) and (arr[largest_idx] < arr[left_child_idx]):
        largest_idx = left_child_idx

    if (right_child_idx < n) and (arr[largest_idx] < arr[right_child_idx]):
        largest_idx = right_child_idx

    if largest_idx != root_idx:
        arr[root_idx], arr[largest_idx] = arr[largest_idx], arr[root_idx]
        heapify(arr, n, largest_idx)

def heapsort(arr):
    """
    Fungsi untuk melakukan sorting pada array
    """
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    

    
   
                

    


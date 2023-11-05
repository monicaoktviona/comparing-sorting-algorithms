# Nama: Monica Oktaviona
# NPM: 2106701210
# Kode Asdos: 4
# Kelas: C
# Desain dan Analisis Algoritma
# Semester Ganjil 2023/2024

"""
Referensi: Michael T Goodrich. 
Randomized Shellsort: A Simple Data-Oblivious Sorting Algorithm. 
Journal of the ACM (JACM), 58(6):1–26, 2011.
"""

import random

C = 4

def exchange (arr, i, j):
    """
    Fungsi untuk melakukan swap elemen array pada index ke-i dan j
    """
    arr[i], arr[j] = arr[j], arr[i]

def compare_exchange(arr, i, j):
    """
    Fungsi untuk membandingkan elemen pada index ke-i dan j. Jika belum terurut, 
    maka akan dilakukan swap dengan memanggil fingsi exchange. """
    if(((i < j) and (arr[i] > arr[j])) or ((i>j) and (arr[i] < arr[j]))):
        exchange(arr, i, j)
    
def permute_random(arr):
    """
    Fungsi untuk melakukan shuffling elemen pada index ke-i dengan elemen random pada array
    """
    for i in range(0, len(arr)):
        exchange(arr, i, random.randint(i, len(arr) - 1))

def compare_regions(arr, s, t, offset):
    """
    Fungsi untuk melakukan compare exchange pada elemen dalam dua region berbeda
    """
    mate = list(range(offset))
    for _ in range(0, C):
        for i in range(0, offset):
            mate[i] = i
        permute_random(mate)
        for i in range(0, offset):
            compare_exchange(arr, (s + i), (t + mate[i]))

def randomized_shellsort(arr):
    """
    Fungsi untuk melakukan randomized Shellsort sorting 
    pada array dengan panjang kelipatan 2
    """
    n = len(arr)
    offset = n // 2

    while offset > 0:
        i = 0
        while(i < n - offset):
            compare_regions(arr, i, i + offset, offset)
            i += offset

        i = n - offset
        while(i >= offset):
            compare_regions(arr, i - offset, i, offset)
            i -= offset

        i = 0
        while(i < n - 3 * offset):
            compare_regions(arr, i, i + 3 * offset, offset)
            i += offset

        i = 0
        while(i < n - 2 * offset):
            compare_regions(arr, i, i + 2 * offset, offset)
            i += offset

        i = 0
        while(i < n):
            compare_regions(arr, i, i + offset, offset)
            i += 2 * offset

        i = offset
        while(i < n - offset):
            compare_regions(arr, i, i + offset, offset)
            i += 2 * offset

        offset = offset // 2

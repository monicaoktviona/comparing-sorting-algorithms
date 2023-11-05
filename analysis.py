# Nama: Monica Oktaviona
# NPM: 2106701210
# Kode Asdos: 4
# Kelas: C
# Desain dan Analisis Algoritma
# Semester Ganjil 2023/2024

import time
import os
import tracemalloc
import max_heap_sort
import randomized_shellsort

def sort(sorting_name, sorting_algorithm, arr):
    """
    Fungsi untuk melakukan sorting sesuai dengan algoritma yang diinput
    serta melakukan perhitungan waktu dan memory yang digunakan untuk sorting
    """    
    print(f"{sorting_name}")
    tracemalloc.reset_peak()
    start_time = time.time()
    sorting_algorithm(arr)
    end_time = time.time()
    print(f"Time taken: {(end_time-start_time)/1000:.10f} ms")
    print(f"Memory used (peak): {tracemalloc.get_traced_memory()[1]}")
    
if __name__ == "__main__":
    dataset_path = "./dataset/"
    tracemalloc.start()
    for dataset in os.scandir(dataset_path):
        with open(dataset, "r") as current_dataset:
            arr = [int(x) for x in current_dataset]
            print("=================================================")
            print(f"File: {dataset.name}")
            print(f"Numbers to sort: {len(arr)}")
            print("=================================================")
            sort("Max Heap", max_heap_sort.heapsort, arr)
            print("-------------------------------------------------")
            sort("Randomized Shellsort", randomized_shellsort.randomized_shellsort, arr)
            print("=================================================")
            print()
    tracemalloc.stop()
    


# Nama: Monica Oktaviona
# NPM: 2106701210
# Kode Asdos: 4
# Kelas: C
# Desain dan Analisis Algoritma
# Semester Ganjil 2023/2024

import random
import os.path

def generate_random(num):
    """
    Fungsi untuk men-generate dataset secara random sebanyak num
    dan menyimpannya dalam file .txt
    """
    file_path = os.path.join("./dataset/", "random_" + str(num) + ".txt")         
    file = open(file_path, "a")
    for i in range(0, num):
        file.write(str(random.randint(1, 2**20)))
        if i != (num - 1):
            file.write("\n")
    file.close()
    print(str(num) + " random numbers succesfully generated.")
    

def generate_sorted(num):
    """
    Fungsi untuk men-generate dataset secara sorted sebanyak num
    dan menyimpannya dalam file .txt
    """
    file_path = os.path.join("./dataset/", "sorted_" + str(num) + ".txt")         
    file = open(file_path, "a")
    numbers = []

    for i in range(0, num):
        numbers.append(random.randint(1, 2**20))

    numbers.sort()

    for i in range(0, len(numbers)):
        file.write(str(numbers[i]))
        if i != (len(numbers) - 1):
            file.write("\n")
    file.close()
    print(str(num) + " sorted numbers succesfully generated.")

def generate_reversed(num):
    """
    Fungsi untuk men-generate dataset secara reversed sebanyak num
    dan menyimpannya dalam file .txt
    """
    file_path = os.path.join("./dataset/", "reversed_" + str(num) + ".txt")         
    file = open(file_path, "a")
    numbers = []

    for i in range(0, num):
        numbers.append(random.randint(1, 2**20))

    numbers.sort(reverse=True)

    for i in range(0, len(numbers)):
        file.write(str(numbers[i]))
        if i != (len(numbers) - 1):
            file.write("\n")
    file.close()
    print(str(num) + " reversed numbers succesfully generated.")

if __name__ == '__main__':
    size = [2**9, 2**13, 2**16]     # list of size dari dataset yang ingin digenerate

    for i in range(0, len(size)):
        generate_random(size[i])
        generate_sorted(size[i])
        generate_reversed(size[i])
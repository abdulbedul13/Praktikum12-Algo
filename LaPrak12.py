# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 23:47:25 2021

@author: Abdullah
"""

# ELEMEN KOMPETENSI 1
while True:
    print("LINEAR SEARCH")
    jumlah = int(input("Masukkan Jumlah Angka Pada List: "))
    elkom1 = []
    for i in range(jumlah):
        elkom1.append(int(input("Angka Ke-{}: ".format(i + 1))))
    print("\nList Angka -> ", elkom1)


    def linear_search(elkom1, cari):
        for i in range(len(elkom1)):
            if elkom1[i] == cari:
                return "Ditemukan\n"
        return "Tidak Ditemukan\n"


    cari = int(input("Masukkan angka yang dicari: "))
    print("Hasil Linear Search -> " + str(linear_search(elkom1, cari)))

# ELEMEN KOMPETENSI 2
while True:
    print("BINARY SEARCH")
    jumlah = int(input("Masukkan Jumlah Angka Pada List: "))
    elkom2 = []
    for i in range(jumlah):
        elkom2.append(int(input("Angka Ke-{}: ".format(i + 1))))
    print("\nList Angka -> ", elkom2)


    def binary_search(elkom2, x, kiri, kanan):
        if kanan >= kiri:
            tengah = kiri + (kanan - kiri) // 2
            if elkom2[tengah] == x:
                return tengah
            elif elkom2[tengah] > x:
                return binary_search(elkom2, x, kiri, tengah - 1)
            else:
                return binary_search(elkom2, x, tengah + 1, kanan)
        else:
            return False


    cari = int(input("Masukkan angka yang dicari: "))

    hasil = binary_search(elkom2, cari, 0, len(elkom2) - 1)

    if hasil:
        print("Ditemukan di indeks: {}\n".format(str(hasil)))
    else:
        print("Tidak ditemukan\n")

# ELEMEN KOMPETENSI 3
print("BUBBLE SORT")
jumlah = int(input("Masukkan Jumlah Angka Pada List: "))
elkom3 = []
for i in range(jumlah):
    elkom3.append(int(input("Angka Ke-{}: ".format(i + 1))))
print("\nList Angka -> ", elkom3)


def bubble_sort(elkom3):
    for i in range(0, len(elkom3) - 1):
        for j in range(len(elkom3) - 1):
            if (elkom3[j] > elkom3[j + 1]):
                temp = elkom3[j]
                elkom3[j] = elkom3[j + 1]
                elkom3[j + 1] = temp
    return elkom3


print("Hasil Bubble Sort -> " + str(bubble_sort(elkom3)))

# ELEMEN KOMPETENSI 4
print("SELECTION SORT")
jumlah = int(input("Masukkan Jumlah Angka Pada List: "))
elkom4 = []
for i in range(jumlah):
    elkom4.append(int(input("Angka Ke-{}: ".format(i + 1))))
print("\nList Angka -> ", elkom4)

def selection_sort(elkom4, panjang):
    for step in range(panjang):
        indeks_awal = step
        for i in range(step + 1, panjang):
            if elkom4[i] < elkom4[indeks_awal]:
                indeks_awal = i
        (elkom4[step], elkom4[indeks_awal]) = (elkom4[indeks_awal], elkom4[step])
    return elkom4

print("Hasil Selection Sort -> " + str(selection_sort(elkom4, jumlah)))

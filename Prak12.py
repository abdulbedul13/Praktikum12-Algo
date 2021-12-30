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


    dicari = int(input("Masukkan angka yang dicari: "))
    print("Hasil Linear Search -> " + str(linear_search(elkom1, dicari)))

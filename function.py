#Function
#Variabel adalah tempat menyimpan value (integer, string, float, list dsb) yang bisa diberi nama dan bisa dipakai
#function adalah tempat menyimpan code yang diberi nama dan bisa dipakai lagi

#CONTOH FUNCTION DENGAN PARAMETER
# def segitiga(jumlah_bintang) : # def Nama_Function(parameter), Parameter = hal paa yang perlu diinput oleh user

#     teks = ''
#     for i in range(0,jumlah_bintang):
#         for j in range(0,i+1): 
#             teks +=(' * ')
#         teks += '\n'
#     print(teks)

# segitiga(6) #menggunakan function

#CONTOH FUNCTION TANPA PARAMETER

# def hallo():
#      print("halo teman2")

# hallo() #menggunakan function

#CONTOH FUNCTION PENGALI

# def kalikan (a,b) : #function dengan nama "kalikan" dan parameter a & B
#     print(a * b)

# kalikan(3,5)   

#CONTOH FUNCTION DENGAN PARAMATER
# def nama_lengkap(nama) :
#     print (nama + " Slamet")
# nama_lengkap('Andi')
# nama_lengkap('Budi')

#RETURN FUNCTION

# def total(x,y):
#     z = x + y
#     return z # z jika tidak kita return maka hasilnya akan "NONE"

# print(total (4,5))
#print(z) #z tidak bisa diprint karena z variable lokal. maksudnya z adalah variable yang hanya ada dlm function

#====================================
# UPDATE PEMBELAJARAN

# DATA TYPES
# NUMBER : INTEGER, FLOAT => PENGOLAHANNYA MENGGUNAKAN OPERASI MATEMATIKA SAJA
# STRING
# LIST
# DICTIONARY, SET, TUPLE

# TOOLS :
# 1. IF ELSE (CONDITION)
# 2. LOOPING (PENGULANGAN)
# 3. FUNCTION (PENYIMPANAN CODE)

#======================================
# LIST = VARIABEL YANG BERISI BANYAK VALUE

# nama = 'andi'
# umur = 34
# domisili = 'bogor'

# #contoh List 
# identitas = ['andi', 34, 'bogor']

buah = ['nanas', 'apel', 'jeruk', 'mangga', 'alpukat']

#1. INDEX

#index_mangga = buah.index('mangga')
#print(index_mangga)

#2. APPEND (menambah komponen list)

# buah.append('salak') #menambah komponen salak
# buah.append('sawo') #menambah komponen sawo
# buah.append(['durian', 'rambutan']) #menambhan list dalam list
print(buah)
# print(buah.index(['durian', 'rambutan']))

#3. INSERT (menambah komponen list di posisi tertentu)

# buah.insert(0, 'pisang') #menambah komponen pisang di index ke 0
# print(buah)

#4. EXTEND (menambah komponen list sehingga melebur menjadi anggota list baru)
# buah.extend (['leci', 'manggis'])
# print(buah)

#5. SLICING (mengakses Komponen dalam list)
# print(buah[1]) #nanas
# print (buah[0]) #pisang ada di index ke -0
# print (buah[8] [0]) #durian ada di index ke 8 (berupa list) dan durian di index ke 0
# print (buah [8] [1])
# print (buah [9])
# print (buah [-1]) #tampilkan pertama dari belakang
# print (buah[::-1]) #tampilkan semua dengan stepnya satu per satu dari belakang

#6. Remove (menghapus komponen list yang spesifik) by nama
# buah.remove('pisang') #menghapus pisang dalam list 
# print (buah)

#7. POP (menghapus) # by index
# buah.pop(0)
# print(buah)

#8. REVERSE (membalikan urutan index)
#buah.reverse()
#print(buah)
#print(buah[::-1]) #sama aja

#9. Sort (mengurutkan)
# print(buah)
# buah.sort()
# print(buah)

#10. Copy (mengcopy list)
# fruit = buah.copy()
# print(fruit)

# x = [40,100,1,5,25,10]

# i = 0
#print(x[i])

# for j in range (0,6) :
#     if x[i] < x[0+i] :
#         print(x[0+i])
#         i += 1
#         print(i)
#     else:
#        print('halo')

import math
umur = [3, 50, 12, 34, 47, 87, 19, 37, 55, 3, 28]

# def rata2 (dataAnda) :
#     total = sum(dataAnda)
#     n = len(dataAnda)

#     hasil = total / n
#     print (hasil)

# rata2(umur)

# def median (dataAnda) :
    
#     data = dataAnda.sort()
#     n = len(dataAnda)

#     if n % 2 == 1 :

#         median = n//2 # pembulatan 2
#         print (dataAnda[median])

#     else:
        
#         median1 = dataAnda [n//2]
#         median2 = dataAnda [n//2-1]
#         totalMedian = (median1 + median2) /2
#         print (totalMedian)

# median(umur)

#print(umur.sort())
# def mean(x) :
#     total = sum(x)
#     n = len(x)
#     hasil = total /n
#     print(hasil)

# # def median(x) :
# #      x.sort()
# #      n = len(x)
# #      a = math.ceil(n/2)
# #      hasil = x[a]
# #      print(hasil)

# def median(dataAnda) :
#     m = len(dataAnda)
#     dataAnda.sort()
    
#     if m % 2 == 0 :
#         median1 = dataAnda[m//2]
#         median2 = dataAnda[m//2-1]
#         median = (median1+median2) / 2
#     else :
#         median = umur[m//2]
#         print(median)
#     return median
#     #return dataAnda


# mean(umur)

# median(umur)

# #print(median(dataAnda))


# def modus(data) :
#     modus1 = 0
#     data.sort()
#     panjang = len(data)
#     for i in range (0,panjang) :
#         for j in range (i+1, panjang) :
#             if data[i] == data[j] :
#               #print("lebih kecil")
#               modus1 += 1
#               #print (f'modus terbanyak adalah : {data[modus1]}')
#             # else    
#             #     print("sama saja")
        
#             #print (data[i])
#             #print (data[j])

#     print(f'modus terbanyak adalah : {data[modus1]}')

# modus(umur)
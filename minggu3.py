# Function = kumpulan / simpanan code yang diberi nama dan dipanggil lagi
# function tanpa nama dan sekali pakai (lambda function)

#============================

# String = data types yang memiliki tanda " " atau ''

#teks = "Learn From Home"

# 1. UPPER : mengubah semua karakter menjadi huruf kapital
#print(teks.upper())

# 2. LOWER
#print(teks.lower())

# 3. CAPITALIZE : mengubah karakter awal menjadi huruf kapital, lalu selanjutnya huruf kecil
#print(teks.capitalize())

# 4. JOIN # Menggabungkan karakter ke dalam string
# hasilnya : L-e-a-r-n- -F-r-o-m- -H-o-m-e spasi dianggap sbg karakter
# strip = '-'
# new_teks = strip.join(teks)
# grup = ['Andi' , 'Budi', 'Caca']
# koma = '-'
# print(new_teks)
# print (koma.join(grup)) 
#hasilnya : Andi-Budi-Caca

# 5. REPLACE : Mengganti Karakter dalam string
# print(teks.replace('Learn From Home', 'Belajar dari rumah'))
# newTeks = 'Belajar dari rumah'
# print(teks.replace(teks,newTeks))
# print(teks.replace('From', '')) 
# hasilnya : Learn  Home ==> kata From diganti jadi string kosong.

#6. SPLIT : memisahkan karakter dalam string berdasarkan karakter tertentu 
          #sehingga berubah menjadi list
# print(teks.split(' ')) #dipisah berdasarkan spasi
# hasil = teks.split(' ')
# print(type(hasil)) # mengecek data types
# print(teks.split('a'))

#7. Count : Menghitung jumlah karakter
# print(teks.count('a'))
# print(teks.count('o'))


#=======================================
# LATIHAN

# teks = 'Belajar data science di Purwadhika'

# #1. Buat function seperti count yang bisa menghitung jumlah suatu huruf atau karakter
# #hitung_huruf ('a')

# def hitung (karakter, kata) :
#     panjang = len(kata)
#     hitung = 0 #variabel lokal

#     for i in range (0, panjang) :
#             if kata[i] == karakter :
#                hitung += 1
#     return (f'jumlah huruf {karakter} dalam kata tersebut = {hitung}')

# print(hitung('a',teks))

# ALTERNATIF JAWABAN

# def hitung_kata(yourText) :
#     kata = yourText.split(' ')
#     print(len(kata))

# #hitung_kata(teks) 

#2. Buat fuction untuk menghitung jumlah kata dalam string
#hitung_kata()

# def hitung_kata (kata) :
#     panjang = len(kata)
#     #print(panjang)
#     hitung = 1
#     for i in range (0, panjang) :
#         if kata[i] == " " :
#             hitung += 1
#         #print(kata[i])

#     print(f'Jumlah kata dalam teks adalah = {hitung}')

# hitung_kata(teks)

# def hitung_kata(teks):
#     kata = teks.split(' ')
#     print(len(kata))
# hitung_kata(teks)

# #3. Buat function untuk membalikan urutan kata dalam string
# #"Purwadhika di Science Data Belajar"

# def balik_kata (yourText) :
#     spasi = ' '
#     listKata = yourText.split(' ')
#     newListKata = listKata[::-1]
#     newTeks = spasi.join(newListKata)
#     return newTeks
# print(balik_kata(teks))


#====================================

#FUNCTION = kumpulan / simpanan code yang diberi nama dan bisa dipanggil lagi
# FUNCTION TANPA NAMA dan SEKALI PAKAI (LAMBDA FUNCTION)

#gaji = [1,2,3,4,5,6,7,8,9,10,15,20] #list gaji

# dengan function normal/biasa

# def pajak (yourList) :
#     return yourList * 0.1

# #Menjalankan function di dalam variabel
# list_pajak = list(map(pajak, gaji))#membuat_list (menjalankan function (pajak) pada data(gaji))
# print(list_pajak)

# map adalah sebuah perintah untuk menjalankan function di dlm tanda kurung kiri, ke tanda kurung kanan
#dengan function tanpa nama & sekali pakai (lambda function)
# list_pajak_lambda = list(map(lambda yourList: yourList * 0.1, gaji))
# print(list_pajak_lambda)

#gaji_Kotor = [1,2,3,4,5,6,7,8,9,10,15,20] # list gaji

# def hitGajiBersih(yourList):
#     pajak =  yourList *0.1
#     return yourList - yourList * 0.1
    
# list_gajiBersih = list(map(hitGajiBersih, gaji))
# print(list_gajiBersih)

# #Lambda Function
# list_gajiBersih_lambda = list(map(lambda yourList: yourList - (yourList * 0.1), gaji))
# print(list_gajiBersih_lambda)

#LAMBDA
# PLUS = Praktis, Efisien hanya satu baris 
# MINUS = Hanya bisa memuat code yang sederhana, hanya sekali pakai

#FUNCTION 
# PLUS = BISA MEMUAT CODE YANG LEBIH KOMPLEKS, bisa dipakai beberapa kali
# MINUS = AGAK BOROS BARIS CODE

#=============================
# Penggunaan looping dalam list (list comprehension)

# gaji = [1,2,3,4,5,6,7,8,9,10,15,20]

# list_pajak = [item * 0.1 for item in gaji]
# list_gaji_bersih = [item - (item*0.1) for item in gaji ]
# print (list_pajak)
# print (list_gaji_bersih)

# Penggunaan function dan looping dalam list (list comprehension)

#gaji = [1,2,3,4,5,6,7,8,9,10,15,20]

# def pajak(yourList) :
#     return yourList * 0.1

# # membuat variabel = [ekseskusi function(item)], looping ]
# list_pajak = [pajak(item) for item in gaji]    
# print(list_pajak)

#DATA Types
# 1. INTEGER dan FLOAT Sudah dipelajari
# 2. List sudah dipelajari
# 3. String Sudah dipelajari
# 4. DICTIONARY, TUPLE, SET

#DICTIONARY
# VARIABEL = tempat menyimpan value
# Var. List = tempat menyimpan beberapa value dan memiliki index = 0,1,2,3
# Var. String = tempat menyimpan karakter ('....') dan memiliki index = 0,1,2,3,4
# Var Dictonary = tempat menyimpan beberapa value dan memiliki index unik /custom

#DICTIONARY
# buah = {'kotak1' : 'mangga', 'key2' : 'nanas', 'kotak3' : 'apel', 'kotak4' : ['sawo',10000]}

# print(type(buah))
# print(buah['kotak1'])
# print(buah['key2'])
# print(buah['kotak3'])
# print(buah['kotak4'] [1])

#1. GET : Mendapatkan value pada index / key tertentu
# print(buah.get('kotak1'))
# print(buah.get('kotak4'))
# print(buah['kotak4'])

#identitas = {'nama' : 'Andi', 'usia' : 26, 'kewarganegaraan' : 'Indonesia', 'gaji' : 20000000}
# print(identitas)

# #menambahakan key & value
# data_tambahan = identitas.get('gol.darah','AB+')
# print(data_tambahan)

# #2.keys # menampilkan keys/kunci/index nya saja
# print(identitas.keys())

# #3. Values : # menampilkan values / isi dari key-nya
# print(identitas.values())

#4. Update Menambahkan isi dari dictionary
# new_data = {'gol.darah' : 'B-'}
# identitas.update(new_data)
# print(identitas)

#5. ITEMS : menampilkan keseluruhan keys dan value
# print (identitas.items())
# print (list(identitas.items()))

# x = list(identitas.items())
# print(list(x[0]))

#6. POP ITEM : menghapus item tertentu dari belakang
# identitas.popitem()
# print(identitas)

# #7. POP : menghapus item berdasarkan key tertentu
# identitas.pop ('nama')
# print(identitas)

#====================================

# LATIHAN
#UBAH LIST KE DALAM DICTIONARY

#UBAH ke dalam dictrionary
data = ['Andi', 23, 'Budi', 30, 'Dedi', 41]

umur = { data[i] : data[i+1] for i in range (0, len(data), 2)}

data_baru = {data[i+1] : data[i] for i in range (0, len(data),2)}

print(umur)
print(data_baru)

#===========================================================

#LATIHAN 
#Buat Dictionary dengan keys (karyawan), value (gaji)
# nama = ['Ferdian', 'Giring', 'Hedi', 'Imam']
# gaji = [20,35,12,17]

# karyawan = {nama[i] : gaji[i] for i in range (0, len(nama))}
# dict_db = {f'{i+1} {nama[i]}' : f'Rp {gaji[i]} Juta' for i in range (0, len(nama))}

# print (dict_db)


#==========================================================
# DATA TYPE  TUPLE = Sama seperti list tapi sudah tidak bisa diedit

# gaji = [1,2,3,4,5]
# gaji[2] = 30 # mengubah gaji di index ke -2 mjd 30
# print (gaji)

#salary = (1,2,3,4,5)
#print(salary[2])
#salary[2] = 30
#print (salary)

#Bagaimana mengedit Tuple?
# salary = (1,2,3,4,5)
# new_salary = list(salary)
# new_salary[2] = 30 # mengganti anggota indeks ke 2 menjadi 30
# salary = tuple(new_salary)
# print (tuple(salary))

#==============================================
# DATA TYPE : SET = sama seperti list, tapi data yg double tidak dianggap

#beda dengan list, smua dianggap ada

# gaji = [1,2,2,3,3,3,4,5,5,5]
# print (gaji)

# #set tidak menampilkan data double
# salary = {1,2,2,3,3,3,4,5,5,5}
# print (salary)
# print(len(salary)) #ada double tidak dianggap

# gaji = [1,2,2,3,3,3,4,5,5,5,4,5,3,3,4,5,2]
# gaji_unik = set(gaji)
# print(gaji_unik)

#TUGAS
nama = ['Andi', 'Budi', 'Caca']
usia = [30,40,50]
gaji = [8,9,10]




karyawan = (nama[0], usia[0], gaji[0])

# identitas = {'karyawan ke -1' : ['Andi', 30, 8], 'karyawan ke -2 ' : ['Budi', 40, 9]}


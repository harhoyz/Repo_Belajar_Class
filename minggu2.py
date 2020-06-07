#Looping
#Algoritma pengulangan supaya code kita lebih efisien dalam menjalankan perintah yang berulang

#Contoh code yang tidak efisien (speed, memory, maintainance)
#print("Halo")
#print("Halo")
#print("Halo")
#print("Halo")
#print("Halo")

# Jenis Looping
# 1. While Loop
# 2. For Loop

#1. While Loop
# angka = 1 # angka awal adalah 1
# while angka <6 : #selama angka kurang dari 6, maka jalankan perintah di bawah
#     print (f"halo ke - {angka}") #tampil halo
#     angka +=1 #angka setiap putaran di tambahkan 1

#2. For Loop
#belajar membuat list
# contoh_list = [1, 2, 3, 4, 5]
# contoh_list2 = ['a', 'b', 'c', 4, 5]
# print(contoh_list)
# print(contoh_list2)

# list_item = list (range(1,11,2)) #membuat list 1 sampai 11 dengan step 2

# print(list_item)

#Belajar Menggunakan For Loop

# list_item = list (range(1,11,2)) #membuat list 1 sampai 11 dengan step 2
# print (list_item)

# for item in range(1,11,2) :
#     print(item)

# for i in range (1,6) :
#     print("halo")

# for item in range (0,5) : #pengulangan 0 sampai 5 : 0,1,2,3,4
#     print ("halo")

# for i in range (5) :
#     print("halo")

# for pengulangan in range (0,5): # pengulangan perintah sebanyak range 0 sampai 5 : 0, 1, 2, 3, 4 (lima kali)
#     print(f'Pengulangan ke - {pengulangan}')
#     print("halo")

# for i in range (1,11) :
#      print (f'Nomor urut ke - {i}')

# j=1
# while j < 11 :
#     print (f'nomor urut ke -{j}')
#     j +=1

# for i in range (0,21,2) :
#   print (f'Nomor urut ke - {i}')

# j=0
# while j < 21 :
#     print (f'nomor urut ke - {j}')
#     j +=2

#LOOP DRAWING

#teks = ''

# for i in range (0,5) :
#     teks += ' * '
#     #print (teks)
# print (teks)

# teks2 = ''
# for i in range (0,5) :
#     teks += ' * \n' # \n itu untuk enter
# print(teks2)

# teks = '' #variabel dengan nama teks yang isisnya string

# for item in range (0,5) : #pengulangan perintah sebanyak jumlah item di range 0 -5 # perintah looping AWAL
#     for item in range (0,5) : #pengulangan perintah sebanyak jumlah item di range 0 -5 # perintah looping AKHIR
#         teks +=' *' # perintah A
#     teks += '\n'   # perintah B
# print (teks) 


# teks = ""

# for item in range (0,5) :
#     teks += ' * '
#     print (teks)
  
teks = ''
for i in range(0,5):
    for j in range(0,i+1): 
        teks +=(' * ')
    teks += '\n'
print(teks)

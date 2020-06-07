# ini coding pertama

# print('hello world')
# print('hello world')

#variabel
#variabel adalah nilai yang kita isi apapun

#nama_saya = 'Andi'
#list_nama = ['andi', 'budi', 'caca']

#print(nama_saya)
#print(list_nama)

#jika ada 2 variabel dgn nama sama, maka variabel terakhir yang muncul
# umur = 32
# umur = 22
# umur = 14

#print(umur)

#data types in phyton
# 1. integer : 1, 2, 3, 1000
# 2. float : 1.5   2.7
# 3. string : 'andi', "caca"
# 4. list : [1, 2, "Andi"]
# 5. Dictionary : {'nama' : 'Andi', 'umur' : 22, 'profesi' : 'guru'}
# 6. Boolean : True or False

#variabel dengan isi value Boolean. Huruf T nya harus besar
# jomblo = True
# print(jomblo)

#Cara Mengecek data type

# nama = "Andi"
# umur = 22
# tinggi = 168.5
# jomblo = False

# print(type(nama))
# print(type(umur))
# print(type(tinggi))
# print(type(jomblo))

# nama = input('berapa umur anda?')
# print (nama)

#Latian PERTAMA
# nama = input('nama kamu?')
# umur = input('umur kamu?')
# kelamin = input('jenis kelamin kamu?')
# pekerjaan = input('pekerjaan kamu?')
# print('Nama :' + nama)
# print('Umur :' + umur)
# print('Kelamin :' + kelamin)
# print ('Pekerjaan :' + pekerjaan)

#Latian numbers dan aritmathica

# usiaAndi = 40;
# usiaBudi = 20;

# # print (usiaAndi * usiaBudi)
# # print (usiaAndi / usiaBudi)
# # print (usiaAndi + usiaBudi)
# # print (usiaAndi - usiaBudi)
# print (usiaAndi % 3)
# print (usiaBudi ** 2 ) #** artinya pangkat

# usiaAndi += 5
# #usiaAndi = usiaAndi +5
# usiaBudi -= 10
# #usiaBudi = usiaBudi -10

# usiaBudi *=2
# #usiaBudi = usiaBudi *2

# print(usiaAndi)
# print(usiaBudi)

# Latihan Numbers dan Aritmathica
# panjang = int(input("Berapa panjangnya?"))
# lebar = int(input("berapa lebarnya?"))

# luas = panjang * lebar

# print ('Luas persegi panjang adalah ', luas)

#Math Module
# import math

# print(math.pi)
# print(math.fabs(-100)) #mengabsolutikan angka minus
# print(pow(8,2)) #pangkat
# print(math.sqrt(50)) #akar kuadrat
# print(math.floor(4.7)) #membulatkan ke bawah. hasilnya 4
# print(math.ceil(4.7)) # membulatkan ke atas. hasilnya 5
# print(round(4.7)) # membulatkan sesuai aturan matematika
# print(round(4.1))

#usiaBudiAndi = 49
#rasioBudiAndi = 0.4

# umur_total = 49

# rasio_andi = 4
# rasio_budi = 10
# total_rasio = rasio_andi + rasio_budi

# Umur_andi = rasio_andi/total_rasio * umur_total
# Umur_budi = rasio_budi/total_rasio * umur_total

# tambahan_waktu = 2

# umur_andi_nanti = Umur_andi + tambahan_waktu
# umur_budi_nanti = Umur_budi + tambahan_waktu

# print(round(umur_andi_nanti))
# print(round(umur_budi_nanti))

# STRING
# teks = 'Mari kita belajar data science'

# print(len(teks)) #dari kata lenght
# print(teks.index("data")) #index dimulai dari nol. jadi M itu index ke Nol
# print(teks.split(" ")) #memisahkan teks berdasarkan spasi
# print(teks.split("a")) #split berdasarkan huruf A
# print(teks.capitalize()) #huruf besar awal kata
# print(teks.upper()) #huruf besar semua
# print(teks.lower()) #huruf kecil smw

# #string indexing
# #[start:stop:step]
# print(teks[0])
# print(teks[2:]) #mulai dari index 2 sampai seterusnya
# print(teks[2:10])
# print(teks[2:30:2]) #start 0, stop 30, step 2
# print(teks[:5]) #start fro beginning until 5 --> 0,1,2,3,4
# print(teks[:]) #start from beginning and stop until the end
# print(teks[::2]) #start from begining, stop until the end, step every 2
# print(teks[::-1]) #step minus artinya terbalik

#convert string to number
# panjang = input('masukan besaran panjang : ')
# lebar = input ('Masukan besaran lebar : ')

# print(type(panjang))
# print(type(lebar))

# print(panjang+lebar) #penggabungan string

# print(int(panjang) + int(lebar)) #sudah dikonversi ke integer
# print(float(panjang) + int(lebar)) # sudah dikonversi ke float

#usia = 22
# nama = 'andi'
# print (usia+usia)
# print (str(usia) + ' ' + nama) #konversi usia ke string
# print (str(usia) + ' ' + str(usia))


#latihan

# angka = int(input("silakan masukan angka berapapun"))

# kuadrat = angka ** 2

# print("kuadrat dari " + str(angka) + " " + "adalah : " + str(kuadrat))

#cara pakai format

#angka = int(input("masukan angka berapa pun : "))
#kuadrat = angka ** 2
#print(f'kuadrat dari {angka} = {kuadrat}') # f = format, bermanfaat untuk menyisipkan variabel dalam string

#LATIHAN
#sebuah perusahaan PT Sehat Sentosa memiliki 3 cabang pabrik di bandung, semarang dan surayaba
#Setiap cabang memiliki 3 jenis mesin penghasil masker, mesin A, mesin B dan mesin C
#Kapasitas produksi mesin A : 500 masker/hari, mesin B : 300 masker /hari, mesin C :100 masker/hari
# semua cabang memiliki 3 jenis mesin kecuali semarang (tidak punya mesin B)
# Berapa produksi masker oleh perusahaan Sehat sentosa selama 1 bulan ( 30 hari) ?

# mesinA = 500
# mesinB = 300
# mesinC = 100

# jumlahHari = 30

# surabaya = (mesinA + mesinB + mesinC)*jumlahHari
# bandung = (mesinA + mesinB + mesinC)*jumlahHari
# semarang =(mesinA + mesinC) *jumlahHari

# total = surabaya+bandung+semarang

# print(f'Kapasitas produksi PT Sehat Sentosa selama 1 bulan = {total} masker per hari')


#totalHari = int(input("Silakan masukkan total hari : "))

# totalHari = 485

# jumlahTahun = round(totalHari / 360)
# jumlahHari = totalHari % 360

# if (totalHari >= 360) :

#     jumlahBulan = round(jumlahHari / 30)
#     sisaHari = jumlahHari % 30   
#     print (f'{totalHari} hari terdiri dari {jumlahTahun} tahun {jumlahBulan} bulan {sisaHari} hari')
# else :
 
#     print (f'Jumlah hari adalah {totalHari}')

#jawabanlain
# data = 485

# tahun = round(data365)
# bulan = round((data- (tahun*360)) / 30)
# hari = (data - (tahun*360) - (bulan*30))

# print(tahun'tahun')
# print(bulan'bulan')
# print(hari'hari')
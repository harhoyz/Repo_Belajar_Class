#===================
# CLASS (Object Oriented Proggraming / OOP)

# Class = Cetakan

# class hewan :

#     #class attribute :
#     spesies = 'kambing'

#     #instance attribute
#     def __init__(self, asal, bobot, usia) :
#         self.asal = asal
#         self.bobot = bobot
#         self.usia = usia

# gaga = hewan('Garut', 40, 8)
# tutul = hewan('Tulungagung', 45, 7)

# mengakses 'Class atribtue'
# print (f'gaga adalah seekor {gaga.__class__.spesies}' )
# print (f'tutul adalah seekor {gaga.__class__.spesies}')

#Cerita 
# print ('Gaga adalah seekor {g.spesies}. Tutul juga seekor {t.spesies}. Gaga berasal dari {g.asal} Sedangkan Tutul berasal dari {t.asal}.'.format (g=gaga, t=tutul))

# print ('Tahun ini, Tutul menginjak usia {t.usia} tahun. Lebih muda setahun dari usia Gaga ({g.usia} tahun)'.format(g=gaga, t=tutul))

# print ('Meskipun lebih muda, Tutul memiliki bobot lebih tinggi ({t.bobot} kg) daripada Gaga ({g.bobot} kg'.format(g=gaga, t=tutul))

#========================================================================

#METHOD = function in class

# class hewan :

#     #class attribute :
#     spesies = 'kambing'

#     #instance attribute
#     def __init__(self, nama, asal, bobot, usia) :
#         self.nama = nama
#         self.asal = asal
#         self.bobot = bobot
#         self.usia = usia
    
#     # instance methods / function
    
#     def makan (self, makanan) :
#         return f'{self.nama} sedang menikmati {makanan}.'

#     def sate (self) :
#         tusuk_sate = self.bobot * 20 
#         return f'{self.nama} bisa diolah menjadi {tusuk_sate} tusuk sate'

# # Mengisi Cetakan 'class'
# kambing_baru = hewan('Etawa', 'Garut', 45, 9)

# #uji coba methods
# print(kambing_baru.makan('Daun Pisang'))
# print(kambing_baru.sate())

#=======================================

#LATIHAN MEMBUAT CLASS CALCULATOR

# class calculator :
#     def tambah (self, x, y) :
#         return x + y
#     def kurang (self, x,y) :
#         return x-y
#     def kali (self, x, y) :
#         return x * y
#     def bagi (self, x, y) :
#         return x / y
#     def pangkat (self, x, y) :
#         return x ** y

# print(calculator().tambah(4,5))
# print(calculator().kurang(40,5))
# print(calculator().kali(2,7))
# print(int(calculator().bagi(40,8)))
# print(calculator().pangkat(4,3))


#=====================================
# Latihan Buat Calculator Statistik
# Buatlah Class yang berisi method dengan fitur :
# 1. Menghitung nilai minimum dalam list (tidak boleh pake built ini function = min())
# 2. Menghitung nilai maximal dalam list (tidak boleh pake built ini function = max())
# 3. Menghitung panjang anggota dalam list (tidak boleh pake built ini function = len())
# 4. Mean tidak boleh pakai build in function
# 5. Standar Deviasi 
data = [2,3,4,5,6,7,8,8,9,21,3,2,5,4,1.5,12]

class statistik :

    def minimum (self, yourList):
        min = yourList[0]

        for i in yourList :
            if i < min :
                min = i
    
        return min

    def maximum (self, yourList):
        max = yourList [0]

        for i in yourList :
            if i > max :
                max = i
        return max 
    
    def panjang (self, yourList) :
        hitung = 0

        for i in yourList :
            hitung += 1
        return hitung

    def mean (self, yourList) :
        jumlah= 0
        hitung = 0

        for i in yourList :
            jumlah += i
            hitung +=1
            
        return jumlah/hitung

    def standev (self, yourList):
        pangkat = 0
        hitung = 0
        jumlah = 0

        for i in yourList :
            hitung += i
            jumlah += 1

        mean = hitung / jumlah #rata-rata data

        total = 0 # total penyimpangan
              
        for i in yourList :
            total += (i - mean)**2
                
        return (total/jumlah)**0.5
             
    #     #print(hitung)
    #     # hasil1 = jumlah**2 / hitung
    
    #     # hasil2 = (pangkat - hasil1) / (hitung -1)

    #     # standar = hasil2**0.5
        

# print(statistik().minimum(data))
# print (statistik().maximum(data))
# print (statistik().panjang(data))
print (statistik().mean(data))
print (statistik().standev(data))
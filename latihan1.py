#latihan 1
#1.Tampilkan n bilangan acak yang lebih kecil dari 0.5.
#2. nilai n diisi pada saat runtime
#3. anda bisa menggunakan kombinasi while dan for untuk menyelesaikannya
#4. gunakan fungsi random() yang dapat diimport terlebih dahulu

print(20*"=")

print("masukan nilai N = 5")
import random
jumlah = 5
a = 0
for x in range (jumlah) :
    i = random.uniform(.0,.5)
    a+=1
    print("data ke = ",a,"===>",i )

print("SELESAI")

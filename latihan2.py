#latihan 2
#Buat program untuk menampilkan bilangan terbesar dari n buah data yang diinputkan.
#Masukkan angka 0 untuk berhenti.

print(20*"=")

max=0
while True :
    x = int(input("masukan bilangan = "))
    if max < x :
        max = x
    if x == 0 :
        break

print("Bilangan terbesar adalah ", max)
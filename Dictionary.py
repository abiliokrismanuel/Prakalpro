# Nama : Abilio Krismanuel
# Nim : 71190498
# Grub B
# Universitas Kristen Duta Wacana


'''
    Buatlah sebuah program dictionary yang dapat menghitung baju dengan menginputkan ukuran baju yang diinputkan oleh user

    input : input ukuran baju , input baju lagi/tidak
    proses : perulangan while menanyakan inputan baju jika users sudah input baju maka di tanyain y/t
    output : semua ukuran baju dan jumlahnya


'''

jumlah = dict()
ukuran = []
stop = False
i = 0

while (not stop):
    masukan = input("Masukan ukuran baju :")
    ukuran.append(masukan)
    i += 1

    masukan1 = input("Lagi (y/t)?")
    if (masukan1 == "t"):
        stop= True

for x in ukuran :
    if x in jumlah :
        jumlah[x] += 1
    else :
        jumlah[x] = 1

print("\nukuran baju :\n",jumlah)
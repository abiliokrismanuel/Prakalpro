# Nama : Abilio Krismanuel
# Nim : 71190498
# Grub B
# Universitas Kristen Duta Wacana

'''
    seorang pedagang makanan mempunyai pelanggan yang suka menunya yaitu daging ayam dan daging babi
    maka bantulah pedagang tersebut dalam menentukan pelanggan mana yang suka keduanya

    input : masukan(pelanggan)
    proses : buat list , if not masukan maka break , masukan ke list , ayam & babi
    output : kedua list dan siapa yang menyukaia kedua daging tersebut


'''

list1 = []
list2 = []

print("Tolong masukan nama pelangan yang menyukai daging ayam :")

while True:
    masukan = input("---> ")
    if not masukan :
        break

    list1.append(tuple(masukan.split(",")))
x = set(list1)
print(x , "\n")

print("Tolong masukan nama pelanggan yang menyukai daging babi :")

while True :
    masukan = input("---> ")
    if not masukan :
        break

    list2.append(tuple(masukan.split(",")))

xx = set(list2)
print(xx , "\n")

print("pelanggan yang menyukai kedua daging : " ,x & xx)


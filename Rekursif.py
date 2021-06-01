# Nama : Abilio Krismanuel
# Nim : 71190498
# Grub B
# Universitas Kristen Duta Wacana


'''
buatlah sebuah program python yang dapat mengkonversi bilangan decimal ke bilangan biner oktal dan hexadecimal 
menggunakan rekursif

input : angka decimal , basis
proses : fungsi rekursif bilamana angka lebih kecil dari basis maka itu biner else okta dan hexadecimal
outputnya : angka biner oktal dan hexadecimal
'''

def rekur(angka,basis):
    kestring = "0123456789ABCDEF"
    if angka < basis:
        return kestring[angka]
    else:
        return rekur(angka//basis,basis) + kestring[angka%basis]

print("masukan angka yang akan di konversi ")
masukan = int(input("silahkan masukan angka :"))
masbas = int(input("silahkan masukan basisnya :"))

print(rekur(masukan,masbas))


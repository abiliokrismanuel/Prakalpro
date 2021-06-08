# Nama : Abilio Krismanuel
# Nim : 71190498
# Grub B
# Universitas Kristen Duta Wacana


'''
    buatlah sebuah password validasi yang memilik ketentuan sebagai berikut:
    1.hurup depan memiliki hurup besar
    2.memilik hurup kecil
    3.harus ada nomor
    4.karakter khusus (%$#*)

'''

import re

def main():
    masukan = input("masukan password anda :")
    rege = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#%*&])[A-Za-z\d@$#%*&]{6,20}$"

    cari = re.compile(rege)

    masu = re.search(cari,masukan)

    if masu:
        print("Password valid lurr")
    else:
        print("password salah lurr")

main()


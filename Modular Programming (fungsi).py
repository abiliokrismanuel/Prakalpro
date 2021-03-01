# Nama : Abilio Krismanuel
# Nim : 71190498
# Grub B
# Universitas Kristen Duta Wacana

''' 
    Seorang penjaga kasir di suatu tempat wisata kerepotan karena dia tidak jago matematika
    untuk menghitung diskon pelanggan bilamana jika pengunjung kurang dari 10 maka tidak di beri diskon 
    jika lebih dari sama dengan 10 pelanggan maka akan di berikan diskon 1o%
    dan bila lebih dari sama dengan 20 maka akan di beri diskon 20% 
    jika uang yang di bayarkan lebih dari yang harus di bayar maka boleh masuk jika tidak ya gaboleh
    
    input : pengunjung , tiket=10000 
    proses :def diskon1 diskon2 
    output : hasil hitungan uangnya

'''

def diskon1 (pengunjung,tiket,dis1):
    x = pengunjung * tiket * dis1
    return x

def diskon2 (pengunjung,tiket,dis2):
    xx= pengunjung * tiket * dis2
    return xx

def gadiskon(pengunjung,tiket):
    xxx = pengunjung * tiket
    return xxx

pengunjung = int(input("Masukan Jumlah Pengunjungnya :"))
tiket = 10000
dis1 = 0.1
dis2 = 0.2

if pengunjung < 10 :
    print("Anda tidak mendapat diskon")
    print("Silahkan bayar :Rp.",gadiskon(pengunjung,tiket))
    masukanuang2 = int (input("\nMasukan uang anda :Rp."))
    if masukanuang2 > gadiskon(pengunjung,tiket):
        print("Silahkan Bersenang senang")
    elif masukanuang2 < gadiskon(pengunjung,tiket):
        print("Mon maap ni uangnya kurang ya")

elif pengunjung >= 10:
    print("Selamat anda mendapat Diskon Sebesar 10%")
    print("Silahkan bayar :Rp.",diskon1(pengunjung,tiket,dis1))
    masukanuang = int(input("\nMasukan uang anda :Rp."))
    if masukanuang > diskon1(pengunjung,tiket,dis1):
        print("Silahkan Bersenang senang")
    elif masukanuang < diskon1(pengunjung,tiket,dis1):
        print("Mon maap ni uangnya kurang ya")

elif pengunjung >= 20 :
    print("Selamat anda mendapat Diskon Sebesar 20%")
    print("Silahkan bayar :Rp.",diskon2(pengunjung,tiket,dis2))
    masukanuang1 = int(input("\nMasukan uang anda :Rp."))
    if masukanuang1 > diskon2(pengunjung,tiket,dis2):
        print("Silahkan Bersenang senang")
    elif masukanuang1 < diskon2(pengunjung,tiket,dis2):
        print("Mon maap ni uangnya kurang")     
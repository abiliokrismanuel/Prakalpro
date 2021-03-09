# Nama : Abilio Krismanuel
# Nim : 71190498
# Grub B
# Universitas Kristen Duta Wacana

''' 
    Seorang penjual donat kebingungan dalam menentukan harga 1 donat lalu ia meminta tolong kepada seorang programer untuk menghitungkan
    donat yang akan di beli pelanggannya 

    input : banyakDonat :
            HargaDonat  :
    Proses : while banyakdonat > 0
            banyakdonat*harga

    output : looping while 
            total yang harus di bayar pembeli
'''

BanyakDonat = int(input("Berapa banyak Donat yang akan di beli pelanggan :"))
HargaDonat = int(input("Berapa Harga per donatnya :"))
nilai = 0
x = BanyakDonat*HargaDonat

while BanyakDonat > nilai :
    nilai = nilai + 1
    print(nilai," Donat :\t Rp.",nilai*HargaDonat)

print("\nTotal donat yang harus di bayarkan adalah :Rp.",x)



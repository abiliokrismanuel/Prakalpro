# Nama : Abilio Krismanuel
# Nim : 71190498
# Grub B
# Universitas Kristen Duta Wacana

'''
    Buatlah sebuah program yang menampilkan sebuah bilangan prima dan bilangan ganjil dengan menggunakan nilai 
    batas atas dan batas bawah. 

    Input = atas , bawah
    proses = for, if
    output = bilangan prima dan bilangan ganjil

'''

atas = int(input("Masukan Batas Atas : "))
bawah = int(input("Masukan batas Bawah : "))

print("\nBilangan Prima dari ",bawah," Sampai ",atas," : ")
for i in range(bawah,atas + 1):
    if i > 1 :
        for j in range (2,i):
            if (i %j) == 0:
                break
        else:
            print(i)

print("\nBilangan ganjil dari ",bawah," sampai ",atas," : ")
for i in range (bawah,atas +1):
    if i%2 == 1:
        print(i) 


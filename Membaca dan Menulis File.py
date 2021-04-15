# Nama : Abilio Krismanuel
# Nim : 71190498
# Grub B
# Universitas Kristen Duta Wacana

'''
    buatlah sebuah program python yang dapat mencari sebuah kata di dalam sebuah file txt 
    jika kata tersebut ada di dalam file maka akan di tampilkan outputnya berupakata yang di cari jika berhasil
    dan jika kata yang di cari tidak ada maka akan di tampilkan sebuah kata tidak lurr mohon di ulang kembali

    input : cari kata yang di cari
    proses ; membuat file txt dulu lalu di beri inputan user kata yang akan di cari lalu masuk ke perulangan
            dan di tampilkan output 
    output : kata yang di cari 

'''

filee = open('laprak8.txt','w')

filee.write(' haha hihi ')
filee.write(' AbiliO krismAnuel ')
filee.write(' asaL klaTen ')
filee.write(' iNforMatika ')
filee.write(' eRerEre ')

filee.close()

masukan = input("Masukan kata yang akan di cari di dalam file 'laprak.txt ' :")
file1 = open('laprak8.txt','r')

for line in file1:
    line = line.lower()
    line = line.split()
    if masukan in line:
        print("Kata ada di dalam file laprak8.txt berupa :",masukan)
    else:
        print("kata tidak lurr mohon di ulang kembali")

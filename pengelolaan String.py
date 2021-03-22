# Nama : Abilio Krismanuel
# Nim : 71190498
# Grub B
# Universitas Kristen Duta Wacana

'''
    Seorang siswa sd kebingungan tentang menentukan panjang/pendek di suatu kalimat
    maka dari itu buatkanlah program yang dapat mencari kata terpendek dan terpanjang untuk membantu anak sd tersebut

    input = masukan user 
    proses = for if 
    output = kata = terpedek
            kata = terpanjang

'''
masukan = input("Masukan kalimatnya :")

pecah = masukan.split(' ')
maks = len(pecah[0])
x=pecah[0]

minn = len(pecah[0])
xx= pecah[0]

for i in pecah :
    if len(i)>maks:
        maks=len(i)
        x =i
    
    elif len(i)<minn:
        minn=len(i)
        xx = i

print("\nKalimat terpanjang adalah",x)
print("Kalimat terpendek adalah",xx)



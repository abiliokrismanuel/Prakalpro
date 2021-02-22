# Nama : Abilio Krismanuel
# Nim : 71190498
# Grub B
# Universitas Kristen Duta Wacana


'''
Seorang siswa sd sedang kebingungan mengenai pelajaran matematika di sekolahnya tentang mengitung bangun datar
yaitu :
    1.segitiga
    2.persegi
    3.persegi panjang
Buatkanlah program yang dapat membantu anak sd tersebut 

inputnya = masuakan =1 - 3 
            a = alas
            l = luas

            s = s**2

            p = panajang
            l = lebar

        prosesnya : anak sd mengiputkan/ memilih 1 - 3  untuk memilih antara segitiga persegi danpersegi panjang nah lalu jika input nya adalah 
        1 maka masuk ke segitiga dan jika inputnya 2 maka persegi dan kalo 3 maka persegi panjang

        output : luas segitiga persegi dan persegi panjang 

'''
print("=====Menghitung bangun datar=====")
jawab = 'ya'

while (True):
    masukan = int(input("\n1.segitiga\n2.persegi\n3,persegi panjang\nMasukan pilihan anda :"))
    if masukan == 1 :
        a = float(input("\nMasukan alas segitiga :"))
        t = float(input("Masukan tinggi segitiga :"))
        rumus1 = 0.5 * a * t
        print("\nLuas segitiganya adalah :",rumus1)

    elif masukan == 2 :
        s = int(input("\nmasukan sisi persegi :"))
        rumus2 = s**2
        print("\nLuas perseginya adalah :",rumus2)

    elif masukan == 3 :
        p = int(input("\nMasukan panjang persegipanjang :"))
        l = int(input("masukan lebar persegi panjang :"))
        rumus3 = p*l
        print("\nLuas persegipanjangnya adalah :",rumus3)
    
    jawab = input("\nulangi tidak ?(ya atau tidak)")
    if jawab == 'tidak':
        break



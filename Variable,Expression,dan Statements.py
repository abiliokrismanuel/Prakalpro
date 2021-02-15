# Nama : Abilio Krismanuel
# Nim : 71190498
# Grub B
# Universitas Kristen Duta Wacana

'''Seorang siswa elektronika kebingungan karena dia tidak mampu untuk menghitung nilai ekuivalen
 resistansi resistor dengan gelang warna 
   gelang 1 = coklat
   gelang 2 = hitam
   gelang 3 = hijau
   gelang 4 = perak
    Ω
 bantulah siswa tersebut dalam menghitung nilai resistansi resistor dengan python

'''
'''
    input  : coklat = 1
             hitam = 0
            hijau = 5
            perak = 10%
             
    Proses : (coklat + hitam)* 10**5 +'perak' 
    Output : 1000000 ohm 10%
'''
print("Menghitung resistansi resistor")

print("Gelang siswa adalah")
print("Gelang 1 = coklat\nGelang 2 = hitam \nGelang 3 = hijau \nGelang 4 = perak \n")
print("=====Keterangan warna=====\ncoklat = 1\nhitam = 0\nhijau = 5\nperak = 10%\n")

coklat = str(1)
hitam = str(0)
hijau = 10**5
perak = "10%"

x = int(coklat + hitam)

hasil = x * hijau 
print("Hasil penghitungan resistansi resistor = ",hasil,"ohm Ω",perak)



# Nama : Abilio Krismanuel
# Nim : 71190498
# Grub B
# Universitas Kristen Duta Wacana



'''
    Buatlah program untuk menggabungkan 2 list dan mengurutkannya.lalu memiliki fitur-fitur program adalah sebagai 
    berikut : 
    1. User harus menginputkan jumlah dari elemen list pertama dan menyimpannya pada variable 
    2. Kemudian user harus memasukan nilai-nilai elemen pertama satu persatu. 
    3. Proses yang sama dilakukan untuk list kedua.
    4. Program harus dapat menggabungkan kedua list yang diinputkan.
    5. Setelah itu program harus dapat mengurutkan list tersebut dengan menggunakan method "sort()" 
    6. Setelah itu program menampilkan list ke layar.

    input = masukan user untuk menginput berapa isi list nya di list 1
            masukan user untuk menginput berapa isi list nya di list 2

    proses = user menginputkan list 1 dan list 2 lalu di gabungkan dan si sort  

    output = gabungan 2 list dan di sort 

'''

masukan1 = int(input("Masukan jumlah elemen yang berada di list pertama : "))
list1 = []

for i in range (1, masukan1+1):
    elemen1 = input("masukan angka : ")
    list1.append(elemen1)
    list1.sort()
print("List 1 : ",list1)

masukan2 = int (input("\nmasukan jumlah elemen yang berada di list kedua : "))
list2 = []

for j in range (1 , masukan2+1):
    elemen2 = input("masukan angka : ")
    list2.append(elemen2)
    list2.sort()
print("list 2 : ",list2)

gabung = list1+list2
gabung.sort()
print("\nHasil gabungan kedua list tersebut adalah :\nlist",gabung)


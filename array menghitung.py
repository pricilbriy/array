#deklarasi array
array = []
#membuat variabel total
total = 0
#membuat variabel n untuk menampung jumlah array yang di inputkan
n =int(input("masukkan jumlah elemen array  : "))
for x in range(n) :
    #menghitung nilai yang akan bertambah satu
    nilai = float(input("masukkan nilai ke- {} :".format(x+1)))
    array.append(nilai)
    #menampilkan jumlah dari nilai
    print("\nhasil nilai total adalah : {}".format(sum(array)))
    #menampilkan rata rata
    print("hasil rata rata adalah : {}".format(sum(array)/n))

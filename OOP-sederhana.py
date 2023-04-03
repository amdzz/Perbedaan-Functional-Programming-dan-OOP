class Orang : #definisi kelas
    def __init__(self, nama, umur): #koknstruktor dari kelas
        self.nama = nama
        self.umur = umur

    def info(self): #fungsi untuk menampilkan informasi objek Orang
        print("Nama:",self.nama)
        print("Umur:",self.umur)

#membuat objek
Orang1 = Orang("Zhafran",18)
Orang2 = Orang("Ahmad",17)

#memanggil fungsi info() untuk menampilkan output informasi kedua objek
Orang1.info()
Orang2.info()
    

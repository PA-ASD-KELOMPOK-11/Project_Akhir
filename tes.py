import time 
import os
os.system ("cls")

class daftar:
    def __init__(self, mobil, peminjam):
        self.mobil = mobil
        self.peminjam = peminjam
        self.next = None

class databos:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.riwayat = []

    def newdata (self):
        rental = daftar(mobil, peminjam)
        if self.head is None:
            self.head = rental
        else:
            rental.next = self.head
            self.head = rental
        self.riwayat.append (f"Ditambahkan : {rental.mobil} (Peminjam A.N {rental.peminjam})")

    def nowcardata (self):
        if self.head is None:
            print("Tidak ada data peminjaman")
        else:
            current = self.head
            while current is not None:
                print (f"{current.mobil} (Peminjam A.N {current.peminjam})")
                current = current.next
    
    def carlist (self, mobil, peminjam):
        data_baru = daftar (mobil, peminjam)
        if self.head == None:
            self.head = data_baru
        else:
            data_baru.next = self.head
            self.head = data_baru
    
    def deletecardata (self, mobil):
        cardatanow = self.head
        previouscardata = None
        while cardatanow is not None:
            if cardatanow.mobil == mobil:
                if previouscardata is not None:
                    previouscardata.next = cardatanow.next
                    if cardatanow.next is None:
                        self.tail = previouscardata
                else:
                    self.head = cardatanow.next
                    if self.head is None:
                        self.tail = None
                self.riwayat.append (f"Dibatalkan  : {cardatanow.mobil} (Peminjam A.N {cardatanow.peminjam})")
                return True
            else:
                previouscardata = cardatanow
                cardatanow = cardatanow.next
        return False
    
    def history (self):
        print ("==Riwayat Data Peminjaman Mobil==")
        
        for carhistory in self.riwayat:
            print (carhistory)

def pemilik() :
        os.system ("cls")
        print ("""=================================
||||>>>=== 11 Rent Car ===<<<||||
=================================
|1. Tambah Data Rental          |
|2. Tampilkan Data Rental       |
|3. Hapus Data Rental           |
|4. Riwayat Peminjaman Mobil    |
|5. Keluar                      |
=================================
""")

rentcar = databos()
rentcar.carlist("Innova Reborn", "Rikad Anggoro")
rentcar.carlist("Avanza Veloz", "Joko Susanto")

akun = {" User " : ["Pemilik","Pembeli"],
        " Passw " : ["123", "456"]}

while True:
    print ("~~~/\/\/\/\ 11 Rent Car /\/\/\/\~~~")
    posisi = input(" Masukkan Username \t\t: ")
    try :
        temukan = akun.get(" User ").index (posisi)
        if akun.get(" User ")[temukan]=="Pemilik":
            pw = input (" Masukkan Password \t: ")
            if posisi == akun.get(" User ")[temukan] and pw == akun.get(" Passw ")[temukan]:
                pemilik()
                while True:
                    pilih = input ("Masukkan Pilihan : ")
                    if pilih == "1":
                        mobil = input ("Jenis Mobil   : ")
                        peminjam = input("Nama Peminjam : ")
                        rentcar.newdata()
                        input ("=================================")
                    elif pilih == "2":
                        rentcar.nowcardata()
                        input ("=================================")
                    elif pilih == "3":
                        mobil = input ("Jenis Mobil : ")
                        if rentcar.deletecardata(mobil):
                            print ("Peminjaman Mobil Telah Dibatalkan")
                            input ("=================================")
                        else:
                            print ("Data Tidak Ditemukan")
                            input ("=================================")
                    elif pilih == "4":
                        rentcar.history()
                        input ("=================================")
                    elif pilih == "5":
                        break
                    else:
                        print ("Pilihan Salah")
                        time.sleep(1)
            else:
                    print (" Password Yang Anda Masukan SALAH ")
        else: 
            akun.get(" User ")[temukan]=="Pembeli"
            pw = input (" Masukkan Password \t\t: ")
            if posisi == akun.get(" User ")[temukan] and pw == akun.get(" Passw ")[temukan]:
                rentcar.nowcardata()

    except ValueError:
        print (" Maaf Username Tidak Ditemukan ")
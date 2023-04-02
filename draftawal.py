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

rentcar = databos()
rentcar.carlist("Innova Reborn", "Rikad Anggoro")
rentcar.carlist("Avanza Veloz", "Joko Susanto")

def loguser():
    print ("~~~/\/\/\/\ 11 Rent Car /\/\/\/\~~~")
    input ("Username : ")
    input ("Password : ")
    return True

if loguser():
    while True:
        os.system ("cls")
        print ("=================================")
        print ("||||>>>=== 11 Rent Car ===<<<||||")    
        print ("=================================")
        print ("1. Tambah Data Rental")
        print ("2. Tampilkan Data Rental")
        print ("3. Hapus Data Rental")
        print ("4. Riwayat Peminjaman Mobil")
        print ("5. Keluar")
        print ("=================================")
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
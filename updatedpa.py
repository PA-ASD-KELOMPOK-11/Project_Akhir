import time 
import os
from prettytable import PrettyTable
os.system ("cls")

class daftar:
    def __init__(self, peminjam, mobil, tanggal, bulan, tahun):
        self.peminjam = peminjam
        self.mobil = mobil
        self.tanggal = tanggal
        self.bulan = bulan
        self.tahun = tahun
        self.next = None

class mobil:
    def __init__(self, no, oto):
        self.no = no
        self.oto = oto
        self.next = None

class databos:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.riwayat = []

    def newdata (self, rental):
        if self.head == None:
            self.head = rental
            self.tail = self.head
        else:
            self.tail.next = rental
            self.tail = self.tail.next
        self.riwayat.append(("Ditambahkan",(rental.peminjam, rental.mobil, rental.tanggal, rental.bulan, rental.tahun)))
    
    def newdata1 (self, mobil):
        if self.head is None:
            self.head = mobil
        else:
            mobil.next = self.head
            self.head = mobil

    def nowcardata (self):
        table = PrettyTable()
        table.field_names = ["ID", "Peminjam", "Mobil", "Tanggal", "Bulan", "Tahun"]
        number = 1
        if self.head is None:
            print("Tidak ada data peminjaman")
        else:
            current = self.head
            while current is not None:
                table.add_row([number, current.peminjam, current.mobil, current.tanggal, current.bulan, current.tahun])
                number += 1
                current = current.next
            print(table)
    
    def carlist (self):
        table = PrettyTable()
        table.field_names = ["ID", "Peminjam", "Mobil", "Tanggal", "Bulan", "Tahun"]
        carlist = self.head
        while carlist:
            table.add_row([carlist.id, carlist.peminjam, carlist.mobil, carlist.tanggal, carlist.bulan, carlist.tahun])
            carlist = carlist.next
        print (table)

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
                self.riwayat.append(("Dibatalkan",(cardatanow.peminjam, cardatanow.mobil, cardatanow.tanggal, cardatanow.bulan, cardatanow.tahun)))
                return True
            else:
                previouscardata = cardatanow
                cardatanow = cardatanow.next
        return False
    
    def search(self, keyword):
        table = PrettyTable()
        table.field_names = ["ID","Mobil", "Peminjam","Tanggal","Bulan","Tahun"]
        cari = self.head
        while cari is not None:
            if keyword.lower() in cari.id.lower() or keyword.lower() in cari.mobil.lower() or keyword.lower() in cari.peminjam.lower():
                table.add_row([ cari.id,cari.mobil, cari.peminjam,cari.tanggal,cari.bulan,cari.tahun])
            cari = cari.next
        if len(table._rows) == 0:
            print("Data Peminjaman Tidak Ditemukan")
        else:
            print(table)

    def history (self):
        t = PrettyTable(['Keterangan', 'Peminjam', 'Mobil', 'Tanggal', 'Bulan', 'Tahun'])
        

        for i in self.riwayat:
            t.add_row([i[0], i[1][0], i[1][1], i[1][2], i[1][3], i[1][4]])
        print(t)
    

    def mobilrental (self):
        table = PrettyTable()
        table.field_names = ["No", "Mobil"]
        mobilrental = self.head
        while mobilrental:
            table.add_row([mobilrental.no, mobilrental.oto])
            mobilrental = mobilrental.next
        print (table)

def admin() :
    os.system ("cls")
    print ("=================================")
    print ("||||>>>=== 11 Rent Car ===<<<||||")
    print ("=================================")
    print ("|1. Tampilkan Data Rental       |")
    print ("|2. Hapus Data Rental           |")
    print ("|3. Riwayat Peminjaman Mobil    |")
    print ("|4. Cari Data Pemesan           |")
    print ("|5. Keluar                      |")
    print ("=================================")

def pembeli() :
    os.system ("cls")
    print ("=================================")
    print ("||||>>>=== 11 Rent Car ===<<<||||")
    print ("=================================")
    print ("|1. Tampilkan Daftar Mobil      |")
    print ("|2. Buat Pemesanan              |")
    print ("=================================")

rentcar = databos()
rentcar.newdata(daftar("Rikad Anggoro", "Innova Reborn", "2", "April", "2023"))
rentcar.newdata(daftar("Joko Susanto", "Avanza Veloz", "5", "Maret", "2023"))


rentcar1=databos()
rentcar1.newdata1(mobil("1","Innova Reborn"))
rentcar1.newdata1(mobil("2","Avanza Veloz"))

akun = {" User " : ["Pemilik","Pembeli"],
        " Passw " : ["123", "0"]}

while True:
    print ("~~~/\/\/\/\ 11 Rent Car /\/\/\/\~~~")
    posisi = str.capitalize(input(" Masukkan Username : "))
    try :
        temukan = akun.get(" User ").index (posisi)
        if akun.get(" User ")[temukan]=="Pemilik":
            pw = input (" Masukkan Password : ")
            if posisi == akun.get(" User ")[temukan] and pw == akun.get(" Passw ")[temukan]:
                admin()
                while True:
                    pilih = input ("Masukkan Pilihan   : ")
                    if pilih == "1":
                        rentcar.nowcardata()
                        input ("=================================")
                    elif pilih == "2":
                        jenis = input ("Jenis Mobil : ")
                        if rentcar.deletecardata(jenis):
                            print ("Peminjaman Mobil Telah Dibatalkan")
                            input ("=================================")
                        else:
                            print ("Data Tidak Ditemukan")
                            input ("=================================")
                    elif pilih == "3":
                        rentcar.history()
                        input ("=================================")
                    elif pilih == "4":
                        cari = input("cari :")
                        rentcar.search(cari)
                    elif pilih == "5":
                        break
                    else:
                        print ("Pilihan Salah")
                        time.sleep(1)
            else:
                    print (" Password Yang Anda Masukan SALAH ")
        else: 
            akun.get(" User ")[temukan]=="Pembeli"
            pw = input (" Masukkan Password : ")
            if posisi == akun.get(" User ")[temukan] and pw == akun.get(" Passw ")[temukan]:
                pembeli()
                while True:
                    pilih = input ("Masukkan Pilihan : ")
                    if pilih == "1":
                        rentcar1.mobilrental()
                    elif pilih == "2":
                        nama= input ("Nama Peminjam      : ")
                        mbl = input ("Jenis Mobil        : ")
                        tgl = input ("Tanggal Peminjaman : ")
                        bln = input ("Bulan Peminjaman   : ")
                        thn = input ("Tahun Peminjaman   : ")
                        pesan = daftar(nama,mbl,tgl,bln,thn)
                        rentcar.newdata(pesan)
                        input ("=================================")
                    else:
                        print ("Pilihan Salah")
                        time.sleep(1)

    except ValueError:
        print (" Maaf Username Tidak Ditemukan ")
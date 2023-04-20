from pymongo import MongoClient
import pwinput
import time 
import os
import math
from prettytable import PrettyTable
os.system ("cls")


cluster = MongoClient("mongodb+srv://rikadanggoro:rikadanggoro123@rikad.biksr9o.mongodb.net/tes")

# Database Name
db = cluster["PAasd"]

# Collection Name (akun,mobil,data)
akun_admin = db["admin"]
akun_pembeli = db["pembeli"]
data_mobil = db["list_mobil"]
pesanan = db["pesanan"]
riwayat = db["riwayat"]

#============================================= MENU LOGIN AWAL =============================================      
def login():
    os.system ("cls")
    print("==================================")
    print("|          11 Rent Car           |")
    print("==================================")
    print("| 1. Admin                       |")
    print("| 2. Pembeli                     |")
    print("==================================")
    pilih = str(input("Masukkan Pilihan : "))
    time.sleep (1)
    if pilih == "1":
        while True:
            os.system ("cls")
            print("===================================================")
            print("                    L O G I N                      ")
            print("===================================================")
            username = str.capitalize(input("Masukkan Username : "))
            pw = str.lower(pwinput.pwinput("Masukkan Password : "))
            result = akun_admin.find_one({"admin": username, "pass": pw})
            if result and result["admin"] == username and result["pass"] == pw:
                print("Login Berhasil!")
                time.sleep (2)
                admin()
            elif result is None:
                print("Login Gagal!")
                time.sleep (2)
            else:
                print("Login Gagal!")

    elif pilih == "2":
        while True:
            os.system ("cls")
            print("==================================")
            print("|         P E M B E L I          |")
            print("==================================")
            print("| 1. Login                       |")
            print("| 2. Registrasi Akun             |")
            print("==================================")
            pilih = str(input("Masukkan Pilihan : "))
            if pilih == "1":
                username = str.capitalize(input("Masukkan Username : "))
                pw = str.lower(pwinput.pwinput("Masukkan Password : "))
                result = akun_pembeli.find_one({"pembeli": username, "pass": pw})
                if result and result["pembeli"] == username and result["pass"] == pw:
                    print("Login Berhasil!")
                    time.sleep (2)
                    pembeli()
                elif result is None:
                    print("Login Gagal!")
                    time.sleep (2)
                else:
                    print("Login Gagal!")
            elif pilih == "2":
                    username_baru = str.capitalize(input("Masukkan username baru: "))
                    cek = akun_pembeli.find_one({"pembeli": username_baru})
                    if cek is not None:
                        print("Nama telah digunakan!")
                        time.sleep (2)
                    else:
                        password_baru = str.lower(input("Masukkan password baru: "))
                        akun_pembeli.insert_one({"pembeli": username_baru, "pass": password_baru})
                        print("Registrasi Berhasil!")
                        time.sleep (2)
    else:
        print("Pilihan tidak tersedia!")

#============================================= MENU ADMIN =============================================               
def admin():
    while True:
        os.system ("cls")
        print ("=============================================")
        print ("||||||>>>>>===== 11 Rent Car =====<<<<<||||||")
        print ("=============================================")
        print ("|1. Tampilkan Data                          |")
        print ("|2. Hapus Data Rental                       |")
        print ("|3. Riwayat Peminjaman Mobil                |")
        print ("|4. Cari Data Pemesan                       |")
        print ("|5. Log Out                                 |")
        print ("=============================================")
        pilih = str(input("Masukkan Pilihan : "))
        if pilih == "1":
            os.system("cls")
            print ("=============================================")
            print ("|               S O R T I N G               |")
            print ("=============================================")
            print ("|1. Berdasarkan Nama                        |")
            print ("|2. Berdasarkan Tanggal                     |")
            print ("|3. Berdasarkan Bulan                       |")
            print ("=============================================")
            choose = str(input("Tentukan Pilihan : "))
            if choose == "1":
                RentalMobil().pengurutan_nama()
                input ("")
            elif choose == "2":
                RentalMobil().pengurutan_tanggal()
                input ("")
            elif choose == "3":
                RentalMobil().pengurutan_bulan()
                input ("")
        elif pilih == "2":
            RentalMobil().delete()
        elif pilih == "3":
            RentalMobil().history()
            input ("")
        elif pilih == "4":
            RentalMobil().search()
        elif pilih == "5":
            login()
        else:
            print ("Pilihan Salah")
            time.sleep(1)

#============================================= MENU PEMBELI =============================================      
def pembeli():
    while True:
        os.system ("cls")
        print ("=================================")
        print ("||||>>>=== 11 Rent Car ===<<<||||")
        print ("=================================")
        print ("|1. Lihat Daftar Mobil          |")
        print ("|2. Buat Pemesanan              |")
        print ("|3. Exit                        |")
        print ("=================================")
        pilih = str(input("Masukkan Pilihan : "))
        if pilih == "1":
            RentalMobil().nowcardata_user()
            time.sleep (2)
        elif pilih == "2":
            RentalMobil().newdata()
        elif pilih == "3":
            login()

#============================================= CLASS =============================================      
class Daftar:
    def __init__(self, rentaldata = None):
        self.rentaldata = rentaldata
        self.next = None

class RentalMobil:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.riwayat_collection = db["riwayat"]
    
    def append(self, rentaldata):
        new_node = Daftar(rentaldata)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # fungsi untuk menambahkan data pesanan
    def newdata(self):
        self.nowcardata_user()
        peminjam = str.capitalize(input("Nama Peminjam : "))
        mobil = str.title(input("Jenis Mobil   : "))
        for i in data_mobil.find({"mobil": mobil}):
            if i["mobil"] == mobil:
                print("Mobil Tersedia")
                tanggal = int(input("Tanggal Peminjaman : "))
                bulan = int(input("Bulan Peminjaman   : "))
                tahun = int(input("Tahun Peminjaman   : "))
                pesan = {
                    "peminjam": peminjam,
                    "mobil": mobil,
                    "tanggal": tanggal,
                    "bulan": bulan,
                    "tahun": tahun
                }
                pesanan.insert_one(pesan)
                riwayat.insert_one({"keterangan": "Ditambah", "peminjam": peminjam, "mobil": mobil, "tanggal": tanggal, "bulan": bulan, "tahun": tahun})
                print("Data berhasil ditambah!")

                rentaldata = [peminjam, mobil, tanggal, bulan, tahun]
                self.append(rentaldata)
                time.sleep (2)
                pembeli()

        print("Mobil Tidak Tersedia")
        time.sleep (2)
        self.newdata()

    # fungsi untuk menampilkan data pesanan admin
    def nowcardata_admin(self):
        data = pesanan.find({})

        if data is None:
            print("Data Kosong")
        else:
            tabel = PrettyTable()
            tabel.field_names = ["ID","Peminjam", "Mobil", "Tanggal", "Bulan", "Tahun"]
            number = 1
            for i in data:
                tabel.add_row([number, i["peminjam"], i["mobil"], i["tanggal"], i["bulan"], i["tahun"]])
                number += 1
            print(tabel)

    def nowcardata_user(self):
        tampung = []
        for i in data_mobil.find({}):
            tampung.append(i)

        if tampung is None:
            print("Data Kosong")
        else:
            tabel = PrettyTable()
            tabel.field_names = ["Nomor", "Mobil"]
            number = 1
            for i in tampung:
                tabel.add_row([number, i["mobil"]])
                number += 1
            print(tabel)

    #fungsi untuk menghapus data pesanan berdasarkan nama peminjam
    def delete(self):
        peminjam = str.capitalize(input("Masukkan Nama Peminjam: "))
        rental_data = []            
        for rental in pesanan.find({}):
            rental_data.append(rental)
        if not rental_data:
            print("Tidak ada Data Pemesanan")
        else:
            found = False
            for data in rental_data:
                if data["peminjam"] == peminjam:
                    found = True
                    break
            if not found:
                print(f"Data Pemesanan {peminjam} tidak ditemukan")
                input("")
            else:
                simpan = []
                rental = pesanan.find_one({"peminjam": peminjam})
                simpan.append(rental["peminjam"])
                simpan.append(rental["mobil"])
                simpan.append(rental["tanggal"])
                simpan.append(rental["bulan"])
                simpan.append(rental["tahun"])
                riwayat.insert_one({"keterangan": "Dihapus", "peminjam": peminjam, "mobil": simpan[1], "tanggal": simpan[2], "bulan": simpan[3], "tahun": simpan[4]})
                pesanan.delete_one({"peminjam": peminjam})
                print(f"Data Pemesanan {peminjam} berhasil dihapus!")
                input("")

    def mergeSort_nama(self, rentaldata):
        penampungan = []
        for i in pesanan.find({}):
            penampungan.append(i)

        if not penampungan:
            print("List Kosong")
            return

        if len(rentaldata) > 1:
            mid = len(rentaldata) // 2
            left = rentaldata[:mid]
            right = rentaldata[mid:]

            self.mergeSort_nama(left)
            self.mergeSort_nama(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i]["peminjam"] < right[j]["peminjam"]:
                    rentaldata[k] = left[i]
                    i += 1
                else:
                    rentaldata[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                rentaldata[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                rentaldata[k] = right[j]
                j += 1
                k += 1
        return rentaldata

    def pengurutan_nama(self):
        penampungan = []
        for i in pesanan.find({}):
            penampungan.append(i)

        result = self.mergeSort_nama(penampungan) 
        number = 1
        table = PrettyTable()
        table.field_names = ["ID","Peminjam", "Mobil", "Tanggal", "Bulan", "Tahun"]
        for x in result:
            table.add_row([number, x["peminjam"], x["mobil"], x["tanggal"], x["bulan"], x["tahun"]])
            number += 1
        table.sortby = "Peminjam"
        print(table)

    def mergeSort_tanggal(self, rentaldata):
        penampungan = []
        for i in pesanan.find({}):
            penampungan.append(i)

        if not penampungan:
            print("List Kosong")
            return
            
        if len(rentaldata) > 1:
            mid = len(rentaldata) // 2
            left = rentaldata[:mid]
            right = rentaldata[mid:]

            self.mergeSort_tanggal(left)
            self.mergeSort_tanggal(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i]["tanggal"] < right[j]["tanggal"]:
                    rentaldata[k] = left[i]
                    i += 1
                else:
                    rentaldata[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                rentaldata[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                rentaldata[k] = right[j]
                j += 1
                k += 1
        return rentaldata

    def pengurutan_tanggal(self):
        penampungan = []
        for i in pesanan.find({}):
            penampungan.append(i)

        result = self.mergeSort_tanggal(penampungan) 
        number = 1
        table = PrettyTable()
        table.field_names = ["ID","Peminjam", "Mobil", "Tanggal", "Bulan", "Tahun"]
        for x in result:
            table.add_row([number, x["peminjam"], x["mobil"], x["tanggal"], x["bulan"], x["tahun"]])
            number += 1
        print(table)

    def mergeSort_bulan(self, rentaldata):
        penampungan = []
        for i in pesanan.find({}):
            penampungan.append(i)

        if not penampungan:
            print("List Kosong")
            return

        if len(rentaldata) > 1:
            mid = len(rentaldata) // 2
            left = rentaldata[:mid]
            right = rentaldata[mid:]

            self.mergeSort_bulan(left)
            self.mergeSort_bulan(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i]["bulan"] < right[j]["bulan"]:
                    rentaldata[k] = left[i]
                    i += 1
                else:
                    rentaldata[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                rentaldata[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                rentaldata[k] = right[j]
                j += 1
                k += 1
        return rentaldata

    def pengurutan_bulan(self):
        penampungan = []
        for i in pesanan.find({}):
            penampungan.append(i)

        result = self.mergeSort_bulan(penampungan) 
        number = 1
        table = PrettyTable()
        table.field_names = ["ID","Peminjam", "Mobil", "Tanggal", "Bulan", "Tahun"]
        for x in result:
            table.add_row([number, x["peminjam"], x["mobil"], x["tanggal"], x["bulan"], x["tahun"]])
            number += 1
        print(table)

    def jump_search(self, key):
        penampungan = []
        for i in pesanan.find({}):
            penampungan.append(i)

        if not penampungan:
            print("List Kosong")
            return None

        penampungan = sorted(penampungan, key=lambda x: x["peminjam"])

        n = len(penampungan)
        step = math.sqrt(n)
        prev = 0
        while penampungan[int(min(step, n) - 1)]["peminjam"] < key:
            prev = step
            step += math.sqrt(n)
            if prev >= n:
                return None

        while penampungan[int(prev)]["peminjam"] < key:
            prev += 1
            if prev == min(step, n):
                return None

        if penampungan[int(prev)]["peminjam"] == key:
            return penampungan[int(prev)]

        return None

    def search(self):
        penampungan = []
        for i in pesanan.find({}):
            penampungan.append(i)

        if not penampungan:
            print("List Kosong")
            input ("")
            return

        nama = str.capitalize(input("Masukkan nama yang ingin dicari: "))
        result = self.jump_search(nama)
        if result is not None:
            table = PrettyTable()
            table.field_names = ["Peminjam", "Mobil", "Tanggal", "Bulan", "Tahun"]
            table.add_row([result["peminjam"], result["mobil"], result["tanggal"], result["bulan"], result["tahun"]])
            print(table)
            input ("")
        else:
            print("Nama tidak ditemukan")
            input ("")

    def history (self):
        data = []
        for x in riwayat.find({}):
            data.append(x)
        t = PrettyTable(["Keterangan", "Peminjam", "Mobil", "Tanggal", "Bulan", "Tahun"])
        t.title = "Riwayat"
        for i in data:
            t.add_row([i["keterangan"], i["peminjam"], i["mobil"], i["tanggal"], i["bulan"], i["tahun"]])
        print(t)

login()
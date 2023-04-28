from pymongo import MongoClient
import pwinput
import time 
import datetime
import os
import math
from prettytable import PrettyTable
from dotenv import load_dotenv
os.system ("cls")

load_dotenv()

cluster = MongoClient(os.getenv("MONGO_URI"))

# Database Name
db = cluster["PAasd"]

# Collection Name (akun,mobil,data)
akun_admin = db["admin"]
akun_pembeli = db["pembeli"]
data_mobil = db["list_mobil"]
pesanan = db["pesanan"]
riwayat = db["riwayat"]

            
class Daftar:
    def __init__(self, rentaldata = None):
        self.rentaldata = rentaldata
        self.next = None

class RentalMobil:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.riwayat = []
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
        while True:
            mobil = str.title(input("Jenis Mobil : "))
            for i in data_mobil.find({"mobil": mobil}):
                if i["mobil"] == mobil:
                    print("Mobil Tersedia")
                    tanggal_pes = datetime.datetime.now()
                    waktu = tanggal_pes.strftime("%X-%d-%B-%Y")
                    while True:
                        try:
                            sampai = int(input("masukan jumlah hari peminjaman : "))
                            if sampai <= 10:
                                tanggal_kem = tanggal_pes + datetime.timedelta(days=sampai)

                                pesan = {
                                    "peminjam": peminjam,
                                    "mobil": mobil,
                                    "tanggal pesan": tanggal_pes.strftime("%Y-%m-%d"),
                                    "tanggal kembali":tanggal_kem.strftime("%Y-%m-%d")}
                                pesanan.insert_one(pesan)
                                riwayat.insert_one({"keterangan": f"Ditambah pada: {waktu}", "peminjam": peminjam, "mobil": mobil, "tanggal pesan": tanggal_pes.strftime("%Y-%m-%d"), "tanggal kembali": tanggal_kem.strftime("%Y-%m-%d")})
                                loading()
                                print("Data berhasil ditambah!")
                                print("Untuk melakukan pembayaran silahkan menuju kasir")

                                rentaldata = [peminjam, mobil, tanggal_pes, tanggal_kem]
                                self.append(rentaldata)
                                time.sleep (2)
                                pembeli()
                            elif sampai > 10:
                                print("batas peminjaman adalah 10 hari")
                            else:
                                print("perhatikan inputan anda")
                                break    
                        except ValueError:
                                print("perhatikan inputan anda")                    
            else:
                print("Mobil Tidak Tersedia")
        # time.sleep (1)
        # self.newdata()


    # fungsi untuk menampilkan data pesanan admin
    def nowcardata_admin(self):
        data = pesanan.find({})

        if data is None:
            print("Data Kosong")
        else:
            tabel = PrettyTable()
            tabel.field_names = ["ID","Peminjam", "Mobil", "Tanggal pesan", "Tanggal kembali"]
            number = 1
            for i in data:
                tabel.add_row([number, i["peminjam"], i["mobil"], i["tanggal pesan"], i["tanggal kembali"]])
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
        waktu1 = datetime.datetime.now()
        waktu = waktu1.strftime("%X-%d-%B-%Y")
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
                loading()
            else:
                simpan = []
                rental = pesanan.find_one({"peminjam": peminjam})
                simpan.append(rental["peminjam"])
                simpan.append(rental["mobil"])
                simpan.append(rental["tanggal pesan"])
                simpan.append(rental["tanggal kembali"])
                riwayat.insert_one({"keterangan": f"Dihapus pada: {waktu}", "peminjam": peminjam, "mobil": simpan[1], "tanggal pesan": simpan[2], "tanggal kembali": simpan[3]})
                pesanan.delete_one({"peminjam": peminjam})
                print(f"Data Pemesanan {peminjam} berhasil dihapus!")
                loading()

#======================================================= shorting =========================================================

    #fungsi untuk mengurutkan data berdasarkan tanggal pesan
    def mergesShort_pes(self, rentaldata):
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

            self.mergesShort_pes(left)
            self.mergesShort_pes(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i]["tanggal pesan"] < right[j]["tanggal pesan"]:
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

    def pengurutan_pes(self):
        penampungan = []
        for i in pesanan.find({}):
            penampungan.append(i)

        result = self.mergesShort_pes(penampungan) 
        number = 1
        table = PrettyTable()
        table.field_names = ["ID","Peminjam", "Mobil", "Tanggal pesan", "Tanggal kembali"]
        for x in result:
            table.add_row([number, x["peminjam"], x["mobil"], x["tanggal pesan"], x["tanggal kembali"]])
            number += 1
        print(table)

    #fungsi untuk mengurutkan data berdasarkan tanggal kembali
    def mergesShort_kem(self, rentaldata):
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

            self.mergesShort_kem(left)
            self.mergesShort_kem(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i]["tanggal kembali"] < right[j]["tanggal kembali"]:
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

    def pengurutan_kem(self):
        penampungan = []
        for i in pesanan.find({}):
            penampungan.append(i)

        result = self.mergesShort_kem(penampungan) 
        number = 1
        table = PrettyTable()
        table.field_names = ["ID","Peminjam", "Mobil", "Tanggal pesan", "Tanggal kembali"]
        for x in result:
            table.add_row([number, x["peminjam"], x["mobil"], x["tanggal pesan"], x["tanggal kembali"]])
            number += 1
        print(table)

    #fungsi untuk mengurutkan data berdasarkan nama peminjam
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
        table.field_names = ["ID","Peminjam", "Mobil", "Tanggal pesan", "Tanggal kembali"]
        for x in result:
            table.add_row([number, x["peminjam"], x["mobil"], x["tanggal pesan"], x["tanggal kembali"]])
            number += 1
        table.sortby = "Peminjam"
        print(table)

#======================================================= searching =========================================================

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
            loading()
            return

        nama = str.capitalize(input("Masukkan nama yang ingin dicari: "))
        result = self.jump_search(nama)
        if result is not None:
            table = PrettyTable()
            table.field_names = ["Peminjam", "Mobil", "Tanggal pesan", "Tanggal kembali"]
            table.add_row([result["peminjam"], result["mobil"], result["tanggal pesan"], result["tanggal kembali"]])
            print(table)
            input ("")
        else:
            print("Nama tidak ditemukan")
            loading()
    
    def history (self):
        data = []
        for x in riwayat.find({}):
            data.append(x)
        t = PrettyTable(["Keterangan", "Peminjam", "Mobil", "Tanggal pesan", "Tangal kembali"])
        t.title = "Riwayat"
        for i in data:
            t.add_row([i["keterangan"], i["peminjam"], i["mobil"], i["tanggal pesan"], i["tanggal kembali"]])
        print(t)

#========================================================= program =================================================================
def loading():
    animation = "|/-\\"
    for i in range(15):
        time.sleep(0.1)
        print("Loading " + animation[i % len(animation)], end="\r")

def login():
    while True:
        os.system ("cls")
        print("==================================")
        print("|          11 Rent Car           |")
        print("==================================")
        print("| 1. Admin                       |")
        print("| 2. Pembeli                     |")
        print("| 3. Exit                        |")
        print("==================================")
        pilih = str(input("Masukkan Pilihan : "))
        if pilih == "1":
            while True:
                os.system ("cls")
                print("==================================")
                print("|            L O G I N           |")
                print("==================================")
                username = str.capitalize(input("Masukkan Username : "))
                pw = str.lower(pwinput.pwinput("Masukkan Password : "))
                loading()
                result = akun_admin.find_one({"admin": username, "pass": pw})
                if result and result["admin"] == username and result["pass"] == pw:
                    print("Login Berhasil!")
                    time.sleep (1)
                    admin()
                elif result is None:
                    print("Login Gagal!")
                    time.sleep (1)
                else:
                    print("Login Gagal!")
                    time.sleep (1)

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
                    while True:
                        os.system ("cls")
                        print("==================================")
                        print("|            L O G I N           |")
                        print("==================================")
                        username = str.capitalize(input("Masukkan Username : "))
                        pw = str.lower(pwinput.pwinput("Masukkan Password : "))
                        loading()
                        result = akun_pembeli.find_one({"pembeli": username, "pass": pw})
                        if result and result["pembeli"] == username and result["pass"] == pw:
                            print("Login Berhasil!")
                            time.sleep (1)
                            pembeli()
                        elif result is None:
                            print("Login Gagal!")
                            time.sleep (1)
                        else:
                            print("Login Gagal!")
                            time.sleep (1)
                elif pilih == "2":
                        while True:
                            os.system ("cls")
                            print("==================================")
                            print("|       R E G I S T R A S I      |")
                            print("==================================")
                            username_baru = str.capitalize(input("Masukkan username baru: "))
                            loading()
                            cek = akun_pembeli.find_one({"pembeli": username_baru})
                            if cek is not None:
                                print("Nama telah digunakan!")
                                time.sleep (1)
                            else:
                                password_baru = str.lower(input("Masukkan password baru: "))
                                akun_pembeli.insert_one({"pembeli": username_baru, "pass": password_baru})
                                print("Registrasi Berhasil!")
                                time.sleep (1)
                else:
                    print("Pilihan tidak tersedia!")
                    time.sleep (1)
        else:
            print("Pilihan tidak tersedia!")
            time.sleep (1)
                
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
        loading()
        if pilih == "1":
            while True:
                os.system("cls")
                print ("=============================================")
                print ("|               S O R T I N G               |")
                print ("=============================================")
                print ("|1. Berdasarkan Nama                        |")
                print ("|2. Berdasarkan Tanggal pesan               |")
                print ("|3. Berdasarkan Tanggal kembali             |")
                print ("|4. Kembali Ke Menu                         |")
                print ("=============================================")
                choose = str(input("Tentukan Pilihan : "))
                loading()
                if choose == "1":
                    RentalMobil().pengurutan_nama()
                    os.system("pause")
                elif choose == "2":
                    RentalMobil().pengurutan_pes()
                    os.system("pause")
                elif choose == "3":
                    RentalMobil().pengurutan_kem()
                    os.system("pause")
                elif choose == "4":
                    break
                else:
                    print ("Pilihan tidak tersedia!")
                    time.sleep (1)
        elif pilih == "2":
            RentalMobil().delete()
        elif pilih == "3":
            RentalMobil().history()
            os.system("pause")
        elif pilih == "4":
            RentalMobil().search()
        elif pilih == "5":
            login()
        else:
            print ("Pilihan Salah")
            time.sleep(1)

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
        loading()
        if pilih == "1":
            RentalMobil().nowcardata_user()
            time.sleep (1)
        elif pilih == "2":
            RentalMobil().newdata()
        elif pilih == "3":
            login()
        else:
            print ("Pilihan tidak tersedia!")
            time.sleep(1)
#login
login()
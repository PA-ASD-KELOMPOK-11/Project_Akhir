#Nama       : M. Haiqal Akbar Pratama Wahyudi
#NIM        : 2209116002
#Pratikum   : A1

from prettytable import PrettyTable
lisamotor = PrettyTable (['No','Motor','Harga Motor','Stock Barang'])

akun = {" User " : ["Bos","Pembeli"],
        " Passw " : ["Haiqal"]}

datamotor = {"Jmotor" : ["Suzuki Hayabusa","Kawasaki Ninja ZX-25R","Honda PCX 160cc", "Honda Vario 150cc", "Honda Beat"],
            "Harga Motor" : ["400000000", "102000000", "31000000", "26000000", "15000000"],
            "Stock Barang" : ["1", "2", "4", "7", "10"]}

def hakboss():
    print (" 1. Tambah Jenis Motor ")
    print (" 2. Tampilkan Data Saat ini ")
    print (" 3. Ubah Data Motor ")
    print (" 4. Hapus Data Motor ")

def tambahJmotor():
    Mbaru = input ("Tambah Motor Baru \t: ")
    Hmbaru = input ("Harga Baru \t\t: ")
    Smbaru = input ("Stock Baru \t\t: ")
    datamotor ["Jmotor"].append(Mbaru)
    datamotor ["Harga Motor"].append(Hmbaru)
    datamotor ["Stock Barang"].append(Smbaru)

def tampilkanDmotor():
    lisamotor.clear_rows()
    no = 1
    for i in range(len(datamotor.get("Jmotor"))):
        lisamotor.add_row([no, datamotor.get("Jmotor")[i],datamotor.get("Harga Motor")[i],datamotor.get("Stock Barang")[i]])
        no += 1

def ubahDmotor():
    tampilkanDmotor()
    print (lisamotor)
    pilihDmotor=int(input("Pilih Data Motor Yang Ingin Diubah : "))
    datamotor ["Jmotor"].pop(pilihDmotor-1)
    datamotor ["Harga Motor"].pop(pilihDmotor-1)
    datamotor ["Stock Barang"].pop(pilihDmotor-1)
    gantimotor = input ("Masukkan Motor Baru : ")
    gantiharga = input ("Masukkan Harga Motor : ")
    gantistock = input ("Masukkan Stock Barang : ")
    datamotor ["Jmotor"].insert(pilihDmotor-1,gantimotor)
    datamotor ["Harga Motor"].insert(pilihDmotor-1,gantiharga)
    datamotor ["Stock Barang"].insert(pilihDmotor-1,gantistock)    

def hapusDmotor():
    tampilkanDmotor()
    print (lisamotor)
    hapus = int(input("Pilih Data Motor Yang Ingin Dihapus : "))
    datamotor ["Jmotor"].pop(hapus-1)
    datamotor ["Harga Motor"].pop(hapus-1)
    datamotor ["Stock Barang"].pop(hapus-1)

while True:
    posisi = input(" Masukkan User \t\t: ")
    try:
        temukan = akun.get(" User ").index (posisi)
        if akun.get(" User ")[temukan]=="Bos":
            pw = input (" Masukkan Password \t: ")
            if posisi == akun.get(" User ")[temukan] and pw == akun.get(" Passw ")[temukan]:
                hakboss()
                while True:
                    bospilih = int(input (" Hai Bos Haiqal, Apa Yang Ingin Anda Lakukan Bos? (1/2/3/4) : "))
                    if bospilih == 1:
                        tambahJmotor()
                        tampilkanDmotor()
                        print (lisamotor)
                        break
                    elif bospilih == 2:
                        tampilkanDmotor()
                        print (lisamotor)
                        break
                    elif bospilih == 3:
                        ubahDmotor()
                        tampilkanDmotor()
                        print (lisamotor)
                        break
                    elif bospilih == 4:
                        hapusDmotor()
                        tampilkanDmotor()
                        print (lisamotor)
                        break
                    else:
                        print (" Maaf Bos, Pilihan Anda Salah ")
            else:
                print (" Password Yang Anda Masukan SALAH ")
        else:
            if posisi == akun.get(" User ")[temukan]:
                tampilkanDmotor()
                print (lisamotor)
                print (" Hi, Selamat Datang Di Dealer Motor Kami ")
                buymotor = input (" Silahkan Pilih Motor Yang Ingin Dibeli \t\t: ")
                banyakmotor = input (" Berapa Banyak Anda Ingin Membeli Motor Tersebut? \t: ")
                rumusbemotor = int(buymotor)-1
                tbayar = int (banyakmotor) * int (datamotor.get("Harga Motor")[int(rumusbemotor)])
                print (f" Total Harga \t\t\t\t\t\t= {tbayar} ")
                rumusbemotor = int (buymotor)-1
                kasiduit = input (" MasukKan Uang Anda \t\t\t\t\t: ")
                if int(kasiduit)<int(tbayar):
                    print (" Maaf, Uang Anda Kurang Untuk Membeli Motor Tersebut ")
                elif int(kasiduit)==int(tbayar):
                    print (" Uang Anda Pas, Silahkan Menikmati Motor Baru Anda ")
                else:
                    duitbalik = int(kasiduit)-int(tbayar)
                    print (f" Ini Uang Kembalian Anda ({duitbalik}), Silahkan Menikmati Motor Baru Anda ")
                break  
    except ValueError:
        print (" Maaf User Tidak Ada ")
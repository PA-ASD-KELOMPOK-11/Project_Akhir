# Project_Akhir

# PROGRAM RENTAL MOBIL

## Nama Kelompok
- M. Haiqal Akbar Pratama Wahyudi (2209116002)
- Silva Jen Retno (2209116019)
- Rikad Anggoro Putra (2209116044)

## Deskripsi Program
Rental Mobil merupakan penyedia layanan penyewaan mobil dengan cara sewa harian lepas kunci. Program ini mencakup fitur seperti pengelolaan pelanggan, system pemesanan pada sewa mobil. Program ini memudahkan pemilik bisnis rental mobil mengelola operasi mereka dan juga meningkatkan efisiensi operasional. 
Berikut merupakan tujuan dari program rental mobil yaitu:
1.	Memberikan pelayanan yang lebih baik kepada pelanggan dengan memberikan informasi yang lebih akurat.
2.	Mengelola inventaris rental mobil dengan lebih efektif dan efisien.

## Struktur Projek

### Library
1.	Import time, yaitu modul yang menyediakan berbagai fungsi yang berhubungan dengan waktu.
2.	Import os yaitu modul yang menyediakan cara portebel untuk menggunakan fungsionalitas yang bergantung pada system operasi.
3.	From prettytable import PrettyTable yaitu pustaka atau library dalam Python yang digunakan untuk membuat atau mengeluarkan data dalam bentuk tabel.   
4.	From pymongo import MongoClient yaitu library yang memungkinkan pengembang membuat koneksi antara aplikasi python  dan MongoDB untuk mengelola data dalam Database NoSQL. Mongo DB sendiri ialah program basis data NoSQL sumber terbuka yang merupakan basis data berorintasi dokumen lintas platform.   
5.	Import datetime adalah modul untuk memanipuasi tanggal dan waktu.
6.	Import math adalah modul yang menyediakan fungsi-fungsi matematika dasar untuk digunakan pada operasi  matematika sederhana. 
7.	Import pwinput yaitu modul python yang menampilkan **** untuk input kata sandi.

### Linked List
- Class Daftar
- Class Rental Mobil

**Fungsi dalam class Rental Mobil : **
-	Append
-	Newdata 
-	Newcardata_admin
-	Nowcardata_user
-	Delete 
-	mergesShort_pes
-	pengurutan_pes
-	mergesShort_kem
-	pengurutan_kem
-	mergesShort_nama
-	pengurutan_nama
-	jump_search
-	search
-	history

### Fungsi
-	def loading
-	def login
-	def admin
-	def pembeli

## Fitur
1. pembeli
- Registrasi pembeli
- Login pembeli
- Melihat daftar mobil
- Membuat pesanan
2. Admin
- Login admin
- Tampilkan Data 
- Hapus Data Rental
- Riwayat Peminjaman Mobil
- Cari Data Pesanan

## Fungsionalitas
1.	Pembeli dapat melakukan registrasi agar mendapatkan akun untuk masuk kedalam program.
2.	Pembeli dapat masuk kedalam program dengan menggunakan akun yang dimiliki saat login.
3.	Pembeli dapat melihat daftar mobil dan membuat pesanan.
4.	Admin telah memiliki akun yang dapat digunakan untuk masuk ke dalam program.
5.	Admin dapat menampilkan data,  menghapus data, melihat history dan mencari data pesanan.
6.	Pada menu “Tampilkan Data”, admin dapat mengurutkan data pada program berdasarkan nama pembeli, berdasarkan tanggal pesan dan berdasarkan tanggal kembali.

## Cara Penggunaan

### Menu Awal
Pada saat program pertama kali dijalankan maka akan muncul tampilan awal yang berisi 3 pilihan yaitu admin, pembeli, dan exit

![gambar 1](output/menu%20awal.png)

### Pembeli
#### Registrasi Pembeli
Jika pada menu awal pengguna memilih opsi pembeli maka tampilan selanjutnya yaitu berupa registrasi dan login. Apabila pembeli belum memiliki akun maka pembeli dapat melakukan registrasi terlebih dahulu. Pada menu ini pembeli diminta untuk memasukkan username dan password.

![gambar 2](output/registrasi%20pembeli.png)

Setelah melakukan registrasi akun program akan kembeli ke menu awal dan pembeli pun dapat login untuk masuk ke dalam program.

#### Login Pembeli
Pada menu ini pembeli akan diminta untuk memasukkan username dan password untuk bisa masuk kedalam program.

![gambar 3](output/login%20pembeli%20berhasil.png)

Jika pembeli salah dalam memasukkan username dan password maka program akan kembali pada menu sebelumnya.

![gambar 4](output/login%20pembeli%20gagal.png)

Jika pembeli telah berhasil login, maka program akan memunculkan 3 menu pelanggan yang berisi , Lihat Daftar Mobil, Buat Pesanan dan Exit.

![gambar 5](output/menu%202%20pembeli.png)

1. Lihat Daftar Mobil
    Jika pembeli memilih opsi pertama, maka pembeli dapat melihat daftar mobil yang tersedia pada program.

    ![gambar 6](output/lihat%20daftar%20mobil(pembeli).png)

2. Buat Pesanan
    Pada menu ini pembeli dapat membuat pesanan dan akan diminta untuk memasukkan nama peminjam, jenis mobil yang akan di sewa, dan kemudian jumlah hari peminjaman.

    ![gambar 7](output/buat%20pesanan(pembeli).png)

3. Exit
    Jika pembeli telah berhasil melakukan penyewaan dan telah selesai, pembeli dapat memilih opsi “exit” untuk keluar dari program.

### Admin
#### Login Admin
Pada saat program di jalankan, dan pada menu awal memilih opsi pertama yaitu admin, maka admin akan langsung diminta memasukkan username dan password untuk login.

![gambar 8](output/login%20admin%20berhasil.png)

Jika admin salah dalam memasukkan username atau password maka program akan Kembali ke menu sebelumnya.

![gambar 9](output/login%20admin%20gagal.png)

Jika pembeli telah berhasil login, maka program akan memunculkan 5 menu admin yang berisi Tampilkan Data, Hapus Data Rental, Riwayat Peminjaman Mobil, Cari Data Pesanan, dan Log Out pada menu kelima.

![gambar 10](output/menu%201%20admin.png)

1. Tampilkan Data
    Pada menu ini, admin akan Kembali diberikan beberapa menu untuk melihat data rental pada program, yaitu berupa pengurutan data atau sorting berdasarkan nama, berdasarkan tanggal mobil pesan, dan berdasarkan tanggal mobil kembali.

    ![gambar 11](output/Tampilkan%20Data%20(admin).png)

    a.	Berdasarkan Nama
    Data yang ditampilkan akan terurut berdasarkan nama pembeli.

    ![gambar 12](output/sorting%20berdasarkan%20nama.png)

    b.	Berdasarkan Tanggal Pesan
    Data yang ditampilkan akan terurut berdasarkan tanggal mobil di pesan.

    ![gambar 13](output/sorting%20berdasarkan%20tanggal%20pesan.png)

    c.	Berdasarkan Tanggal Kembali 
    Data yang ditampilkan akan terurut berdasarkan tanggal mobil kembali setelah dipesan.

    ![gambar 14](output/sorting%20berdasarkan%20tanggal%20kembali.png)

2. Hapus Data Rental
    Untuk menghapus data pada program, admin dapat memilih opsi kedua yaitu Hapus Data Rental. Kemudian, admin akan diminta untuk menginputkan nama pembeli yang ingin di hapus.

    ![gambar 15](output/berhasil%20menghapus%20pesanan.png)

    Ketika admin salah atau keliru saat menginput nama saat menghapus data

    ![gambar 16](output/gagal%20menghapus%20pesanan.png)

    Sebelum data dengan nama peminjam “Logan” di hapus

    ![gambar 17](output/sorting%20berdasarkan%20nama.png)

    Sesudah data dengan nama peminjam “Logan” di hapus

    ![gambar 18](output/data%20setelah%20dihapus%20(admin).png)

3. Riwayat Peminjaman Mobil
    Menu ini merupakan history atau seluruh data rental mobil pada program baik yang baru ditambahkan maupun yang sudah dihapus.

    ![gambar 19](output/riwayat%20pemesanan%20mobil.png)

4. Cari Data Pemesan
    Pada menu ke 4 yaitu Cari Data Pemesan, admin akan diminta untuk menginputkan nama pemesan yang ingin dicari.

    ![gambar 20](output/cari%20data%20pesanan.png)

    Ketika admin salah atau keliru saat menginput nama saat mencari data

    ![gambar 21](output/gagal%20cari%20data%20pesanan.png)

5. Log Out
    Menu terakhir yaitu Log Out, untuk kembali pada menu sebelumnya.


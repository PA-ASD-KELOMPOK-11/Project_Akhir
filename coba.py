# from datetime import datetime, timedelta

# input_date = datetime.now()
# days_to_add = now + timedelta(days=1)

# # Mengubah input ke objek datetime
# date_obj = datetime.strptime(input_date, "%d-%B-%Y")

# # Menambahkan jumlah hari
# new_date = date_obj + timedelta(days=days_to_add)

# # Menampilkan hasil
# print("Tanggal baru setelah ditambahkan", days_to_add, "hari:", new_date.strftime('%Y-%m-%d'))

# now = datetime.now()
# new_date = now + timedelta(days=1)

# print("Tanggal sekarang:", now)
# print("Tanggal besok:", new_date)

# import datetime

# # dapatkan datetime saat ini
# now = datetime.datetime.now()

# # minta input dari pengguna
# jumlah_hari = int(input("Masukkan jumlah hari yang ingin ditambahkan: "))

# # tambahkan jumlah hari ke datetime saat ini
# tanggal_baru = now + datetime.timedelta(days=jumlah_hari)

# # tampilkan tanggal baru
# print("Tanggal setelah ditambahkan", jumlah_hari, "hari adalah:", tanggal_baru.strftime("%d-%B-%Y"))
txt = input("masukan nama :")

x = txt.title()

print(x)

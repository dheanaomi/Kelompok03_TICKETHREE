import os
loop = True

#Memulai Program TICKETHREE
#Menampilkan program
tampilan = "Selamat Datang di Program TICKETHREE Aplikasi Pemesanan Tiket Konser Online"
s=tampilan.center(120, "=")
print(s)

#Menampilkan menu program TICKETHREE

print("Menu Program\t\t: ")
print("1. \t Menu Pembelian Tiket Konser")
print("2. \t Menu Pembatalan Tiket konser")
print("="*len(s))
print("")

#Menginputkan menu yang diinginkan
pilihan_menu = int(input("Ketik Menu Program\t:"))
if pilihan_menu == 1:
    print("Filter Konser Berdasarkan: ")
    print("\n==================================================")
    print("1. Genre")
    print("2. Artis")
    print("3. Kota")
    print("4. Harga")
    filter = input("Pilih Filter Yang Anda Inginkan: ")
    print("\n==================================================")
    if filter == "1":
         print("\n==================================================")
         print("Menampilkan Hasil Pencarian Berdasarkan Genre :")
         print("1. EDM")
         print("2. Indie")
         print("3. Jazz")
         print("4. Pop")
         genre = input("Masukkan Nomor Genre Yang Anda Inginkan : ")
         print("\n==================================================")
         if genre == "1":
            print("\n===========================================================")
            print("Nama Acara  : We The Fest")
            print("Nama Artis  : Dipha Barus")
            print("              Weird Genius")
            print("              Roni & Joni")
            print("              Cyda")
            print("Hari,Tanggal: Jumat, 11 Juni 2021 ")
            print("Kota        : Medan")
            print("Tempat      : Pendopo Rumah Dinas Gubernur Sumatra Utara Jln. Jendral Sudirman")
            print("Genre       : EDM")
            print("Harga Tiket : Rp 1.200.000,00")
            print("Status      : Tersisa >100")
            print("\n============================================================")
         elif genre == "2":
            print("\n===========================================================")
            print("Nama Acara  : Indigo Fest")
            print("Nama Artis  : Fourtwenty")
            print("              Burgerkill")
            print("              Bottlesmoker")
            print("              Mocca")
            print("Hari,Tanggal: Minggu, 20 Juni 2021 ")
            print("Kota        : Riau")
            print("Tempat      : Kompleks Bandar Seni Raja Ali Haji Purna")
            print("Genre       : Indie")
            print("Harga Tiket : Rp 1.300.000,00")
            print("Status      : Tersisa <100")
            print("\n============================================================")
         elif genre == "3":
            print("\n===========================================================")
            print("Nama Acara  : Java Jazz Fest")
            print("Nama Artis  : Tulus")
            print("              Indra Lesmana")
            print("              Maliq & D'Essentials")
            print("              Andien")
            print("Hari,Tanggal: Senin, 28 Juni 2021 ")
            print("Kota        : Surabaya")
            print("Tempat      : Tunjungan Plaza Convention Center")
            print("Genre       : Jazz")
            print("Harga Tiket : Rp 1.500.000,00")
            print("Status      : Tersisa <100")
            print("\n============================================================")
         else:
            print("\n===========================================================")
            print("Nama Acara  : Lalala Fest")
            print("Nama Artis  : Ardhito Pramono")
            print("              Isyana Sarasvati")
            print("              Yura Yunita")
            print("              Crush")
            print("Hari,Tanggal: Sabtu, 5 Juni 2021 ")
            print("Kota        : Jakarta")
            print("Tempat      : Aula Simfonia 81 Jln. Industri Raya Blok B14")
            print("Genre       : Pop")
            print("Harga Tiket : Rp 500.000,00")
            print("Status      : Tersisa >100")
            print("\n============================================================")
    elif filter == "2":
        print("\n==================================================")
        print("Menampilkan Hasil Pencarian Berdasarkan Nama Artis :")
        print("1. Ardhito Pramono")
        print("2. Dipha Barus")
        print("3. Fourtwenty")
        print("4. Tulus")
        artis = input("Masukkan Nomor Artis Yang Anda Inginkan : ")
        print("\n==================================================")
        if artis == "1":
            print("\n===========================================================")
            print("Nama Acara  : Lalala Fest")
            print("Nama Artis  : Ardhito Pramono")
            print("              Isyana Sarasvati")
            print("              Yura Yunita")
            print("              Crush")
            print("Hari,Tanggal: Sabtu, 5 Juni 2021 ")
            print("Kota        : Jakarta")
            print("Tempat      : Aula Simfonia 81 Jln. Industri Raya Blok B14")
            print("Genre       : Pop")
            print("Harga Tiket : Rp 500.000,00")
            print("Status      : Tersisa >100")
            print("\n============================================================")
        elif artis == "2":
            print("\n===========================================================")
            print("Nama Acara  : We The Fest")
            print("Nama Artis  : Dipha Barus")
            print("              Weird Genius")
            print("              Roni & Joni")
            print("              Cyda")
            print("Hari,Tanggal: Jumat, 11 Juni 2021 ")
            print("Kota        : Medan")
            print("Tempat      : Pendopo Rumah Dinas Gubernur Sumatra Utara Jln. Jendral Sudirman")
            print("Genre       : EDM")
            print("Harga Tiket : Rp 1.200.000,00")
            print("Status      : Tersisa >100")
            print("\n============================================================")
        elif artis == "3":
            print("\n===========================================================")
            print("Nama Acara  : Indigo Fest")
            print("Nama Artis  : Fourtwenty")
            print("              Burgerkill")
            print("              Bottlesmoker")
            print("              Mocca")
            print("Hari,Tanggal: Minggu, 20 Juni 2021 ")
            print("Kota        : Riau")
            print("Tempat      : Kompleks Bandar Seni Raja Ali Haji Purna")
            print("Genre       : Indie")
            print("Harga Tiket : Rp 1.300.000,00")
            print("Status      : Tersisa <100")
            print("\n============================================================")
        else:
            print("\n===========================================================")
            print("Nama Acara  : Java Jazz Fest")
            print("Nama Artis  : Tulus")
            print("              Indra Lesmana")
            print("              Maliq & D'Essentials")
            print("              Andien")
            print("Hari,Tanggal: Senin, 28 Juni 2021 ")
            print("Kota        : Surabaya")
            print("Tempat      : Tunjungan Plaza Convention Center")
            print("Genre       : Jazz")
            print("Harga Tiket : Rp 1.500.000,00")
            print("Status      : Tersisa <100")
            print("\n============================================================")
    elif filter == "3":
        print("\n==================================================")
        print("Menampilkan Hasil Pencarian Berdasarkan Nama Kota:")
        print("1. Jakarta")
        print("2. Medan")
        print("3. Riau")
        print("4. Surabaya")
        kota = input("Masukkan Nomor Kota Yang Anda Inginkan : ")
        print("\n==================================================")
        if kota == "1":
            print("\n===========================================================")
            print("Nama Acara  : Lalala Fest")
            print("Nama Artis  : Ardhito Pramono")
            print("              Isyana Sarasvati")
            print("              Yura Yunita")
            print("              Crush")
            print("Hari,Tanggal: Sabtu, 5 Juni 2021 ")
            print("Kota        : Jakarta")
            print("Tempat      : Aula Simfonia 81 Jln. Industri Raya Blok B14")
            print("Genre       : Pop")
            print("Harga Tiket : Rp 500.000,00")
            print("Status      : Tersisa >100")
            print("\n============================================================")
        elif kota == "2":
            print("\n===========================================================")
            print("Nama Acara  : We The Fest")
            print("Nama Artis  : Dipha Barus")
            print("              Weird Genius")
            print("              Roni & Joni")
            print("              Cyda")
            print("Hari,Tanggal: Jumat, 11 Juni 2021 ")
            print("Kota        : Medan")
            print("Tempat      : Pendopo Rumah Dinas Gubernur Sumatra Utara Jln. Jendral Sudirman")
            print("Genre       : EDM")
            print("Harga Tiket : Rp 1.200.000,00")
            print("Status      : Tersisa >100")
            print("\n============================================================")
        elif kota == "3":
            print("\n===========================================================")
            print("Nama Acara  : Indigo Fest")
            print("Nama Artis  : Fourtwenty")
            print("              Burgerkill")
            print("              Bottlesmoker")
            print("              Mocca")
            print("Hari,Tanggal: Minggu, 20 Juni 2021 ")
            print("Kota        : Riau")
            print("Tempat      : Kompleks Bandar Seni Raja Ali Haji Purna")
            print("Genre       : Indie")
            print("Harga Tiket : Rp 1.300.000,00")
            print("Status      : Tersisa <100")
            print("\n============================================================")
        else:
            print("\n===========================================================")
            print("Nama Acara  : Java Jazz Fest")
            print("Nama Artis  : Tulus")
            print("              Indra Lesmana")
            print("              Maliq & D'Essentials")
            print("              Andien")
            print("Hari,Tanggal: Senin, 28 Juni 2021 ")
            print("Kota        : Surabaya")
            print("Tempat      : Tunjungan Plaza Convention Center")
            print("Genre       : Jazz")
            print("Harga Tiket : Rp 1.500.000,00")
            print("Status      : Tersisa <100")
            print("\n============================================================")
    else:
        print("\n==================================================")
        print("Silahkan Pilih Pencarian Berdasarkan Harga Tertinggi/Terendah:")
        print("1. Tertinggi->")
        print("2. Terendah<-")
        m = input("Masukkan Nomor Yang Anda Inginkan : ")
        print("\n==================================================")
        if m == "1":
            print("\n==================================================")
            print("Menampilkan Hasil Pencarian Berdasarkan Harga Tertinggi:")
            print("1. Rp 1.500.000,00")
            print("2. Rp 1.300.000,00")
            print("3. Rp 1.200.000,00")
            print("4. Rp   500.000,00")
            harga1 = input("Masukkan Nomor Yang Anda Inginkan : ")
            print("\n==================================================")
            if harga1==  "1":
                print("\n===========================================================")
                print("Nama Acara  : Java Jazz Fest")
                print("Nama Artis  : Tulus")
                print("              Indra Lesmana")
                print("              Maliq & D'Essentials")
                print("              Andien")
                print("Hari,Tanggal: Senin, 28 Juni 2021 ")
                print("Kota        : Surabaya")
                print("Tempat      : Tunjungan Plaza Convention Center")
                print("Genre       : Jazz")
                print("Harga Tiket : Rp 1.500.000,00")
                print("Status      : Tersisa <100")
                print("\n============================================================")
            elif harga1 =="2":
                print("\n===========================================================")
                print("Nama Acara  : Indigo Fest")
                print("Nama Artis  : Fourtwenty")
                print("              Burgerkill")
                print("              Bottlesmoker")
                print("              Mocca")
                print("Hari,Tanggal: Minggu, 20 Juni 2021 ")
                print("Kota        : Riau")
                print("Tempat      : Kompleks Bandar Seni Raja Ali Haji Purna")
                print("Genre       : Indie")
                print("Harga Tiket : Rp 1.300.000,00")
                print("Status      : Tersisa <100")
                print("\n============================================================")
            elif harga1 =="3":
                print("\n===========================================================")
                print("Nama Acara  : We The Fest")
                print("Nama Artis  : Dipha Barus")
                print("              Weird Genius")
                print("              Roni & Joni")
                print("              Cyda")
                print("Hari,Tanggal: Jumat, 11 Juni 2021 ")
                print("Kota        : Medan")
                print("Tempat      : Pendopo Rumah Dinas Gubernur Sumatra Utara Jln. Jendral Sudirman")
                print("Genre       : EDM")
                print("Harga Tiket : Rp 1.200.000,00")
                print("Status      : Tersisa >100")
                print("\n============================================================")
            else:
                print("\n===========================================================")
                print("Nama Acara  : Lalala Fest")
                print("Nama Artis  : Ardhito Pramono")
                print("              Isyana Sarasvati")
                print("              Yura Yunita")
                print("              Crush")
                print("Hari,Tanggal: Sabtu, 5 Juni 2021 ")
                print("Kota        : Jakarta")
                print("Tempat      : Aula Simfonia 81 Jln. Industri Raya Blok B14")
                print("Genre       : Pop")
                print("Harga Tiket : Rp 500.000,00")
                print("Status      : Tersisa >100")
                print("\n============================================================")
        else:
            print("\n==================================================")
            print("Menampilkan Hasil Pencarian Berdasarkan Harga Terendah:")
            print("1. Rp   500.000,00")
            print("2. Rp 1.200.000,00")
            print("3. Rp 1.300.000,00")
            print("4. Rp 1.500.000,00")
            harga2 = input("Masukkan Nomor Yang Anda Inginkan : ")
            print("\n==================================================")
            if harga2 == "1":
                print("\n===========================================================")
                print("Nama Acara  : Lalala Fest")
                print("Nama Artis  : Ardhito Pramono")
                print("              Isyana Sarasvati")
                print("              Yura Yunita")
                print("              Crush")
                print("Hari,Tanggal: Sabtu, 5 Juni 2021 ")
                print("Kota        : Jakarta")
                print("Tempat      : Aula Simfonia 81 Jln. Industri Raya Blok B14")
                print("Genre       : Pop")
                print("Harga Tiket : Rp 500.000,00")
                print("Status      : Tersisa >100")
                print("\n============================================================")
            elif harga2 == "2":
                print("\n===========================================================")
                print("Nama Acara  : We The Fest")
                print("Nama Artis  : Dipha Barus")
                print("              Weird Genius")
                print("              Roni & Joni")
                print("              Cyda")
                print("Hari,Tanggal: Jumat, 11 Juni 2021 ")
                print("Kota        : Medan")
                print("Tempat      : Pendopo Rumah Dinas Gubernur Sumatra Utara Jln. Jendral Sudirman")
                print("Genre       : EDM")
                print("Harga Tiket : Rp 1.200.000,00")
                print("Status      : Tersisa >100")
                print("\n============================================================")
            elif harga2 == "3":
                print("\n===========================================================")
                print("Nama Acara  : Indigo Fest")
                print("Nama Artis  : Fourtwenty")
                print("              Burgerkill")
                print("              Bottlesmoker")
                print("              Mocca")
                print("Hari,Tanggal: Minggu, 20 Juni 2021 ")
                print("Kota        : Riau")
                print("Tempat      : Kompleks Bandar Seni Raja Ali Haji Purna")
                print("Genre       : Indie")
                print("Harga Tiket : Rp 1.300.000,00")
                print("Status      : Tersisa <100")
                print("\n============================================================")
            else:
                print("\n===========================================================")
                print("Nama Acara  : Java Jazz Fest")
                print("Nama Artis  : Tulus")
                print("              Indra Lesmana")
                print("              Maliq & D'Essentials")
                print("              Andien")
                print("Hari,Tanggal: Senin, 28 Juni 2021 ")
                print("Kota        : Surabaya")
                print("Tempat      : Tunjungan Plaza Convention Center")
                print("Genre       : Jazz")
                print("Harga Tiket : Rp 1.500.000,00")
                print("Status      : Tersisa <100")
                print("\n============================================================")

#Pilihan Pembatalan Tiket
else:
    proses_pembatalan= input("Masukkan Kode Unik Tiket Anda: ")
    print(proses_pembatalan)
    konfirm_batal= input("Apakah anda sudah yakin melakukan pembatalan?(Y/T):")
    if konfirm_batal.upper()=="Y":
        print("Tiket Anda Telah Dibatalkan, Refund akan dikirim melalui metode pembayaran dengan potongan 20%")

    else:
       exit()

#pemesanan tiket
biaya_adm = 3000

num_array = list()
banyak_tiket = int(input("Masukkan jumlah tiket yang ingin dipesan : "))
print("Nasukan nama Pemesan : ")
for i in range(int(banyak_tiket)):
    i += 1
    n = input("Nama orang ke {} :".format(i))
    num_array.append(str(n))
print("Masukkan nomor telepon :")
for i in range(int(banyak_tiket)):
    i += 1
    n = input("No telepon orang ke {} :".format(i))
    num_array.append(str(n))
print("Masukkan email:")
for i in range(int(banyak_tiket)):
    i += 1
    n = input("Email orang ke  {} :".format(i))
    num_array.append(str(n))
print("Masukkan No KTP :")
for i in range(int(banyak_tiket)):
    i += 1
    n = input("No KTP orang ke  {} :".format(i))
    num_array.append(str(n))
print("Masukkan Usia :")
for i in range(int(banyak_tiket)):
    i += 1
    n = input("Usia orang ke{} :".format(i))
    num_array.append(str(n))
total_biaya = banyak_tiket * harga_tiket * 0.05 + biaya_adm
os.system('cls')
print("\n----------------------------------------------")
print("Anda telah berhasil melakukan pembelian tiket ")
print("----------------------------------------------")
print("Nama Pemesan :".format(len(num_array)))
for a in num_array:
    print(("- {}").format(a))
print("Total Harga", "Rp.", (total_biaya))

# informasi paket dan promo tiap bank
promo_BNI = 0.03
promo_Mandiri = 0.025
promo_BCA = 0.025
promo_shopeepay = 0.3
promo_gopay = 0.3
paket1 = 15000
paket2 = 85000
paket3 = 110000

# PROGRAM PEMBELIAN MERCHANDISE
print('\n Disini kami menyediakan paket merchandise eksklusif untuk memeriahkan konser yang Anda pilih\n')
merchandise = int(input(
    """ 1. Lighstick\n 2. Lighstick + kaos\n 3. Lightstick + kaos + topi\n 
    Apakah Anda akan membeli paket merchandise?\n 
    (Jika iya ketik 1, Jika tidak ketik 2) \n """))

if merchandise == 1:
    paket = str(
        input(""" 1. Lighstick\n 2. Lighstick + kaos\n 3. Lightstick + kaos + topi\n
             Silahkan pilih 1, 2, atau 3 :\n"""))
    if paket == '1':
        biaya1 = total_biaya + paket1
        print('Total biaya = ', biaya1)

    elif paket == '2':
        biaya1 = total_biaya +  paket2
        print('Total biaya = ', biaya1)

    else:
        biaya1 = total_biaya +  paket3
        print('Total biaya = ', biaya1)


else:
    biaya1 = total_biaya 
    print('Total biaya = ', biaya1)


# Memunculkan kode transaksi
import random

bil = random.randint(999999, 9999999)
kode_unik = random.randint(99, 9999)
print("------------ Kode transaksi Anda ------------\n",
      "\n------------------ ", bil, " ------------------ ", 
    "\n\nSilahkan lakukan pembayaran dengan kode tersebut\n")

bayar = int(input("Silahkan masukkan kode transaksi untuk melakukan pembayaran:\n"))
if bayar == bil :
     print("\nSelamat! Transaksi sukses!\n")
else:
    print('Kode yang Anda masukkan salah! Silahkan coba lagi!\n')

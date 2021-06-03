from os import system
import time

# Memulai Program TICKETHREE
# Menampilkan program
tampilan = 'Selamat Datang di Program TICKETHREE Aplikasi Pemesanan Tiket Konser Online'
s = tampilan.center(120, "=")
print(s)

katalog_konser = {
    'Katalog_1': {'Nama Acara': 'We The Fest', 'Artis': 'Dipha Barus,Weird Genius,Roni & Joni,Cyda',
                  'Tanggal': 'Jumat, 11 Juni 2021', 'Kota': 'Medan',
                  'Tempat': 'Pendopo Rumah Dinas Gubernur Sumatra Utara Jln. Jendral Sudirman', 'Genre': 'EDM',
                  'Harga': 1200000, 'Status\t': '>100'},
    'Katalog_2': {'Nama Acara': 'Indigo Fest', 'Artis': 'Fourtwenty,Burgerkill,Bottlesmoker,Mocca',
                  'Tanggal': 'Minggu, 20 Juni 2021', 'Kota': 'Riau',
                  'Tempat': 'Kompleks Bandar Seni Raja Ali Haji Purna', 'Genre': 'Indie', 'Harga': 1300000,
                  'Status': '<100'},
    'Katalog_3': {'Nama Acara': 'Java Jazz Fest', 'Artis': 'Tulus,Indra Lesmana,Maliq & DEssentials,Andien',
                  'Tanggal': 'Senin, 28 Juni 2021', 'Kota': 'Surabaya', 'Tempat': 'Tunjungan Plaza Convention Center',
                  'Genre': 'Jazz', 'Harga': 1500000, 'Status': '<100'},
    'Katalog_4': {'Nama Acara': 'Lalala Fest', 'Artis': 'Ardhito Pramono,Isyana Sarasvati,Yura Yunita,Crush',
                  'Tanggal': 'Sabtu, 5 Juni 2021', 'Kota': 'Jakarta',
                  'Tempat': 'Aula Simfonia 81 Jln. Industri Raya Blok B14', 'Genre': 'Pop', 'Harga': 500000,
                  'Status': '>100'}
}

tamp = """\n======================================
Informasi Pemesanan Tiket Konser 'TICKETHREE'
======================================"""


def formatter(katalog):
    for key in katalog.keys():
        print(f"""{key}\t\t= {katalog[key]}""")


# Menampilkan menu program TICKETHREE
def mainmenu():
    print("""Menu Program\t\t: 
1.Menu Pembelian Tiket Konser
2.Menu Pembatalan Tiket konser""")
    v = '=' * len(s)
    print(v)
    # Menginputkan menu yang diinginkan
    pilihan_menu = int(input("Ketik Menu Program (1/2)\t:"))
    if pilihan_menu == 1:
        print("""
\n==================================================
Filter Konser Berdasarkan\t:
1. Genre
2. Artis
3. Kota
4. Harga
\n=================================================""")

        filter_pilihan = int(input("Ketik Filter Konser Yang Anda Inginkan (1/2/3/4)\t:"))

        # Berdasarkan Genre
        if filter_pilihan == 1:
            # Menampilkan list berdasar genre
            print("""
\n=================================================
List Konser Berdasar Genre:
1. EDM
2. Indie
3. Jazz
4. Pop
""")
            list_genre = int(input("Ketik List Konser Genre (1/2/3/4)\t: "))
            if list_genre == 1:
                print(tamp)
                for key in katalog_konser.keys():
                    if katalog_konser[key]['Genre'] == 'EDM':
                        current_harga = katalog_konser[key]['Harga']
                        print(formatter(katalog_konser[key]))

            elif list_genre == 2:
                print(tamp)
                for key in katalog_konser.keys():
                    if katalog_konser[key]['Genre'] == 'Indie':
                        current_harga = katalog_konser[key]['Harga']
                        print(formatter(katalog_konser[key]))

            elif list_genre == 3:
                print(tamp)
                for key in katalog_konser.keys():
                    if katalog_konser[key]['Genre'] == 'Jazz':
                        current_harga = katalog_konser[key]['Harga']
                        print(formatter(katalog_konser[key]))

            elif list_genre == 4:
                print(tamp)
                for key in katalog_konser.keys():
                    if katalog_konser[key]['Genre'] == 'Pop':
                        current_harga = katalog_konser[key]['Harga']
                        print(formatter(katalog_konser[key]))
            else:
                print("\nMaaf Pilihan yang Anda Masukkan Salah")

        # Berdasarkan Artis
        elif filter_pilihan == 2:
            # Menampilkan list berdasar artis
            print("""
\n================================================
List Konser Berdasar Artis:
1. Ardhito Pramono
2. Dipha Barus
3. Fourtwenty
4. Tulus
""")
            list_artis = int(input("Ketik List Konser Berdasar Artis (1/2/3/4)\t: "))
            if list_artis == 1:
                print(tamp)
                for key in katalog_konser.keys():
                    if katalog_konser[key]['Artis'][0] == 'Ardhito Pramono,Isyana Sarasvati,Yura Yunita,Crush':
                        current_harga = katalog_konser[key]['Harga']
                        print(formatter(katalog_konser[key]))
            elif list_artis == 2:
                print(tamp)
                for key in katalog_konser.keys():
                    if katalog_konser[key]['Artis'] == 'Dipha Barus,Weird Genius,Roni & Joni,Cyda':
                        current_harga = katalog_konser[key]['Harga']
                        print(formatter(katalog_konser[key]))
            elif list_artis == 3:
                print(tamp)
                for key in katalog_konser.keys():
                    if katalog_konser[key]['Artis'] == 'Fourtwenty,Burgerkill,Bottlesmoker,Mocca':
                        current_harga = katalog_konser[key]['Harga']
                        print(formatter(katalog_konser[key]))
            elif list_artis == 4:
                print(tamp)
                for key in katalog_konser.keys():
                    if katalog_konser[key]['Artis'] == 'Tulus,Indra Lesmana,Maliq & DEssentials,Andien':
                        current_harga = katalog_konser[key]['Harga']
                        print(formatter(katalog_konser[key]))
            else:
                print("\nMaaf Pilihan yang Anda Masukkan Salah")

        # Berdasarkan Kota
        elif filter_pilihan == 3:
            #Menampilkan list berdasar kota
            print(""" 
\n================================================
List Konser Berdasar Kota\t:
1. Jakarta
2. Medan
3. Riau
4. Surabaya
""")
            list_kota = int(input("Ketik List Konser Berdasar Kota (1/2/3/4)\t: "))
            if list_kota == 1:
                print(tamp)
                for key in katalog_konser.keys():
                    if katalog_konser[key]['Kota'] == 'Jakarta':
                        current_harga = katalog_konser[key]['Harga']
                        print(formatter(katalog_konser[key]))
            elif list_kota == 2:
                print(tamp)
                for key in katalog_konser.keys():
                    if katalog_konser[key]['Kota'] == 'Medan':
                        current_harga = katalog_konser[key]['Harga']
                        print(formatter(katalog_konser[key]))
            elif list_kota == 3:
                print(tamp)
                for key in katalog_konser.keys():
                    if katalog_konser[key]['Kota'] == 'Riau':
                        current_harga = katalog_konser[key]['Harga']
                        print(formatter(katalog_konser[key]))
            elif list_kota == 4:
                print(tamp)
                for key in katalog_konser.keys():
                    if katalog_konser[key]['Kota'] == 'Surabaya':
                        current_harga = katalog_konser[key]['Harga']
                        print(formatter(katalog_konser[key]))
            else:
                print("\nMaaf Pilihan yang Anda Masukkan Salah")

        # Berdasarkan Harga
        elif filter_pilihan == 4:
            #Menampilkan list berdasarkan harga
            print("""
\n================================================
Filter Harga Berdasarkan\t:
1. Tertinggi->Terendah
2. Terendah->Tertinggi
""")
            filter_harga = int(input("Ketik Filter Harga yang Anda Inginkan (1/2/3/4)\t: "))
            list_harga = []

            for key in katalog_konser.keys():
                list_harga.append(katalog_konser[key]['Harga'])

            if filter_harga == 1:
                list_harga.sort(reverse=True)

                print("List Harga Tiket Konser Dari Yang Tertinggi :")
                for i in range(0, len(list_harga)):
                    print('%d. %d' % (i+1, list_harga[i]))

                pilihan_harga = int(input("Masukkan Nomor Harga Yang Dipilih(1/2/3/4): "))
                if pilihan_harga == 1:
                    print(tamp)
                    for key in katalog_konser.keys():
                        if katalog_konser[key]['Harga'] == 1500000:
                            current_harga = katalog_konser[key]['Harga']
                            formatter(katalog_konser[key])
                elif pilihan_harga == 2:
                    print(tamp)
                    for key in katalog_konser.keys():
                        if katalog_konser[key]['Harga'] == 1300000:
                            current_harga = katalog_konser[key]['Harga']
                            formatter(katalog_konser[key])
                elif pilihan_harga == 3:
                    print(tamp)
                    for key in katalog_konser.keys():
                        if katalog_konser[key]['Harga'] == 1200000:
                            current_harga = katalog_konser[key]['Harga']
                            formatter(katalog_konser[key])
                elif pilihan_harga == 4:
                    print(tamp)
                    for key in katalog_konser.keys():
                        if katalog_konser[key]['Harga'] == 500000:
                            current_harga = katalog_konser[key]['Harga']
                            formatter(katalog_konser[key])
                else:
                    print("\nMaaf Pilihan yang Anda Masukkan Salah")


            elif filter_harga == 2:
                list_harga.sort()

                print("List Harga Tiket Konser Dari Yang Terendah :")
                for i in range(0, len(list_harga)):
                    print('%d. %d' % (i+1, list_harga[i]))

                pilihan_harga = int(input("Masukkan Nomor Harga Yang Dipilih(1/2/3/4): "))
                if pilihan_harga == 1:
                    print(tamp)
                    for key in katalog_konser.keys():
                        if katalog_konser[key]['Harga'] == 500000:
                            current_harga = katalog_konser[key]['Harga']
                            formatter(katalog_konser[key])
                elif pilihan_harga == 2:
                    print(tamp)
                    for key in katalog_konser.keys():
                        if katalog_konser[key]['Harga'] == 1200000:
                            current_harga = katalog_konser[key]['Harga']
                            formatter(katalog_konser[key])
                elif pilihan_harga == 3:
                    print(tamp)
                    for key in katalog_konser.keys():
                        if katalog_konser[key]['Harga'] == 1300000:
                            current_harga = katalog_konser[key]['Harga']
                            formatter(katalog_konser[key])
                elif pilihan_harga == 4:
                    print(tamp)
                    for key in katalog_konser.keys():
                        if katalog_konser[key]['Harga'] == 1500000:
                            current_harga = katalog_konser[key]['Harga']
                            formatter(katalog_konser[key])
                else:
                    print("\nMaaf Pilihan yang Anda Masukkan Salah")

            else:
                print("\nMaaf Pilihan yang Anda Masukkan Salah")


    #Menu pembatalan tiket
    elif pilihan_menu==2:
        proses_pembatalan = input("Masukkan Kode Unik Tiket Anda: ")
        list_kodeunik= list(proses_pembatalan)
        if len(list_kodeunik) ==7:
            konfirm_batal = input("Apakah anda sudah yakin melakukan pembatalan?(Y/T):")
            if konfirm_batal.upper() == "Y":
                print("\nTiket Anda Telah Dibatalkan, Refund akan dikirim melalui metode pembayaran dengan potongan 20%")
            else:
                mainmenu()
        else:
            print("\nMaaf Kode yang Anda Masukkan Salah\n")
            mainmenu()
    else:
        exit()
# pemesanan tiket
    syarat_ketentuan = ("Syarat dan ketentuan :" 
                       "\n1. Pembeli tiket yang akan menonton konser harus berusia 17 tahun keatas dan memiliki KTP." 
                       "\n2. Saat akan memasuki Acara pemegang tiket wajib menunjukkan KTP , serta menyertai bukti pembelian yang sah apabila diperlukan." 
                       "\n3. Anak-anak atau Anak-anak tanpa tiket tidak diizinkan memasuki Acara." 
                       "\n4. Setiap Pemegang Tiket yang memasuki Acara diwajibkan untuk patuh pada peraturan, ketentuan dan kondisi yang berlaku di Tempat Acara.")

    biaya_adm = 3000
    banyak_tiket = int(input("Masukkan jumlah tiket yang ingin dipesan : "))
    database = []
    print()

    for i in range(int(banyak_tiket)):
        print('biodata', i + 1)
        entry = {
            'nama': input('Nama: '),
            'telepon': input('Telepon: '),
            'email': input('Email: '),
            'ktp': input('No Ktp: '),
            'usia': int(input('Usia: '))
        }
        print()
        database.append(entry)


    for i, entry in enumerate(database):
        print('biodata', i + 1)
        if len(entry['ktp']) != 16 or entry['usia'] <= 16:
            print('==Maaf anda belum memenuhi persyaratan terdapat data ktp atau usia yang tidak valid. silahkan kembali ke menu awal==',syarat_ketentuan,'\n')
        else:
            formatter(entry)
        print()

    total_biaya = (banyak_tiket * current_harga) * 1.05 + biaya_adm

    pilihan1 = input("Apakah data diri sudah sesuai (ya/tidak) :")
    if pilihan1 == "ya":
        print("Tunggu sebentar...")
        time.sleep(2)
        pilihan2 = input("Melanjutkan ke proses transaksi (ya/tidak) :")
        if pilihan2 == "ya":
            print(total_biaya)
        else:
            print("========Terima kasih telah menggunakan program TICKETHREE========")
    else:
        print("Tunggu sebentar...")
        time.sleep(2)
        print("tidak valid")

if __name__ == '__main__':
    mainmenu()

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
# PROGRAM METODE PEMBAYARAN MELALUI BANK
print("""
----------------------------------------------------
SELAMAT DATANG DI METODE PEMBAYARAN TICKETHREE
----------------------------------------------------
Silahkan pilih metode pembayaran
a. Bank
b. Aplikasi Online
----------------------------------------------------
            """)
pilihmetodepemb = input("Silahkan pilih metode pembayaran dengan memasukkan abjad dari list di atas :")

if pilihmetodepemb == "a" or pilihmetodepemb == "A":
        print("""
------------------------------------
PILIHAN BANK
------------------------------------
a. BNI  
b. MANDIRI
c. BCA
------------------------------------                   
                    """)
        pilbank = input("Silahkan pilih bank dengan memasukkan abjad dari list diatas :")
        if pilbank == "a" or pilbank == "A":
            print("Rekening BNI")
            biaya_akhir = (biaya1 * promo_BNI) + biaya1  or (total_biaya * promo_BNI) + total_biaya
        elif pilbank == "b" or pilbank == "B":
            print("Rekening Mandiri")
            biaya_akhir = (biaya1 * promo_Mandiri) + biaya1  or (total_biaya * promo_Mandiri) + total_biaya
        else:
            print("Rekening BCA")
            biaya_akhir = (biaya1 * promo_BCA) + biaya1  or (total_biaya * promo_BCA) + total_biaya
        print("Total Pembayaran tiket anda: ", "Rp", biaya_akhir)
else:
        print("""
------------------------------------
PILIHAN APLIKASI ONLINE
------------------------------------
a. Shopeepay
b. Gopay
------------------------------------                   
                    """)
        pilonline = input("Silahkan pilih aplikasi online dengan memasukkan abjad dari list diatas :")
        if pilonline == "a" or pilonline == "A":
            print("NO SHOPEEPAY")
            biaya_akhir = (biaya1 * promo_shopeepay) + biaya1  or (total_biaya * promo_shopeepay) + total_biaya
        else:
            print("NO GOPAY")
            biaya_akhir = (biaya1 * promo_gopay) + biaya1  or (total_biaya * promo_gopay) + total_biaya
        print("Total Pembayaran tiket anda: ", "Rp", biaya_akhir)

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

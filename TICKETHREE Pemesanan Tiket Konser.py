import time

localtime = time.asctime(time.localtime(time.time()))
'''
import time berfungsi untuk melacak tanggal dan waktu pemesanan tiket
'''

import json

'''
import json digunakan untuk pertukaran dan penyimpanan database
'''

import random

'''
import random digunakan untuk menghasilkan angka acak sebagai kode unik tiket
'''

interface_program = 'Selamat Datang di Program TICKETHREE Aplikasi Pemesanan Tiket Konser Online'
header = interface_program.center(120, "=")
print(header)

katalog_konser = {
    'Katalog_1': {'Nama Acara': 'We The Fest', 'Artis': 'Dipha Barus,Weird Genius,Roni & Joni,Cyda',
                  'Tanggal': 'Jumat, 11 Juni 2021', 'Kota': 'Medan',
                  'Tempat': 'Pendopo Rumah Dinas Gubernur Sumatra Utara Jln. Jendral Sudirman', 'Genre': 'EDM',
                  'Harga': 1200000, 'Status\t': 150},
    'Katalog_2': {'Nama Acara': 'Indigo Fest', 'Artis': 'Fourtwenty,Burgerkill,Bottlesmoker,Mocca',
                  'Tanggal': 'Minggu, 20 Juni 2021', 'Kota': 'Riau',
                  'Tempat': 'Kompleks Bandar Seni Raja Ali Haji Purna', 'Genre': 'Indie', 'Harga': 1300000,
                  'Status': 98},
    'Katalog_3': {'Nama Acara': 'Java Jazz Fest', 'Artis': 'Tulus,Indra Lesmana,Maliq & DEssentials,Andien',
                  'Tanggal': 'Senin, 28 Juni 2021', 'Kota': 'Surabaya', 'Tempat': 'Tunjungan Plaza Convention Center',
                  'Genre': 'Jazz', 'Harga': 1500000, 'Status': 60},
    'Katalog_4': {'Nama Acara': 'Lalala Fest', 'Artis': 'Ardhito Pramono,Isyana Sarasvati,Yura Yunita,Crush',
                  'Tanggal': 'Sabtu, 5 Juni 2021', 'Kota': 'Jakarta',
                  'Tempat': 'Aula Simfonia 81 Jln. Industri Raya Blok B14', 'Genre': 'Pop', 'Harga': 500000,
                  'Status': 400}
}

interface_konser = """\n=================================================
Informasi Pemesanan Tiket Konser 'TICKETHREE'
================================================="""

def formatter(katalog):
    for key in katalog.keys():
        print(f"""{key}\t\t= {katalog[key]}""")

"""
formatter digunakan untuk menampilkan data konser dengan tampilan yang lebih userable
yaitu dengan menuliskan key dan value per baris
"""

def mainmenu():
    print("""Menu Program\t\t: 
1.Menu Pembelian Tiket Konser
2.Menu Pembatalan Tiket konser""")
    pembatas = '=' * len(header)
    print(pembatas)
    pilihan_menu = int(input("Ketik Menu Program (1/2)\t:"))
    if pilihan_menu == 1:
        filtermenu = True
        while filtermenu == True:
            print("""
\n==================================================
Filter Konser Berdasarkan\t:
1. Genre
2. Artis
3. Kota
4. Harga
\n=================================================""")
            filter_pilihan = int(input("Ketik Filter Konser Yang Anda Inginkan (1/2/3/4)\t:"))

            # filter berdasarkan genre musik
            if filter_pilihan == 1:
                print("""
\n=================================================
List Konser Berdasar Genre:
1. EDM
2. Indie
3. Jazz
4. Pop
""")
                filtermenu = False
                list_genre = int(input("Ketik List Konser Genre (1/2/3/4)\t: "))

                if list_genre == 1:
                    print(interface_konser)
                    for key in katalog_konser.keys():
                        if katalog_konser[key]['Genre'] == 'EDM':
                            current_harga = katalog_konser[key]['Harga']
                            print(formatter(katalog_konser[key]))

                elif list_genre == 2:
                    print(interface_konser)
                    for key in katalog_konser.keys():
                        if katalog_konser[key]['Genre'] == 'Indie':
                            current_harga = katalog_konser[key]['Harga']
                            print(formatter(katalog_konser[key]))

                elif list_genre == 3:
                    print(interface_konser)
                    for key in katalog_konser.keys():
                        if katalog_konser[key]['Genre'] == 'Jazz':
                            current_harga = katalog_konser[key]['Harga']
                            print(formatter(katalog_konser[key]))

                elif list_genre == 4:
                    print(interface_konser)
                    for key in katalog_konser.keys():
                        if katalog_konser[key]['Genre'] == 'Pop':
                            current_harga = katalog_konser[key]['Harga']
                            print(formatter(katalog_konser[key]))

                else:
                    print("\nMaaf Pilihan yang Anda Masukkan Salah")

            # filter berdasarkan artis
            elif filter_pilihan == 2:
                print("""
\n================================================
List Konser Berdasar Artis:
1. Ardhito Pramono
2. Dipha Barus
3. Fourtwenty
4. Tulus
""")
                filtermenu = False
                list_artis = int(input("Ketik List Konser Berdasar Artis (1/2/3/4)\t: "))

                if list_artis == 1:
                    print(interface_konser)
                    for key in katalog_konser.keys():
                        if katalog_konser[key]['Artis'] == 'Ardhito Pramono,Isyana Sarasvati,Yura Yunita,Crush':
                            current_harga = katalog_konser[key]['Harga']
                            print(formatter(katalog_konser[key]))

                elif list_artis == 2:
                    print(interface_konser)
                    for key in katalog_konser.keys():
                        if katalog_konser[key]['Artis'] == 'Dipha Barus,Weird Genius,Roni & Joni,Cyda':
                            current_harga = katalog_konser[key]['Harga']
                            print(formatter(katalog_konser[key]))

                elif list_artis == 3:
                    print(interface_konser)
                    for key in katalog_konser.keys():
                        if katalog_konser[key]['Artis'] == 'Fourtwenty,Burgerkill,Bottlesmoker,Mocca':
                            current_harga = katalog_konser[key]['Harga']
                            print(formatter(katalog_konser[key]))

                elif list_artis == 4:
                    print(interface_konser)
                    for key in katalog_konser.keys():
                        if katalog_konser[key]['Artis'] == 'Tulus,Indra Lesmana,Maliq & DEssentials,Andien':
                            current_harga = katalog_konser[key]['Harga']
                            print(formatter(katalog_konser[key]))

                else:
                    print("\nMaaf Pilihan yang Anda Masukkan Salah")

            # filter berdasarkan kota
            elif filter_pilihan == 3:
                print(""" 
\n================================================
List Konser Berdasar Kota\t:
1. Jakarta
2. Medan
3. Riau
4. Surabaya
""")
                filtermenu = False
                list_kota = int(input("Ketik List Konser Berdasar Kota (1/2/3/4)\t: "))

                if list_kota == 1:
                    print(interface_konser)
                    for key in katalog_konser.keys():
                        if katalog_konser[key]['Kota'] == 'Jakarta':
                            current_harga = katalog_konser[key]['Harga']
                            print(formatter(katalog_konser[key]))

                elif list_kota == 2:
                    print(interface_konser)
                    for key in katalog_konser.keys():
                        if katalog_konser[key]['Kota'] == 'Medan':
                            current_harga = katalog_konser[key]['Harga']
                            print(formatter(katalog_konser[key]))

                elif list_kota == 3:
                    print(interface_konser)
                    for key in katalog_konser.keys():
                        if katalog_konser[key]['Kota'] == 'Riau':
                            current_harga = katalog_konser[key]['Harga']
                            print(formatter(katalog_konser[key]))

                elif list_kota == 4:
                    print(interface_konser)
                    for key in katalog_konser.keys():
                        if katalog_konser[key]['Kota'] == 'Surabaya':
                            current_harga = katalog_konser[key]['Harga']
                            print(formatter(katalog_konser[key]))

                else:
                    print("\nMaaf Pilihan yang Anda Masukkan Salah")

            # filter berdasarkan harga
            elif filter_pilihan == 4:
                print("""
\n================================================
Filter Harga Berdasarkan\t:
1. Tertinggi->Terendah
2. Terendah->Tertinggi
""")
                filtermenu = False
                filter_harga = int(input("Ketik Filter Harga yang Anda Inginkan (1/2/3/4)\t: "))
                list_harga = []

                for key in katalog_konser.keys():
                    list_harga.append(katalog_konser[key]['Harga'])

                if filter_harga == 1:
                    list_harga.sort(reverse=True)
                    print("List Harga Tiket Konser Dari Yang Tertinggi :")
                    for i in range(0, len(list_harga)):
                        print('%d. %d' % (i + 1, list_harga[i]))

                    pilihan_harga = int(input("Masukkan Nomor Harga Yang Dipilih(1/2/3/4): "))

                    if pilihan_harga == 1:
                        print(interface_konser)
                        for key in katalog_konser.keys():
                            if katalog_konser[key]['Harga'] == 1500000:
                                current_harga = katalog_konser[key]['Harga']
                                formatter(katalog_konser[key])

                    elif pilihan_harga == 2:
                        print(interface_konser)
                        for key in katalog_konser.keys():
                            if katalog_konser[key]['Harga'] == 1300000:
                                current_harga = katalog_konser[key]['Harga']
                                formatter(katalog_konser[key])

                    elif pilihan_harga == 3:
                        print(interface_konser)
                        
                        for key in katalog_konser.keys():
                            if katalog_konser[key]['Harga'] == 1200000:
                                current_harga = katalog_konser[key]['Harga']
                                formatter(katalog_konser[key])

                    elif pilihan_harga == 4:
                        print(interface_konser)
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
                        print('%d. %d' % (i + 1, list_harga[i]))

                    pilihan_harga = int(input("Masukkan Nomor Harga Yang Dipilih(1/2/3/4): "))
                    if pilihan_harga == 1:
                        print(interface_konser)
                        for key in katalog_konser.keys():
                            if katalog_konser[key]['Harga'] == 500000:
                                current_harga = katalog_konser[key]['Harga']
                                formatter(katalog_konser[key])

                    elif pilihan_harga == 2:
                        print(interface_konser)
                        for key in katalog_konser.keys():
                            if katalog_konser[key]['Harga'] == 1200000:
                                current_harga = katalog_konser[key]['Harga']
                                formatter(katalog_konser[key])

                    elif pilihan_harga == 3:
                        print(interface_konser)
                        for key in katalog_konser.keys():
                            if katalog_konser[key]['Harga'] == 1300000:
                                current_harga = katalog_konser[key]['Harga']
                                formatter(katalog_konser[key])

                    elif pilihan_harga == 4:
                        print(interface_konser)
                        for key in katalog_konser.keys():
                            if katalog_konser[key]['Harga'] == 1500000:
                                current_harga = katalog_konser[key]['Harga']
                                formatter(katalog_konser[key])

                    else:
                        print("\nMaaf Pilihan yang Anda Masukkan Salah")

            else:
                print("\nMaaf Pilihan yang Anda Masukkan Salah")

    # Menu pembatalan tiket
    elif pilihan_menu == 2:
        proses_pembatalan = input("Masukkan Kode Unik Tiket Anda: ")
        list_kodeunik = list(proses_pembatalan)

        if len(list_kodeunik) == 7:
            konfirm_batal = input("Apakah anda sudah yakin melakukan pembatalan?(Y/T):")

            if konfirm_batal.upper() == "Y":
                print(
                    "\nTiket Anda Telah Dibatalkan, Refund akan dikirim melalui metode pembayaran dengan potongan 20%")
                exit(0)

            else:
                mainmenu()

        else:
            print("\nMaaf Kode yang Anda Masukkan Salah\n")
            mainmenu()

    else:
        mainmenu()

# pemesanan tiket
    print("\nTunggu sebentar...")
    time.sleep(2)

    syarat_ketentuan = ("\nSyarat dan ketentuan :"
                        "\n1. Pembeli tiket yang akan menonton konser harus berusia 17 tahun keatas dan memiliki KTP."
                        "\n2. Saat akan memasuki Acara pemegang tiket wajib menunjukkan KTP , serta menyertai bukti pembelian yang sah apabila diperlukan."
                        "\n3. Anak-anak atau Anak-anak tanpa tiket tidak diizinkan memasuki Acara."
                        "\n4. Setiap Pemegang Tiket yang memasuki Acara diwajibkan untuk patuh pada peraturan, ketentuan dan kondisi yang berlaku di Tempat Acara.\n")
    print('\n', syarat_ketentuan)
    biaya_adm = 3000
    repeat = True

    while repeat == True:
        file_name = open("dataevent.json", "r")
        data_str = "".join(file_name.readlines())
        print("""====================================
        \nInformasi Tiket Konser\t:
        1. We The Fest
        2. Indigo Fest
        3. Java Jazz Fest
        4. Lalala Fest 
        """)
        data_str = data_str.replace("\'", "\"")
        datanw = json.loads(data_str)

        # print(datanw, "\n\n", type(datanw), "\n", len(datanw))
        # file_name.close()
        pilih_konser = int(input("Silahkan input angka sesuai dengan acara yang sudah dipilih sebelumnya (1/2/3/4) : "))
        dct = "Katalog_%d" % pilih_konser
        st = datanw[pilih_konser - 1][dct]

        # print(status)
        status = datanw[pilih_konser - 1][dct]["Status"]
        print("Tiket tersedia dalam jumlah %d tiket" % status)
        banyak_tiket = int(input("Masukkan jumlah tiket yang ingin dipesan : "))
        status -= banyak_tiket
        print("Banyak tiket tersisa ", status)
        datanw[pilih_konser - 1][dct]["Status"] = status
        datanw = str(datanw)
        file_name.close()
        repeat = False
        database = []
        print()

        for i in range(int(banyak_tiket)):
            print('Biodata', i + 1)
            entry = {
                'nama': input('Nama: '),
                'telepon': input('Telepon: '),
                'email': input('Email: '),
                'KTP': input('No KTP: '),
                'usia': int(input('Usia: '))
            }
            print()
            database.append(entry)

        for i, entry in enumerate(database):
            print('Biodata', i + 1)

            if len(entry['KTP']) != 16 or entry['usia'] <= 16:
                print('===Maaf anda belum memenuhi persyaratan terdapat data ktp atau usia yang tidak valid===',
                        syarat_ketentuan, '\n')
                repeat = True

            else:
                formatter(entry)
                repeat = False
            print()

    global total_biaya
    total_biaya = (banyak_tiket * current_harga) * 1.05 + biaya_adm
    pilihan2 = input("\nMelanjutkan ke proses transaksi (ya/tidak) :")

    if pilihan2 == "ya":
        time.sleep(1)
        print("\nBiaya :", total_biaya)
        print("Tunggu sebentar...\n")
        time.sleep(2)

    else:
        print("\n========Terima kasih telah menggunakan program TICKETHREE========")
        exit(0)        

    # variabel paket merchandise dan promo tiap bank
    promo_BNI = 0.03
    promo_Mandiri = 0.025
    promo_BCA = 0.025
    promo_shopeepay = 0.3
    promo_gopay = 0.3
    paket1 = 15000
    paket2 = 85000
    paket3 = 110000
    
    # PROGRAM PEMBELIAN MERCHANDISE
    ulang = True 
    
    while ulang == True:    
        beli_merchandise = int(input("""
----------------------------------------------------
Disini kami menyediakan paket merchandise eksklusif 
untuk memeriahkan konser yang Anda pilih
----------------------------------------------------
1. Lighstick  Rp. 15.000
2. Lighstick + kaos  Rp. 85.000
3. Lightstick + kaos + topi  Rp. 110.000
----------------------------------------------------
Apakah Anda akan membeli paket merchandise?
(Jika iya ketik 1, Jika tidak ketik 2) 
----------------------------------------------------
        """))
    
        if beli_merchandise == 1:
            pilih_paket = True       

            # Input pilihan merchandise
            while pilih_paket == True:
                paket = int(input('\n1. Lighstick\n2. Lighstick + kaos\n3. Lightstick + kaos + topi\nSilahkan pilih 1, 2, atau 3 :\n'))

                if paket == 1:
                    harga_merch = paket1 
                    biaya1 =  total_biaya + paket1 
                    print('\nTotal biaya = ', biaya1)
                    pilih_paket = False 
                    ulang = False

                elif paket == 2:
                    harga_merch = paket2
                    biaya1 = total_biaya + paket2
                    print('\nTotal biaya = ', biaya1 )
                    pilih_paket = False
                    ulang = False

                elif paket == 3:
                    harga_merch = paket3
                    biaya1 = total_biaya + paket3
                    print('\nTotal biaya = ', biaya1)
                    pilih_paket = False
                    ulang = False

                else:
                    print('\nInput Anda salah! Silahkan masukkan angka 1/2/3')
        
        elif beli_merchandise == 2:
            harga_merch = 0
            biaya1 = total_biaya
            print()
            ulang = False
    
        else:
            print("\nInput Anda salah! Silahkan coba lagi")
            
    # PROGRAM METODE PEMBAYARAN MELALUI BANK    
    ulang = True 
    
    while ulang == True:
        pilihmetodepemb = int(input("""
----------------------------------------------------
SELAMAT DATANG DI METODE PEMBAYARAN TICKETHREE
----------------------------------------------------
Silahkan pilih metode pembayaran
1. Bank
2. Aplikasi Online
----------------------------------------------------
Silahkan pilih metode pembayaran dengan memasukkan nomor dari list di atas :
    """))
    
        if pilihmetodepemb == 1:            
                print("""
------------------------------------
PILIHAN BANK
------------------------------------
1. BNI  
2. MANDIRI
3. BCA
------------------------------------                   
                            """)
                pilbank = int(input("Silahkan pilih bank dengan memasukkan nomor dari list diatas :"))

                if pilbank == 1:
                    print("Rekening BNI 0178305704")
                    biaya_akhir = (biaya1 * promo_BNI) + biaya1  or (total_biaya * promo_BNI) + total_biaya
                    print("Total Pembayaran tiket anda: ", "Rp", biaya_akhir)
                    ulang = False

                elif pilbank == 2:
                    print("Rekening Mandiri 1560009861578")
                    biaya_akhir = (biaya1 * promo_Mandiri) + biaya1  or (total_biaya * promo_Mandiri) + total_biaya
                    print("Total Pembayaran tiket anda: ", "Rp", biaya_akhir)
                    ulang = False

                elif pilbank == 3:
                    print("Rekening BCA 5220304312")
                    biaya_akhir = (biaya1 * promo_BCA) + biaya1  or (total_biaya * promo_BCA) + total_biaya
                    print("Total Pembayaran tiket anda: ", "Rp", biaya_akhir)
                    ulang = False

                else:
                    print('\nAnda salah! coba lagi!')
                
        elif pilihmetodepemb == 2:            
                print("""
------------------------------------
PILIHAN APLIKASI ONLINE
------------------------------------
1. Shopeepay
2. Gopay
------------------------------------                   
                            """)
                pilonline = int(input("Silahkan pilih aplikasi online dengan memasukkan abjad dari list diatas :"))

                if pilonline == 1:
                    print("NO SHOPEEPAY 0812 3135 2171")
                    biaya_akhir = (biaya1 * promo_shopeepay) + biaya1  or (total_biaya * promo_shopeepay) + total_biaya
                    print("Total Pembayaran tiket anda: ", "Rp", biaya_akhir)
                    ulang = False

                elif pilonline == 2:
                    print("NO GOPAY 0812 6373 3323")
                    biaya_akhir = (biaya1 * promo_gopay) + biaya1  or (total_biaya * promo_gopay) + total_biaya
                    print("Total Pembayaran tiket anda: ", "Rp", biaya_akhir)
                    ulang = False

                else:
                    print('\nAnda salah! coba lagi!')
            
        else:
            print('\nInput yang Anda masukkan salah! Silahkan coba lagi!')
    
    # program untuk memunculkan Struk, kode transaksi dan kode unik
    kode_unik = random.randint(999999, 9999999)  
    ulangi = True 
    
    while ulangi == True:
        print("------------- Kode transaksi Anda -------------\n",
            "\n------------------ ", kode_unik, " ------------------ ", 
            "\n\nSilahkan lakukan pembayaran dengan kode tersebut\n")
        bayar = int(input("Silahkan masukkan kode transaksi untuk melakukan pembayaran:\n"))
        
        if bayar == kode_unik : 
            print("\nSelamat! Transaksi sukses!\n")
            print("\n================= STRUK =====================")
            print("\n=========",localtime, "==========\n")
            formatter(entry)
            print("============================================="
                    "\nBanyak Tiket  : \t", banyak_tiket,
                    "\nHarga tiket   : \t", current_harga,
                    "\nHarga merch   : \t", harga_merch,
                    "\nTotal biaya   : \t", biaya_akhir,
                    "\n\n================= KODE UNIK =================",
                    "\n==================", kode_unik, "=================="
                    """\nTukarkan kode diatas dengan merchandise 
yang Anda beli.
Jika tidak membeli, abaikan! akan dicek!""",
                    "\n================ TERIMA KASIH ===============")
            ulangi = False 

        else: 
            print('Kode yang Anda masukkan salah! Silahkan coba lagi!\n')
        print()
        ulang = False

if __name__ == '__main__':
    mainmenu()

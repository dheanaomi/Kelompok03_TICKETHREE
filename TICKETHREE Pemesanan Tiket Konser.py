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
    print("Informasi Rekomendasi Konser dan Konser Coming Soon")
    print("1. Acara")
    print("2. Artis")
    print("3. Kota" )
    print("4. Harga")
    print("")

    filter_pilihan= input("Filter Konser Pencarian Berdasar (Acara/Artis/Kota/Harga)\t:")

    #Berdasarkan Acara
    if filter_pilihan.capitalize()=="Acara":
        #Menampilkan list berdasar acara
        print("List Konser Berdasar Acara")
        print("1. EDM")
        print("2. Indie")
        print("3. Jazz")
        print("4. Pop")
        print("")
        list_acara= int(input("Ketik List Konser Acara (1/2/3/4)\t: "))
        if list_acara==1:
            print("==================================")
            print("Tiket Konser yang Dipilih yaitu:\n"
                    "Konser Berdasarkan Acara\n"
                    "Filter 'EDM'"
                    "Harga Tiket Rp ")

        elif list_acara==2:
            print("Bagiannya Afiq")

        else:
            print("Nyusul nggabung yang lain")
    else:
        print("Nyusul jugaa")

#Pilihan Pembatalan Tiket
else:
    proses_pembatalan= input("Masukkan Kode Unik Tiket Anda: ")
    print(proses_pembatalan)
    konfirm_batal= input("Apakah anda sudah yakin melakukan pembatalan?(Y/T):")
    if konfirm_batal.upper()=="Y":
        print("Tiket Anda Telah Dibatalkan, Refund akan dikirim melalui metode pembayaran dengan potongan 20%")

    else:
       exit()








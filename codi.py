#Menu
menu = {
    'Gayung' : 5000,
    'Ember'  : 2000,
    'Sapu'   : 10000,
    'Gelas'  : 8000
}

def list_menu():
    menu
    for key, value in menu.items():
        print(key, ':', value)

def tambah():
    input_baru = input('masukan menu: ')
    in_baru = int(input('masukan harga: '))
    menu [input_baru] = in_baru

def update():
    input_baru = input('Update menu: ')
    in_baru = int(input('Update harga: '))
    menu[input_baru] = in_baru

def delete():
    del menu [input('menu yang ingin di hapus: ')]

#CRUD
def main_menu():
    while True:
        print('menu')
        print('1. List\n2. Tambahkan\n3. Update\n4. Hapus\n5. Exit')
        choice = input('Masukan pilihan: ')
        if choice == '1':
            list_menu()
            print('\nTekan [Enter] untuk kembali')
            input()
        elif choice == '2':
            tambah()
            print('\nTekan [Enter] untuk kembali')
            input()
        elif choice == '3':
            update()
            print('\nTekan [Enter] untuk kembali')
            input()
        elif choice == '4':
            delete()
            print('\nTekan [Enter] untuk kembali')
            input()
        elif choice == '5':
            print('Anda telah keluar')
            break

def kasir():
    menu 
    for key, value in menu.items ():
        print (key,":", value)
    pilih = menu [input("masukkan menu yang anda inginkan: ")]
    jumlah = int(input("masukan jumlah menu yang dibeli: "))
    total = pilih*jumlah
    Hari = input('masukan hari pembelian: ')


    if Hari == 'senin' :
        diskon = total*(0.1)
        print('-Diskon 10 %-')
    elif Hari == 'jumat': 
        diskon = total*(0.25)
        print('-Diskon 10 %-')
    else: 
        print ('maaf,tidak dapat diskon')

    total_bayar=int(total - diskon)

    uang = int(input("Uang Tunai pembeli: RP"))
    kembalian = int(uang - total_bayar)
    print(f"Kembalian: Rp{kembalian}")

    print(f"""
    --------------------------------------------
    ------------ S T R U K   B E L I------------
    --------------------------------------------
    Beli           : {pilih} barang {jumlah}
    Total          : RP{total}
    Diskon         : - RP{diskon}
    Total Tagihan  : RP{total_bayar}
    Uang           : RP{uang}
    Kembalian      : Rp{kembalian}
    --------------------------------------------
     Terima Kasih Telah Membeli Barang       
    --------------------------------------------
    """)
while True : 
    print('selamat datang')
    print('1. database')
    print('2. kasir')
    x = input('masukkan pilihan: ')
    if  x == "1" :
        main_menu ()
    elif x == "2" :
        kasir()
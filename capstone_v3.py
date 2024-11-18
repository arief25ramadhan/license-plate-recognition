import sys
# Define inventory using list of lists
list_item_roti = [
    ['ITM001', 'Donat', 10000, 10, 0],
    ['ITM002', 'Muffin', 15000, 10, 0],
    ['ITM003', 'Brownies', 20000, 10, 0],
    ['ITM004', 'Roti Tawar', 10000, 10, 0],
    ['ITM005', 'Cupcake', 5000, 10, 0]
]
index_item_roti = 6 

def tambah_roti():
    print("\nOpsi: Tambah Roti")
    print("== Pilih Menu Tambah Roti ==")
    print("1. Tambah Item")
    print("2. Keluar")
    while True:
        opsi_tambah_roti = input("Pilih Opsi Tambah 1/2: ")
        if opsi_tambah_roti == '1':
            input_roti_baru()
        elif opsi_tambah_roti == '2':
            print("Kembali ke menu utama.")
            menu_utama()  # Pastikan `menu_utama` sudah didefinisikan
            break
        else:
            print("Input Tidak Valid. Silakan masukkan 1 atau 2.")

def input_roti_baru():
    while True:
        # Meminta ID roti baru dari pengguna
        input_id_roti = input("Masukkan ID Roti Baru (misal: ITM006): ").strip().upper()

        # Validasi apakah ID sudah ada
        id_sudah_ada = any(roti[0] == input_id_roti for roti in list_item_roti)
        if not input_id_roti:
            print("ID tidak boleh kosong. Silakan masukkan ID.")
        elif id_sudah_ada:
            print(f"ID '{input_id_roti}' sudah ada dalam daftar. Silakan masukkan ID yang berbeda.")
        else:
            while True:
                # ID valid, lanjutkan untuk input nama roti
                input_nama_roti = input("Masukkan Nama Roti Baru: ").strip()
                if not input_nama_roti:
                    print("Nama roti tidak boleh kosong. Silakan masukkan nama roti.")
                else:
                    while True:
                        input_harga_roti = input("Masukkan Harga Roti Baru: ").strip()
                        if input_harga_roti.isdigit(): # 01000 ->1000
                            input_harga_roti = int(input_harga_roti)
                            tambahkan_stock_roti(input_id_roti, input_nama_roti, input_harga_roti)
                            return  # Selesai, kembali ke menu tambah roti
                        else:
                            print("Masukkan nominal harga yang valid!")

def tambahkan_stock_roti(input_id_roti, input_nama_roti, input_harga_roti):
    while True:
        input_stock_roti = input("Masukkan Stock Roti Baru: ").strip()
        if input_stock_roti.isdigit():
            input_stock_roti = int(input_stock_roti)
            konfirmasi_hapus = input(
                f"Apakah Anda yakin ingin menambahkan item {input_nama_roti} dengan ID {input_id_roti}, harga Rp {input_harga_roti}, dan stok {input_stock_roti}? (y/n): "
            ).strip().lower()
            if konfirmasi_hapus == 'y':
                list_item_roti.append([input_id_roti, input_nama_roti, input_harga_roti, input_stock_roti, 0])
                print(f"Item {input_nama_roti} berhasil ditambahkan!")
                break
            elif konfirmasi_hapus == 'n':
                print("Penambahan item dibatalkan.")
                break
            else:
                print("Masukkan 'y' untuk ya atau 'n' untuk tidak.")
        else:
            print("Masukkan nominal stock yang valid.")

    # Setelah selesai menambah roti, kembali ke menu tambah roti
    tambah_roti()


# Fungsi untuk mengambil harga dari roti untuk keperluan sortir
def ambil_harga(roti): # [ITM, "DONAT", 10000, 12, 0.0]
    return roti[2]  # Mengambil harga roti

# Menampilkan menu keseluruhan
def menu_keseluruhan():
    print("\nMenu Roti:")
    for roti in list_item_roti:
        print(f"ID: {roti[0]} | {roti[1]} | Rp {roti[2]} | Stok: {roti[3]}")

    while True:
        print("\nTampilkan Menu Keseluruhan:")
        print("1. Sortir berdasarkan harga termurah")
        print("2. Sortir berdasarkan harga termahal")
        print("3. Kembali ke menu utama")

        opsi_sortir = input("Pilih opsi (1/2/3): ")
        if opsi_sortir == '1':
            sorted_menu = sorted(list_item_roti, key=ambil_harga)  # Sortir berdasarkan harga termurah
            print("\nMenu Roti (Harga Termurah ke Termahal):")
            for roti in sorted_menu:
                print(f"ID: {roti[0]} | {roti[1]} | Rp {roti[2]} | Stok: {roti[3]}")
        elif opsi_sortir == '2':
            sorted_menu = sorted(list_item_roti, key=ambil_harga, reverse=True)  # Sortir berdasarkan harga termahal
            print("\nMenu Roti (Harga Termahal ke Termurah):")
            for roti in sorted_menu:
                print(f"ID: {roti[0]} | {roti[1]} | Rp {roti[2]} | Stok: {roti[3]}")
        elif opsi_sortir == '3':
            break  # Kembali ke menu utama
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

# Fungsi untuk menampilkan menu berdasarkan ID yang dipilih oleh pengguna
def input_tampilkan_menu():
     print("\nMenu Roti:")
     for roti in list_item_roti:
        print(f"ID: {roti[0]} | {roti[1]} | Rp {roti[2]} | Stok: {roti[3]}")

     while True:
        input_id_menu = input("\nMasukkan ID menu yang ingin ditampilkan: ").strip().upper()  # Minta ID item
        found = False
        for roti in list_item_roti:
            if roti[0] == input_id_menu:
                print(f"\nID: {roti[0]} | {roti[1]} | Rp {roti[2]} | Stok: {roti[3]}")
                found = True
                break  # Menghentikan pencarian setelah ID ditemukan
        if not found:
            print(f"ID '{input_id_menu}' tidak ditemukan. Silakan coba lagi.")
        else:
            break  # Keluar dari loop dan kembali ke menu utama

# Fungsi untuk menampilkan menu utama
def tampilkan_main_menu():
    while True:
        print("\nOpsi:")
        print("1. Tampilkan Menu Keseluruhan")
        print("2. Tampilkan Menu Berdasarkan ID")
        print("3. Keluar")

        choice = input("Pilih opsi: ")
        if choice == '1':
            menu_keseluruhan()  # Panggil fungsi untuk menampilkan menu keseluruhan
        elif choice == '2':
            input_tampilkan_menu()  # Panggil fungsi untuk menampilkan berdasarkan ID
        elif choice == '3':
            print("Terima kasih! Keluar dari program.")
            break  # Keluar dari program
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")


def hapus_roti():
    while True:
        print("\nOpsi: Hapus Roti")
        print("== Pilih Menu Hapus Roti ==")
        print("1. Hapus Item")
        print("2. Keluar")
        
        opsi_hapus_roti = input("Pilih Opsi Hapus (1/2): ")
        if opsi_hapus_roti == '1':
            pilihan_hapus()
        elif opsi_hapus_roti == '2':
            print("Kembali ke menu utama.")
            menu_utama()  # Fungsi untuk kembali ke menu utama (pastikan ini sudah didefinisikan)
            break
        else:
            print("Input tidak valid. Silakan masukkan 1 atau 2.")

def pilihan_hapus():
    print("\nMenu Roti:")
    for roti in list_item_roti:
        print(f"ID: {roti[0]} | {roti[1]} | Rp {roti[2]} | Stok: {roti[3]}")

    while True:
        input_id_roti = input("Masukkan ID Roti yang ingin dihapus: ").strip().upper()

        # Cek apakah ID ditemukan
        roti_ditemukan = None
        for roti in list_item_roti:
            if roti[0] == input_id_roti:
                roti_ditemukan = roti
                break

        if roti_ditemukan:
            print(f"Anda akan menghapus item: {roti_ditemukan[0]} | {roti_ditemukan[1]} | Stok: {roti_ditemukan[3]} | Harga: Rp {roti_ditemukan[2]}")
            
            # Konfirmasi penghapusan
            konfirmasi_hapus = input("Apakah Anda yakin ingin menghapus item ini? (y/n): ").strip().lower()
            if konfirmasi_hapus == 'y':
                list_item_roti.remove(roti_ditemukan)
                print(f"Item {roti_ditemukan[0]} | {roti_ditemukan[1]} | Stok: {roti_ditemukan[3]} | Harga: Rp {roti_ditemukan[2]} berhasil dihapus.")
                break
            elif konfirmasi_hapus == 'n':
                print("Penghapusan dibatalkan.")
                break
            else:
                print("Input tidak valid. Masukkan 'y' untuk ya atau 'n' untuk tidak.")
        else:
            print(f"ID '{input_id_roti}' tidak ditemukan. Silakan coba lagi.")

def menu_update_roti():
    while True:
        print("Opsi 3: Update Roti")
        print(" == Pilih Opsi Update == ")
        print(" 1. Perbaharui Harga ")
        print(" 2. Perbaharui Stock ")
        print(" 3. Keluar")

        # Menampilkan daftar roti untuk dipilih
        # for i in range(len(list_item_roti)):
        #     print(f"{i + 1}. Nama: {list_item_roti[i][1]}, Stock: {list_item_roti[i][3]}")

        input_nomor_roti = input('Pilih Opsi Update 1/2/3: ')
        if input_nomor_roti.isdigit():
            input_nomor_roti = int(input_nomor_roti)  # Mengubah ke indeks list (0-based)
                # Menentukan dan memperbarui harga atau stock
            if input_nomor_roti == 1:
                    update_roti('harga')
            elif input_nomor_roti == 2:
                    update_roti('stock')
            elif input_nomor_roti == 3:
                    menu_utama()
                    break
            else:
                    print('Input tidak Valid')
        else:
            print('Masukkan Index Valid !!')

def update_roti(kolom):
    # Menampilkan daftar roti
    print("\nDaftar Menu Roti:")
    for roti in list_item_roti:
        print(f"ID: {roti[0]} | Nama: {roti[1]} | Harga: Rp {roti[2]} | Stock: {roti[3]}")

    input_id_roti = input('Masukkan ID Roti Yang Mau Diupdate: ').strip().upper()
    
    # Mencari roti berdasarkan ID
    roti_ditemukan = next((roti for roti in list_item_roti if roti[0] == input_id_roti), None)

    if not roti_ditemukan:
        print(f"ID '{input_id_roti}' tidak ditemukan. Silakan coba lagi.")
        return  # Keluar jika ID tidak ditemukan

    # Proses pembaruan
    while True:
        try:
            nilai_baru = int(input(f"Masukkan {kolom.capitalize()} Baru untuk {roti_ditemukan[1]}: "))
            if kolom == 'harga' and nilai_baru <= 0:
                print("Harga harus lebih besar dari 0.")
            elif kolom == 'stock' and nilai_baru < 0:
                print("Stock tidak boleh negatif.")
            else:
                if konfirmasi(f"Apakah Anda yakin ingin mengubah {kolom} menjadi {nilai_baru}? (y/n): "):
                    roti_ditemukan[2 if kolom == 'harga' else 3] = nilai_baru
                    print(f"Roti dengan ID {roti_ditemukan[0]}, nama {roti_ditemukan[1]} harganya berhasil diubah menjadi {nilai_baru}.")
                else:
                    print(f"Pengubahan {kolom} dibatalkan.")
                break
        except:
            print(f"Masukkan nilai {kolom} yang valid (angka).")

def konfirmasi(text):
    while True:
        konfirmasi_input = input(text).lower()
        if konfirmasi_input == "y":
            return True
        elif konfirmasi_input == "n":
            return False
        else:
            print("Input tidak valid. Masukkan 'y' untuk ya atau 'n' untuk tidak.")

# Menu utama
def menu_utama():
    while True:
        print("\n== Inventory Toko Roti == \n 1. Tambahkan Roti \n 2. Lihat Menu Roti \n 3. Perbaharui Stok/Harga Item \n 4. Hapus Item \n 5. Keluar\n")
        input_opsi = input('Pilih Opsi 1-6: ')
        
        if input_opsi == '1':
            tambah_roti()
        elif input_opsi == '2':
            tampilkan_main_menu()
        elif input_opsi == '3':
            menu_update_roti()
        elif input_opsi == '4':
            hapus_roti()
        elif input_opsi == '5':
            print('Keluar')
            sys.exit()
        else:
            print("Opsi tidak valid, silakan pilih 1-6.")
menu_utama()

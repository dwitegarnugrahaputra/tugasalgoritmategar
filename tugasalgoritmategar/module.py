stok = []

def add():
    input_nama = input("masukkan nama barang : ").title()
    input_stok = int(input("Masukkan stok barang : "))
    item = {'nama' : input_nama, 'stok' : input_stok}
    stok.append(item)
    print("--- data berhasil ditambahkan ---")
    return '\n'

def edit():
    index = int(input("ubah data ke : "))
    index -= 1
    input_nama = input("masukkan nama barang : ").title()
    input_stok = int(input("masukkan stok barang : "))
    data_change = {'nama' : input_nama, 'stok' : input_stok}
    stok[index] = data_change
    print("--- data berhasil diperbarui ---")
    return '\n'

def delete():
    index = int(input("hapus data ke : "))
    index -= 1
    del stok[index]
    print("--- data berhasil dihapus ---")
    return '\n'

def search():
    data_input = input("cari nama barang : ").title()
    number = 1
    stock = []
    for i in stok:
        if data_input in i['nama']:
            stock.append(i)
    if stock:
        for i in stock:
            print(f"{number}. {i['nama']} , Stok : {i['stok']}")
            number += 1
    else:
        print("--- data barang tidak ditemukan ---")
    return '\n'

def list():
    number = 1
    if stok:
        print("--- data barang ---")
        for i in stok:
            print(f"{number}. {i['nama']} , Stok : {i['stok']}")
            number += 1
    else:
        print("--- data barang kosong ---")
    return '\n'

def total():
    print(f"jumlah data tersimpan : {len(stok)}")
    return '\n'
from tabulate import tabulate
import re

# Fungsi untuk validasi input pemilihan menu 
def validasiMenu(entry,limit):
    while True:
        try:
            entry = int(entry)
            if not 0<entry<=limit :
                print('Input salah\nMohon dicoba kembali')
                entry = input('Pilihan menu = ')
                continue
        except:
            print('Input salah\nMohon dicoba kembali')
            entry = input('Pilihan menu = ')
            continue
        break
    return entry

# Fungsi untuk validasi input no telp
def validasiNoTelp(entry):
    while True:
        if not re.match('^[\d]*$',entry):
            print('Input salah\nMohon dicoba kembali')
            entry = input('Masukkan nomor telepon (karakter angka saja): ')
            continue
        break
    return entry

# Fungsi untuk validasi input email
def validasiEmail(entry):
    while True:
        if not re.match('^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}$',entry):
            print('Input salah\nMohon dicoba kembali')
            entry = input('Masukkan alamat email : ')
            continue
        break
    return entry

#Fungsi untuk memilih tampilan berdasarkan grup
def tampilanGrup():
    temp = []
    for i in data:
        if i['Grup'] not in temp:
            temp.append(i['Grup'])
    grup = temp
    while True:
        print('Pilih Grup :')
        for i in grup:
            print(f'{grup.index(i)+1} : {i}')
        print(f'{len(grup)+1} : Keluar')
        menu = input('Pilihan menu = ')
        menu = validasiMenu(menu,(len(grup)+1))
        if menu <= len(grup):
            grupTerpilih = grup[menu-1]
            temp = []
            for i in data:
                if i['Grup'] == grupTerpilih:
                    temp.append(i)
            print(tabulate(temp, headers = 'keys', tablefmt= 'pretty'))
            break
        else:
            break

#Fungsi untuk memasukkan input grup
def inputGrup():
    temp = []
    for i in data:
        if i['Grup'] not in temp:
            temp.append(i['Grup'])
    grup = temp
    while True:
        print('Pilih Grup :')
        for i in grup:
            print(f'{grup.index(i)+1} : {i}')
        print(f'{len(grup)+1} : Tambah grup baru' )
        print(f'{len(grup)+2} : Keluar')
        menu = input('Pilihan menu = ')
        menu = validasiMenu(menu,(len(grup)+2))
        if menu <= len(grup):
            grupTerpilih = grup[menu-1]
            return grupTerpilih
            break
        elif menu == len(grup)+1:
            katbaru = input('Masukkan grup baru = ')
            grup.append(katbaru)
        else:
            break

#Fungsi untuk menampilkan data dalam bentuk tabel
def readData():
    while True :
        print("""Pilihan tabel tampilan data :
1. Tampilkan semua data
2. Tampilkan berdasarkan grup
3. Keluar""")
        menu = input('Pilihan menu = ')
        menu = validasiMenu(menu,3)
        if menu == 1:
            print(tabulate(data, headers = 'keys', tablefmt= 'pretty'))
            break
        elif menu == 2:
            print('\n')
            tampilanGrup()
            break
        else:
            break

#Fungsi untuk menambahkan data baru
def addData():
    index = len(data)+1
    nama = input('Masukkan nama : ')
    notelp = input('Masukkan nomor telepon (karakter angka saja) : ') 
    notelp = validasiNoTelp(notelp)
    email = input('Masukkan alamat email : ')
    email = validasiEmail(email)
    tulisGrup = inputGrup()
    data.append({'Index':index, 'Nama':nama, 'Nomor Telepon':notelp, 'Email':email, 'Grup':tulisGrup})
    print('\nData berhasil disimpan !')

#Fungsi untuk mencari entry data
def findData(criteria,entry):    
    index = 0
    for i in data:
        if i[criteria] == entry:
            break
        index +=1
    return index
    
#Fungsi untuk update data
def updateData():
    update = int(input('Masukkan index data yang ingin diubah = '))
    index = findData('Index',update)
    if index >= len(data):
        print('Data tidak ditemukan')
    else:
        temp = []
        temp.append(data[index])
        print(tabulate(temp ,headers = 'keys', tablefmt= 'pretty'))
        print("Pilih kolom yang akan diupdate :\n1. Nama\n2. Nomor Telepon\n3. Email\n4. Grup\n5. Keluar")
    menu = input('Pilihan menu = ')
    menu = validasiMenu(menu,5)
    if menu == 1:
        nama = input('Masukkan nama : ')
        data[index]['Nama'] = nama
        print('Data berhasil diupdate !')
    elif menu == 2:
        notelp = input('Masukkan nomor telepon (karakter angka saja) : ') 
        notelp = validasiNoTelp(notelp)
        data[index]['Nomor Telepon'] = notelp
        print('Data berhasil diupdate !')
    elif menu == 3:
        email = input('Masukkan alamat email : ')
        email = validasiEmail(email)
        data[index]['Email'] = email
        print('Data berhasil diupdate !')
    elif menu == 4:
        tulisGrup = inputGrup()
        data[index]['Grup'] = tulisGrup
        print('Data berhasil diupdate !')

#Fungsi untuk hapus data
def deleteData():
    update = input('Masukkan index data yang ingin dihapus = ')
    try:
        index = findData('Index',int(update))
        if index >= len(data):
            print('Data tidak ditemukan')
        else:
            temp = []
            temp.append(data[index])
            print(tabulate(temp ,headers = 'keys', tablefmt= 'pretty'))
            while True :
                konfirmasi = input('Yakin? [Y/N] = ').capitalize()
                if konfirmasi == ('Y'):
                    del data[index]
                    print('Data berhasil dihapus !')
                    print('Menyusun ulang index data ...')
                    n = 0
                    for i in data :
                        i['Index'] = n+1
                        data[n] = i
                        n += 1
                    break
                elif konfirmasi == ('N'):
                    break
                else :
                    continue
    except:
        print('Data tidak ditemukan')

# Memulai program utama
def programUtama():
    print('Selamat datang di program Yellow Pages (Data Kontak Telepon)')
    while True :
        print("""Pilih opsi berikut :\n1. Masukkan data baru\n2. Tampilkan data\n3. Update data\n4. Hapus data\n5. Keluar""")
        menu = input('Pilihan menu = ')
        menu = validasiMenu(menu,5)
        if menu == 1:
            print('\n')
            addData()
            print('\n')
        elif menu == 2:
            print('\n')
            readData()
            print('\n')
        elif menu == 3:
            print('\n')
            updateData()
            print('\n')
        elif menu == 4:
            print('\n')
            deleteData()
            print('\n')
        else:
            print("Sampai jumpa !")
            break

data = [
    {'Index': 1, 'Nama': 'Mike', 'Nomor Telepon':'08161737455', 'Email':'mike@gmail.com', 'Grup':'Personal'},
    {'Index': 2, 'Nama': 'Fred', 'Nomor Telepon':'0212345678', 'Email':'fred@gmail.com', 'Grup':'Kantor'},
    {'Index': 3, 'Nama': 'Tefa', 'Nomor Telepon':'0219876543', 'Email':'tefa@gmail.com', 'Grup':'Personal'},
    {'Index': 4, 'Nama': 'Budi', 'Nomor Telepon':'02254321321', 'Email':'budi@yahoo.com', 'Grup':'Personal'},
    {'Index': 5, 'Nama': 'Harjo', 'Nomor Telepon':'085692798765', 'Email':'harjo@hotmail.com', 'Grup':'Kantor'},
]

grup = ['Personal','Kantor']

programUtama()
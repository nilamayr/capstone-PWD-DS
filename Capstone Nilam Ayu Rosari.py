################################# STOK GUDANG NILAM'S #################################


# DATA STOK GUDANG
stockGudang =  [
                {'code'         : '001',
                 'name'         : 'Facial Wash',
                 'category'     : 'Skincare',
                 'stock'        : '100',
                 'vendor'       : 'CV.KARYA INDAH'
                },
                {'code'         : '002',
                 'name'         : 'Laptop',
                 'category'     : 'Electronics',
                 'stock'        : '57',
                 'vendor'       : 'PT.NUSA JAYA'
                },
                {'code'         : '003',
                 'name'         : 'Panci',
                 'category'     : 'Cutlery',
                 'stock'        : '172',
                 'vendor'       : 'PT.PELITA HARAPAN'
                },
                {'code'         : '004',
                 'name'         : 'Printer',
                 'category'     : 'Electronics',
                 'stock'        : '300',
                 'vendor'       : 'PT.NUSA JAYA'
                },
                {'code'         : '005',
                 'name'         : 'Mangkok',
                 'category'     : 'Cutlery',
                 'stock'        : '81',
                 'vendor'       : 'PT.PELITA HARAPAN'
                },
                {'code'         : '006',
                 'name'         : 'Note Book',
                 'category'     : 'Stationery',
                 'stock'        : '165',
                 'vendor'       : 'PT.MULTI STATIONARY'
                },
                {'code'         : '007',
                 'name'         : 'Face Toner',
                 'category'     : 'Skincare',
                 'stock'        : '172',
                 'vendor'       : 'CV.KARYA INDAH'
                },
                {'code'         : '008',
                 'name'         : 'Sunscreen',
                 'category'     : 'Skincare',
                 'stock'        : '118',
                 'vendor'       : 'CV.KARYA INDAH'
                },
                {'code'         : '009',
                 'name'         : 'Ballpoint',
                 'category'     : 'Stationery',
                 'stock'        : '169',
                 'vendor'       : 'PT.MULTI STATIONARY'
                },
                {'code'         : '010',
                 'name'         : 'Cutter ',
                 'category'     : 'Stationery',
                 'stock'        : '180',
                 'vendor'       : 'PT.MULTI STATIONARY'
                }
                ]

recordDataMutasi = []
recordDataHistoryAdd = []
recordDataHistoryDel = []

# MENU UTAMA
def Menu():
    print('''\n
*=*=*=* SELAMAT DATANG DI GUDANG NILAM'S !!^^ *=*=*=*
        
List Menu :
        1. Tampilkan Data Stock Barang
        2. Tambah Data Stock Barang Baru
        3. Update Data Stock Barang
        4. Hapus Data Stock Barang
        5. Record Kegiatan Stock Gudang
        6. Exit Program
          ''')

# TEMPLETE TABEL STOK BARANG
def showTable(listdata):
    print('\n')
    print("\t================== DATA STOCK GUDANG NILAM'S ===================")
    print('*' * 88)
    print('|KODE |\t    NAMA       |     KATEGORI   |   STOK   |\t   VENDOR   \t|    STATUS    |')
    print('----------------------------------------------------------------------------------------')
    for i in range(len(listdata)):
        if int(str(listdata[i]['stock'])) > 0:
            status = 'Ready' 
        else:
            status = 'Out of Stock'
        print(f"|{listdata[i]['code']:^5}|{listdata[i]['name']:16}|{listdata[i]['category']:16}|{listdata[i]['stock']:^10}|{listdata[i]['vendor']:20}|{status:^14}|")
    print('*' * 88)
    print('*' * 88)

# TEMPLETE TABEL MUTASI STOK GUDANG
def recordMutation(mutasidata):
    print('\n')
    print("\t============================ RECORD MUTASI STOK GUDANG NILAM'S ============================")
    print('*' * 107)
    print('|KODE |\t    NAMA       |    STOK AWAL   |   STOK MASUK   |   STOK KELUAR   |   STOK AKHIR   |    STATUS   |')
    print('-----------------------------------------------------------------------------------------------------------')
    for i in range(len(mutasidata)):
        if int(mutasidata[i]['totalstock']) > 0:
            status = 'Ready' 
        else:
            status = 'Out of Stock'
        print(f"|{mutasidata[i]['code']:^5}|{mutasidata[i]['name']:16}|{mutasidata[i]['stock']:^16}|{mutasidata[i]['stockin']:^16}|{mutasidata[i]['stockout']:^17}|{mutasidata[i]['totalstock']:^16}|{status:^13}|")
    print('*' * 107)
    print('*' * 107)

# TEMPLETE TABEL HISTORY ADD ITEM
def recordHistoryAdd(addData):
    print('\n')
    print("============== RECORD HISTORY ADD ITEM STOK GUDANG NILAM'S ============== ")
    print('*' * 73)
    print('|KODE |\t    NAMA       |     KATEGORI   |   STOK   |\t   VENDOR   \t|')
    print('-------------------------------------------------------------------------')
    for item_list in addData:
        for data_dict in item_list:
            print(f"|{data_dict['code']:^5}|{data_dict['name']:16}|{data_dict['category']:16}|{data_dict['stock']:^10}|{data_dict['vendor']:20}|")

    print('*' * 73)
    print('*' * 73)

# TEMPLETE TABEL HISTORY DELETE ITEM
def recordHistoryDel(delData):
    print('\n')
    print("============== RECORD HISTORY DELETE ITEM STOK GUDANG NILAM'S ============== ")
    print('*' * 73)
    print('|KODE |\t    NAMA       |     KATEGORI   |   STOK   |\t   VENDOR   \t|')
    print('-------------------------------------------------------------------------')
    for data_dict in delData:
        print(f"|{data_dict['code']:^5}|{data_dict['name']:16}|{data_dict['category']:16}|{data_dict['stock']:^10}|{data_dict['vendor']:20}|")
    print('*' * 73)
    print('*' * 73)

# FILTER DICTIONARY DALAM STOK GUDANG
def searchItem(userInput):
    searchItem = list(filter(lambda data: data['code'] == userInput, stockGudang))
    return searchItem

# FUNGSI UNTUK MENGHIRAUKAN TANDA BACA DAN HURUF BESAR KECIL PADA VENDOR
def removePeriod(inputString):
    translator = str.maketrans('','','. ')
    return inputString.translate(translator)

# UPDATE BARANG BERDASARKAN KOLOM
def updateBarang(data, Key, newData):
    inputUpdateBarang = input('\n\tApakah Data Yang Diupdate Sudah Benar? (Ya/Tidak) ==>  ').lower()
    if inputUpdateBarang == 'ya':
        data[0][Key] = newData
        print('\n\t\t==== DATA SUDAH DIPERBARUI! ====')
    else:
        print('\n\t\t==== DATA TIDAK TER-UPDATE! ====')

# TAMPILKAN STOK GUDANG
def Read():
    inputSubMenu1 = input('''\n
        --------------------MENU TAMPILKAN DATA-------------------
         --------------pilih salah satu menu dibawah-------------
                                     
        1. Tampilkan Seluruh Data Stock Bulan Terakhir
        2. Tampilkan 1 Baris Data Stok Sesuai Kode yang Diinginkan
        3. Tampilkan Data Stock Berdasarkan Vendor
        4. Kembali ke Menu Utama

        Masukkan Menu yang Ingin Dijalankan : ''')
    if inputSubMenu1 == '1' and len(stockGudang) != 0:
        showTable(stockGudang)
        Read()
    elif inputSubMenu1 == '1' and len(stockGudang) == 0:
        print('\n\t\t=================== DATA STOK KOSONG ===================')
        Read()
    elif inputSubMenu1 == '2' and len(stockGudang) != 0:
        codeItem = input('\t== Masukkan Kode Barang yang Ingin Dicari : ')
        if len(searchItem(codeItem)):
            showTable(searchItem(codeItem))
        else:
            print('\n\t TIDAK ADA DATA')
        Read()
    elif inputSubMenu1 == '2' and len(stockGudang) == 0:
        print('\n\t\t=================== DATA STOK KOSONG ===================')
        Read()
    elif inputSubMenu1 == '3':
        vendors = input('\t== Masukkan Nama Vendor yang Ingin Dicari : ')
        cleanedVenInput = removePeriod(vendors).lower()
        searchVendors = list(filter(lambda data: removePeriod(data['vendor']).lower() == cleanedVenInput, stockGudang))
        if searchVendors:
            showTable(searchVendors)
        else:
            print('Data yang dimasukkan tidak valid/Data Kosong!')
        Read()
    elif inputSubMenu1 == '4':
        pass
    else:
        print('\n\t MENU YANG DIMASUKKAN TIDAK TERSEDIA!')
        Read()

# MENAMBAH DATA STOCK GUDANG
def Add():
    while True:
        inputSubMenu2 = input('''\n
        --------------------MENU MENAMBAH DATA-------------------
         -------------pilih salah satu menu dibawah-------------
                                    
        1. Menambah Data Barang
        2. Kembali ke Menu Utama

        Masukkan Menu yang Ingin Dijalankan : ''')

        if inputSubMenu2 == '1':
            showTable(stockGudang)
            while True:
                addStockCode = input('\n\t Masukkan Kode Barang Baru : ')
                if addStockCode.isdigit() and len(addStockCode) > 5:
                    print('\t==Maaf Kode Barang Tidak Boleh Lebih Dari 5 Digit==')
                elif not addStockCode.isdigit():
                    print('\t==Kode Barang Harus Dalam Angka!==')
                elif addStockCode.isdigit() and len(addStockCode) < 6:
                    listValue = [dataStock['code'] for dataStock in stockGudang]
                    if addStockCode in listValue:
                        print('\n\t=== DATA SUDAH ADA ===')
                    else:
                        itemName = input('\t Masukkan Nama Barang : ')
                        categoryItem = input('\t Masukkan Jenis Item : ')
                        valid_input = False
                        while not valid_input:
                            earlyStock = input('\t Masukkan Besar Stok Awal : ')
                            if earlyStock.isdigit() and len(earlyStock) < 4:
                                earlyStock = int(earlyStock)
                                valid_input = True
                            else:
                                print('\t== Maaf stok barang melebihi kuantitas atau Data Invalid. Masukkan angka untuk Stok Awal! ==')
                        vendorName = input('\t Masukkan Nama Vendor : ')
                        newItemList = [{
                            'code': addStockCode,
                            'name': itemName,
                            'category': categoryItem,
                            'stock': earlyStock,
                            'vendor': vendorName,
                        }]

                        showTable(newItemList)
                        save = input('\n\tSimpan Data (Ya/Tidak) ==>  ').lower()
                        if save == 'ya':
                            stockGudang.extend(newItemList)
                            showTable(stockGudang)
                            recordDataHistoryAdd.append(newItemList)
                            print('\n\t\t===DATA TERSIMPAN!===')
                        else:
                            print('\n\t\t===DATA TIDAK TERSIMPAN!===')

                    break

        elif inputSubMenu2 == '2':
            return  

        else:
            print('\n\tMENU YANG DIMASUKKAN TIDAK TERSEDIA!')

# MENGUBAH DATA STOCK GUDANG
def Update():
    inputSubMenu3 = input('''\n
        --------------------MENU UPDATE DATA---------------------
         -------------pilih salah satu menu dibawah-------------
                                     
        1. Update Data Barang
        2. Kembali ke Menu Utama

        Masukkan Menu yang Ingin Dijalankan : ''')
    
    if inputSubMenu3 == '1':
        showTable(stockGudang)
        updateStock = input('\n\t Masukkan Kode Item yang Ingin Diubah : ')
        listValue1 = [dataStock['code'] for dataStock in stockGudang]
        if updateStock not in listValue1:
            print('\n\t DATA YANG INGIN DIUBAH TIDAK TERSEDIA!')
            Update()
        else:
            searchItem(updateStock)
            showTable(searchItem(updateStock))
            inputUpdate = input('\nUpdate Data? (Ya/Tidak) ==>  ').lower()
            if inputUpdate == 'ya':
                inputKategori = input(''' 
        Kategori DataBase Gudang:
            1. Kode Barang
            2. Nama Barang
            3. Jenis Barang
            4. Stok Barang                        
            5. Nama Vendor                                     
        == Masukkan Kategori Yang Ingin Diubah : ''')
                while True: 
                    if inputKategori == '1'or inputKategori == 'kode barang':
                        valid_input = False
                        while not valid_input:
                            inputDataBaru = input('\n\t~~ Masukkan Kode Barang Baru: ')
                            if inputDataBaru in listValue1:
                                print('Kode Barang Sudah Digunakan!')
                            elif inputDataBaru.isdigit() and len(inputDataBaru) <= 5:
                                valid_input = True
                            elif inputDataBaru.isdigit() and len(inputDataBaru) >= 6:
                                print('Maaf, Kode Barang Tidak Boleh Lebih Dari 5 Digit')
                            elif not inputDataBaru.isdigit():
                                print('Kode Barang Harus Dalam Angka!')
                        updateBarang(searchItem(updateStock), 'code', inputDataBaru)
                    elif inputKategori == '2' or inputKategori == 'nama barang':
                        inputDataBaru = input('\n\t~~ Masukkan Nama Item Baru : ')
                        updateBarang(searchItem(updateStock), 'name', inputDataBaru)
                    elif inputKategori == '3'or inputKategori == 'jenis barang':
                        inputDataBaru = input('\n\t~~ Masukkan Jenis Barang Baru : ')
                        updateBarang(searchItem(updateStock), 'category', inputDataBaru)
                    elif inputKategori == '4' or inputKategori == 'stok barang':
                        inputStockINstr = input('\n\t~~ Masukkan Jumlah Stok Masuk : ')
                        inputStockOutstr = input('\n\t~~ Masukkan Jumlah Stock Keluar : ')

                        if inputStockINstr.isdigit() and inputStockOutstr.isdigit():
                            inputStockIN = int(inputStockINstr)
                            inputStockOUT = int(inputStockOutstr)

                            item = searchItem(updateStock)  
                            if item:
                                currentStock = int(item[0]['stock'])  
                                initialStock = currentStock
                                updatedStock = currentStock + inputStockIN - inputStockOUT
                                item[0]['stock'] = str(updatedStock)  
                                print('\n\t\t===Data stok sudah diperbarui===')
                                showTable(stockGudang)  

                                data_mutasi = {
                                    'code': item[0]['code'],
                                    'name': item[0]['name'],
                                    'stock' : initialStock,
                                    'stockin': inputStockIN,    
                                    'stockout': inputStockOUT,
                                    'totalstock': updatedStock
                                    }
                                recordDataMutasi.append(data_mutasi)

                            else:
                                print('Kode Barang Tidak Ditemukan')
                        else:
                            print('Data tidak valid')
                    elif inputKategori == '5' or inputKategori == 'nama vendor':
                        inputDataBaru = input('\n\t~~ Masukkan Nama Vendor Baru : ')
                        updateBarang(searchItem(updateStock), 'vendor', inputDataBaru)
                    else:
                        print('KATEGORI TIDAK TERSEDIA!')
                    break
            elif inputUpdate == 'tidak':
                print('\t\tDATA TIDAK TER-UPDATE!')
                Update() 
            else:
                print('\t\tMENU YANG DIMASUKKAN TIDAK VALID!')
            Update()

    elif inputSubMenu3 == '2':
        pass                      
    else:
        print('\n\t MENU YANG DIMASUKKAN TIDAK TERSEDIA!')
        Update()   

# RECORD KEGIATAN STOCK GUDANG
def RecordData():
    inputSubMenu4 = input('''\t
        --------------------MENU RECORD DATA---------------------
         -------------pilih salah satu menu dibawah-------------
                                     
        1. Tampilkan Tabel Record Mutasi Stok Gudang
        2. Tampilkan Tabel History Tambah dan Delete Item Stok Gudang
        3. Kembali ke Menu Utama

        Masukkan menu yang ingin dijalankan : ''')
    
    if inputSubMenu4 == '1':
        recordMutation(recordDataMutasi)
        RecordData()
    elif inputSubMenu4 == '2':
        while True:
            inputOptionTable = input('''
            ---- Pilih Salah Satu Menu ----- :
                                 
            1. Tampilkan Tabel History ADD Stok
            2. Tampilkan Tabel History DELETE Stok
            3. Kembali Ke Sub Menu
                                 
            Masukkan menu yang ingin dijalankan : ''')
            if inputOptionTable == '1':
                recordHistoryAdd(recordDataHistoryAdd)
                continue
            elif inputOptionTable == '2':
                recordHistoryDel(recordDataHistoryDel)
                continue
            elif inputOptionTable == '3':
                break
            else:
                print('Menu Tidak Tersedia')
                pass
        RecordData()
    elif inputSubMenu4 == '3':
        pass
    else:
        print('\n\t MENU YANG DIMASUKKAN TIDAK TERSEDIA!')
        RecordData()

# MENGHAPUS DATA STOCK GUDANG
def Delete():
    inputSubMenu5 = input('''\t
        --------------------MENU DELETE DATA---------------------
         -------------pilih salah satu menu dibawah-------------
                                     
        1. Hapus Data Barang
        2. Kembali ke Menu Utama

        Masukkan menu yang ingin dijalankan : ''')
    
    if inputSubMenu5 == '1':
        showTable(stockGudang)
        delCode = input('\nMasukkan Kode Barang Yang Ingin Dihapus : ')
        listValue2 = [dataStock['code'] for dataStock in stockGudang]
        if delCode not in listValue2:
            print('\n\t DATA YANG INGIN DIHAPUS TIDAK ADA!')
        else:
            searchItem(delCode)
            showTable(searchItem(delCode))
            delData = (input('\n\t Hapus Data? (Ya/Tidak) ==>  ')).lower()
            if delData == 'ya':
                for listItem in searchItem(delCode):
                    stockGudang.remove(listItem)
                    recordDataHistoryDel.append(listItem)
                print('\n\t\t==DATA BERHASIL DIHAPUS!==')
                
            else:
                print('\n\t\t==DATA TIDAK BERHASIL DIHAPUS!==')
            Delete()
    elif inputSubMenu5 == '2':
        pass
    else:
        print('\n\t==MENU YANG DIMASUKKAN TIDAK TERSEDIA!==')
        Delete()

# FUNCTION MAIN MENU
def selectMenu():
    while True:  
        Menu()
        pilihanMenu = input('Masukkan Menu Yang Ingin Dijalankan : ') 
        if pilihanMenu == '1':
            Read()
        elif pilihanMenu == '2': 
            Add()
        elif pilihanMenu == '3':  
            Update()
        elif pilihanMenu == '4':  
            Delete()
        elif pilihanMenu == '5':
            RecordData()
        elif pilihanMenu == '6':    
            print('\n\t========== TERIMA KASIH SUDAH MENGGUNAKAN PROGRAM INI ==========')
            print()
            break
        else:
            print('\n\t==MENU YANG DIMASUKKAN TIDAK TERSEDIA!==')      
selectMenu()


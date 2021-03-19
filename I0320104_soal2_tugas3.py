# Program Dictionary

dict = {'Nama':'Truely', 'Hobi1':'Membaca', 'Hobi2':'Berenang', 'Hobi3':'Traveling', 'Hobi4':'Menulis', 'Sosmed1': 'Ig:@truely.hfdz', 'Sosmed2':'line:@truelyhafidz', 'Sosmed3':'fb:@truelyhafidz', 'Lagu1':'Gajah', 'Lagu2':'Tiba-tiba', 'Lagu3':'senyumlah', 'Makanan1':'bakso', 'Makanan2':'Mie', 'Makanan3':'tempe', 'Makanan4':'ayam'}
print("Dict:", dict)

# Mengubah salah satu hobi dan sosial media
dict['Hobi2'] = 'olahraga'
dict['Sosmed3'] = 'Ig : uly.truely'
print("Dict setelah diubah:", dict)

# Menghapus 2 makanan favorit
del dict['Makanan1']
del dict['Makanan2']
print("dict:", dict)

# Menambahkan 1 hobi
dict['Hobi5'] = 'makan'
print("dict:", dict)
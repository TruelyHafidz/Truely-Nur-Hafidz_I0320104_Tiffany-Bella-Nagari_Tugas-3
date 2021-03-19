# Program List untuk Menyimpan Nama Teman

list_teman = ['Desy', 'Pincen', 'Ara', 'Yuki', 'Sekar', 'Zaneta', 'Sasa', 'Yola', 'Raysa', 'Putri']
print("Temanku:", list_teman)

# Menampilkan isi list indeks nomor 4, 6, 7
print("Temanku:", list_teman[4], ",", list_teman[6], ",", list_teman[7])

# Mengganti nama teman pada list 3, 5, 9
list_teman[3] = 'Ica'
list_teman[5] = 'Ryan'
list_teman[9] = 'Retno'
print("Temanku setelah diganti:", list_teman)

# Menambahkan 2 teman
list_teman.append('Efa')
list_teman.append('Hafizh')
print("Temanku setelah ditambah:", list_teman)

# Menampilkan list teman dengan perulangan
print("Temanku:", list_teman * 1000)

# Menampilkan panjang list teman
print("Panjang list Temanku:", len(list_teman) )
print("Panjang list Temanku perulangan:", len(list_teman *1000))

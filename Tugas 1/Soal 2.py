# Mendefinisikan fungsi untuk memeriksa ganjil dan pembagian 3
def cek_ganjil_dan_pembagian_tiga(bilangan):
    if bilangan % 2 == 0:
        return "genap"
    else:
        if bilangan % 3 == 0:
            return "ganjil dan bisa dibagi 3"
        else:
            return "ganjil dan tidak bisa dibagi 3"

# List bilangan
bilangan_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Menggunakan loop untuk memeriksa setiap bilangan dalam list
for bilangan in bilangan_list:
    print(f"{bilangan} adalah bilangan {cek_ganjil_dan_pembagian_tiga(bilangan)}")

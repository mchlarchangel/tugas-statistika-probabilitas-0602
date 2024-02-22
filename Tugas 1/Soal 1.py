def cek_huruf(huruf):
    # List huruf vocal
    vocal = ['a', 'i', 'u', 'e', 'o']

    # Mengubah huruf menjadi huruf kecil untuk memudahkan pengecekan
    huruf = huruf.lower()

    # Memeriksa apakah huruf merupakan vocal atau konsonan
    if huruf in vocal:
        print(f"{huruf} adalah huruf vocal")
    else:
        print(f"{huruf} adalah huruf konsonan")

# Input huruf
huruf_input = input("Masukkan huruf: ")

# Memanggil fungsi untuk memeriksa huruf
cek_huruf(huruf_input)
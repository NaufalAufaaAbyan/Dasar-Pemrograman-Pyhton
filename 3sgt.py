# Fungsi untuk menghitung luas segitiga
def hitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

# Input dari pengguna
alas = float(input("Masukkan panjang alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))

# Menghitung luas
luas = hitung_luas_segitiga(alas, tinggi)

# Menampilkan hasil
print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas}")
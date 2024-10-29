# List A
A = [2, 2, 1, 3, 5, 5, 5, 7, 2, 10]

# Fungsi untuk mencari nilai x, jumlah kemunculannya, dan indeks-indeksnya
def cari_nilai_x(A, x):
    indeks = [i for i, nilai in enumerate(A) if nilai == x]
    jumlah_kemunculan = len(indeks)
    return jumlah_kemunculan, indeks

# Input dari pengguna
x = int(input("Masukkan nilai x: "))

# Mencari dan menampilkan jumlah kemunculan dan indeks-indeks di mana nilai x muncul
jumlah_kemunculan, indeks_x = cari_nilai_x(A, x)

if jumlah_kemunculan > 0:
    print(f"Nilai {x} muncul sebanyak {jumlah_kemunculan} kali pada indeks: {indeks_x}")
else:
    print(f"Nilai {x} tidak ditemukan di dalam list.")

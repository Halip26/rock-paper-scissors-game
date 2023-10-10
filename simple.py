import random

# Dictionary yang mengaitkan karakter input dengan pilihan permainan
my_dict = {"R": "Batu", "P": "Kertas", "S": "Gunting"}

# Inisialisasi skor pengguna dan komputer
user_count = 0
comp_count = 0

# Meminta pengguna untuk memasukkan jumlah permainan yang ingin dimainkan
games = int(input("\nMasukkan jumlah permainan yang ingin Anda mainkan: "))

# Melakukan perulangan sampai jumlah total permainan mencapai jumlah yang diinginkan
while games > 0:
    games -= 1

    # Meminta input dari pengguna dan mengonversinya menjadi huruf kapital
    user_input = input("\nInput Pengguna: ")[0].upper()

    # Memeriksa apakah input pengguna valid (ada dalam kamus)
    if user_input not in my_dict:
        print("INPUT TIDAK VALID")
        continue

    # Menghasilkan input komputer secara acak menggunakan kunci kamus
    comp_input = random.choice(list(my_dict.keys()))

    # Mencetak input komputer
    print("Input Komputer: ", my_dict[comp_input])

    # Memperbarui skor berdasarkan aturan permainan
    if (
        (user_input == "R" and comp_input == "P")
        or (user_input == "P" and comp_input == "S")
        or (user_input == "S" and comp_input == "R")
    ):
        comp_count += 1
    elif (
        (user_input == "P" and comp_input == "R")
        or (user_input == "S" and comp_input == "P")
        or (user_input == "R" and comp_input == "S")
    ):
        user_count += 1
    else:
        print("SERI")

    # Mencetak skor saat ini
    print("\nSKOR:")
    print("Skor Pengguna:", user_count, "\tSkor Komputer:", comp_count, "\n")

print("\n\t\tSKOR AKHIR:")
print("Skor Pengguna:", user_count, "\t\tSkor Komputer:", comp_count, "\n")

# Memeriksa dan mencetak pemenang atau hasil seri
if user_count > comp_count:
    print("\n\tSELAMAT! ANDA MENANG!")
elif user_count < comp_count:
    print("\n\t\tMAAF! ANDA KALAH!")
else:
    print("\n\t\tOOPS! INI SERI!")

import os
from datetime import datetime
#waktu
jam_masuk = datetime.now().strftime("%H:%M:%S")
#cetak struk
def cetak_struk(jam_masuk):
    with open("struk_parkir.txt", "w") as file:
        file.write("\n" + "="*20)
        file.write("\n   STRUK PARKIR   ")
        file.write("\n" + "="*20)
        file.write(f"\nJam Masuk: {jam_masuk}")
        file.write(f"\nTerima kasih telah menggunakan layanan parkir kami!")

#main
print("=" * 20)
print("Secure parking os")
print("=" * 20)
print("Selamat datang")
print("1. Parkir Mobil")
print("2. Parkir Motor")
print("3. Keluar")

pilihan = input("Masukan pilihan (1/2/3): ")

if pilihan == "1":
    jam_masuk = datetime.now().strftime("%H:%M:%S")
    print(f"Mobil parkir pada jam {jam_masuk}.")
    cetak_struk(jam_masuk)

elif pilihan == "2":
    print(f"Motor parkir pada jam {jam_masuk}.")
    cetak_struk(jam_masuk)

elif pilihan == "3":
    print("Selamat datang di mall bg juction")

import os
#cetak struk

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
    jam_masuk = input("Masukan jam masuk (HH:MM): ")
    print(f"Mobil parkir pada jam {jam_masuk}.")

elif pilihan == "2":
    jam_masuk = input("Masukan jam masuk (HH:MM): ")
    print(f"Motor parkir pada jam {jam_masuk}.")

elif pilihan == "3":
    print("Selamat datang di mall bg juction")
print("=== Mengidentifikasi Segitiga dan luasnya ===")
print(" ")
sisi_a = int(input("Masukkan Sisi A: "))
sisi_b = int(input("Masukkan Sisi B: "))
sisi_c = int(input("Masukkan Sisi C: "))

print(" ")
# MENGHITUNG LUAS DENGAN RUMUS HERON
setengah_luas = ((sisi_a + sisi_b) + sisi_c) / 2
luas = (setengah_luas * (setengah_luas - sisi_a) * (setengah_luas - sisi_b) * (setengah_luas - sisi_c)) ** 0.5

if (sisi_a + sisi_b > sisi_c) and (sisi_b + sisi_c > sisi_a) and (sisi_c + sisi_a > sisi_b) :
    if sisi_a == sisi_b == sisi_c:
        print("Segitiga Sama Sisi")
    elif (sisi_a == sisi_b) or (sisi_a == sisi_c) or (sisi_b == sisi_c):
        print("Segitiga Sama Kaki")
    elif sisi_a != sisi_b != sisi_c:
        print("Segitiga Sembarang")
    print(f"Hasil luasnya adalah: {luas}")
else:
    print("Bukan Segitiga.")

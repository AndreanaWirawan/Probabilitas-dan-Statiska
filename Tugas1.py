biodata = ['Nama : I putu andreana wirawan','Nim : D0221068','Kelas : informatika E\n']
for i in biodata:
    print(i)
print('Soal'.center(50, " "))
soal = ['1. Mencari nilai mean','2. Mencari nilai modus','3. Mencari nilai median']
for i in soal:
    print(i)
print()
print("Penyelesaian".center(50, " "))
    
print("1. Mencari nilai mean")
angka = [0, 2, 2, 10, 6, 8]
jumlah_angka = 0
for i in angka:
    jumlah_angka += i

mean = jumlah_angka / len(angka)
print("Nilai mean dari",angka, "adalah:", mean)
print()

print("2. Mencari nilai modus")
nim = [0, 2, 2, 10, 6, 8]
tampungan = {}
for i in nim:
    if i in tampungan:
        tampungan[i] += 1
    else:
        tampungan[i] = 0
modus = None
tampungan_tertinggi = 0
for k, j in tampungan.items():
    if j > tampungan_tertinggi:
        modus = j
        tampungan_tertinggi = j
print("Modus dari nim", nim, "adalah = ", modus)
print()

print("3. Mencari nalai median")
data = [0,2,2,10,6,8]
if len(data) % 2 == 0 :
    print("Nilai median dari" ,data, "tersebuat adalah GENAL")
else:
    print("Nilai median dari",data, " tersebut adalah GANJIL")

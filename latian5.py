data = []

while True:
        Nama = input("nama : ")
        nim = input("nim : ")
        tugas = int(input("nilai tugas :"))
        uts = int(input("nilai uts :"))
        uas = int(input("nilai uas :"))
        akhir = float(tugas  * 30 / 100) + (uts * 35 / 100) + (uas * 35 / 100)
        data.append ([Nama, nim, tugas, uts, uas, int(akhir)])
        Lagi = input ("tambah lagi (y/t)?")
        if Lagi.lower() =="t":
            break

print("\n                               Daftar nilai mahasiswa")
print("===============================================================")
print("| No | Nama     | NIM  |tugas  |  UTS  | UAS  | AKHIR  |")
print("===============================================================")
i = 0
for nilai in data:
        i += 1
        print("|  {no:2d}  |  {nama:12s}  |  {nim:9s}  |  {tugas:5d}  |  {uts:5d}  |  {uas:5d}  |  {akhir:6.2f} | " .format(no=i, nama=nilai[0], nim=nilai[1], tugas=nilai[2], uts=nilai[3], uas=nilai[4], akhir=nilai[5]))

print("=================================================================")
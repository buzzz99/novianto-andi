data = [11,12,13,18,19]
print ("menampilkan semua list:", data[0:6])
print ("element ke 3 : ", data[2])
print ("element ke 2 sampai ke 4 :", data[1:4])

data[3] = 20
print("mengubah element 4 : ",data)
data[4:5] = 90,50
print("mengubah element 4 dan terkahir : ",data)
print("=====================================================================")

dataa = [11,23,26]
datab = [29,19,69]
print("list a : ",dataa)
print("list b: ",datab)
datab.append(99)
print("menambahkan list B nilai string : ", datab)
datab.extend([60,70,80])
print("menambahkan list b dengan 3 nilai ", datab)
print("menggabungkan list a dan b :", dataa + datab )

print("=======================================================================")
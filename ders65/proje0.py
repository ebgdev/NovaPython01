kisi_sayisi = int(input("kac kisinin ortalamasini gireceksiniz ? "))
# print("kisi sayisi = ",kisi_sayisi)

total = 0
for i in range(kisi_sayisi): # ornek: range(4): 0, 3
    puan = int(input(f"{i+1}.kisinin ortalamasini giriniz: "))
    total += puan


ortalama = total/kisi_sayisi

print(f"sinif ortalamasi : {ortalama}")

if ortalama % 2 == 0:
    print(f"ortalama yaklasik: {int(ortalama)} ve cift")
else:
    print(f"ortalama yaklasik: {int(ortalama)} ve tek")

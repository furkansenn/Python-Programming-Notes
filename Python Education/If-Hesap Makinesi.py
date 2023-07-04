print("""Hesap Makinesi

[1] Toplama
[2] Çıkarma
[3] Çarpma
[4] Bölme
[5] Üs Alma
[Q] Çıkış
""")

islem=input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz")

if islem=="1":
    sayı1=float(input("Lütfen İlk Sayıyı Giriniz:"))
    sayı2=float(input("Lütfen İkinci Sayıyı Giriniz"))
    print("Toplama İşleminizin Sonucu {}".format(sayı1+sayı2))
elif islem=="2":
    sayı1=float(input("Lütfen İlk Sayıyı Giriniz:"))
    sayı2=float(input("Lütfen İkinci Sayıyı Giriniz"))
    print("Çarpma İşleminizin Sonucu {}".format(sayı1*sayı2))
elif islem=="3":
    sayı1=float(input("Lütfen İlk Sayıyı Giriniz:"))
    sayı2=float(input("Lütfen İkinci Sayıyı Giriniz"))
    print("Çarpma İşleminizin Sonucu {}".format(sayı1*sayı2))
elif islem=="4":
    sayı1=float(input("Lütfen İlk Sayıyı Giriniz:"))
    sayı2=float(input("Lütfen İkinci Sayıyı Giriniz"))
    print("Bölme İşleminizin Sonucu {}".format(sayı1/sayı2))
elif islem=="5":
    sayı1=float(input("Lütfen İlk Sayıyı Giriniz:"))
    sayı2=float(input("Lütfen İkinci Sayıyı Giriniz"))
    print("Üs Alma İşleminizin Sonucu {}".format(sayı1**sayı2))
elif islem=="Q" or islem=="q":
    print("Hoşçakalın...")

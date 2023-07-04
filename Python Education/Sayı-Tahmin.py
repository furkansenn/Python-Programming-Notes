Sayı=25
Hak=10

while Hak>0:
    Tahmin=int(input("Lütfen Pozitif Bir Tam Sayı Giriniz:"))
    if Tahmin<0:
        print("Girdiğiniz Sayı Pozitif Bir Tam Sayı Değildir!!!!")
        continue
    Hak-=1
    if Sayı==Tahmin:
        print("Doğru Tahmin Ettiniz, Tebrikler (: ")
        break
    elif Sayı>Tahmin:
        print("Yukarı, Kalan Hakkınız {}".format(Hak))
    else:    
        print("Aşağı, Kalan Hakkınız {}".format(Hak))
    if Hak==0:
        print("Hakkınız Kalmamıştır :(.Doğru Sayı {} olacaktır.".format(Sayı))
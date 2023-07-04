def Toplam(x,y):
    sonuc=x+y
    print(sonuc)

Toplam(5,7)


def Usalma(x,y):
    sonuc=x**y
    print(sonuc)

Usalma(9,6)

print(pow(9,6))# Üstte bunu direk yazmak yerine nasıl fonksiyonunu kuracağımızı yaptım.

#Mesela bir örnek yapalım:

def Resitlikhesapla(x):
    Yas = 2022 - x     
    if Yas<18:
        print("Yaşınız [0] Reşit değilsiniz!!!", Yas)   #print(f"Yaşınız {Yas} Reşit değilsiniz!!!) Farklı yazma yöntemleri(3 tane var)
    else:                                          
        print("Yaşınız {} Reşitsiniz!!!".format(Yas))

Resitlikhesapla(int(input("yılı giriniz: ")))


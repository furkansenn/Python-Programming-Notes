Sayi=int(input("Lütfen Bir Sayı Giriniz:"))
Kontrol=(Sayi>0) and (Sayi%2==1)

if Kontrol==True:
    print("{} pozitif bir tek sayıdır!".format(Sayi))
else:
    print("{} pozitif bir tek sayı değildir".format(Sayi))
    
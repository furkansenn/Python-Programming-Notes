print("Merhaba, Vücut Kitle Endeksi Hesaplama Uygulamasına Hoş geldiniz!!")

Boy=int(input("Lütfen Boyunuzu Cm Cinsinden Giriniz:"))
Kilo=int(input("Lütfen Kilonuzu Giriniz:"))

Endeks=round(((Kilo)/(Boy/100)**2),2) #round virgülden sonra kaç basamağın yazılmasını söyler

if Endeks<=18.5:
    print("Vücut Kitle Endeksiniz {}'dir.Düşük Kilolu Grubundansınız!".format(Endeks))
elif Endeks>18.5 and Endeks<=24.9:
    print("Vücut Kitle Endeksiniz {}'dir.Normal Kilolu Grubundansınız!".format(Endeks))
elif Endeks>25 and Endeks<=29.9:
    print("Vücut Kitle Endeksiniz {}'dir.Fazla Kilolu Grubundansınız!".format(Endeks))
elif Endeks>30 and Endeks<=40:
    print("Vücut Kitle Endeksiniz {}'dir.Obez Kilolu Grubundansınız!".format(Endeks))








#Videoda cmd üzerinden çalıştırdık
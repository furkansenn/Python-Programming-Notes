from multiprocessing.sharedctypes import Value


def Toplam(*x):
    sayac = 0
    for i in x:
        sayac += 1
    return sayac

print(Toplam(2,3,5,100,1000))

def isim(*x):
    return "Merhaba,benim adım {},soyadım {}".format(x[0],x[1])

print(isim("Furkan","Şen"))

def kalori(**meyve):
    return meyve

print(kalori(Elma=45,Armut=50))

def kimlik(**bilgi):
    for i in bilgi.items():  #Eğer değerleri isteseydik keys yerine values yazmalıydık.
        print(i)

kimlik(Ad="Furkan",Soyad="Şen", Yas=20)

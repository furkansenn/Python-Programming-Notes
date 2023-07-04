# class Insan:
#     pass

# x=Insan()
# print(type(x))

from ast import alias


class Insan:
    Ad="Furkan"
    Soyad="Şen"
    Yas=20
    Sacrengi="Siyah"

# print(Insan.Ad)
# print(Insan.Sacrengi)

#Eğer birden fazla bilgi girilecekse alttaki yapılır.Özel bir parametre kullanılır.

class Insan:
    def __init__(self,Ad,Soyad,Yas,Sacrengi):
        self.Ad=Ad 
        self.Soyad=Soyad
        self.Yas=Yas
        self.Sacrengi=Sacrengi

Insan1=Insan("Kel","Mahmut",44,"Siyahamayok")
Insan2=Insan("Burak","Şen",24,"Kumral")

print(Insan1.Sacrengi)
print(Insan2.Sacrengi)


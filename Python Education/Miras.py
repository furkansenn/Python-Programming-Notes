class Insan:
    def __init__(self,Ad,Soyad,Sacrengi,Boy,Kilo):
        self.Ad=Ad
        self.Soyad=Soyad
        self.Sacrengi=Sacrengi
        self.Boy=Boy
        self.Kilo=Kilo

#Bir sınıfa ait değişkenleri tekrar tekrar yazmamak için (Miraslama)

class Ogrenci(Insan):
    def __init__(self, Ad, Soyad, Sacrengi, Boy, Kilo, Yas, Bolum):
        super().__init__(Ad, Soyad, Sacrengi, Boy, Kilo)
        self.Yas=Yas
        self.Bolum=Bolum

Insan1=Insan("Enes","Sen","Kumral",190,80)
Ogrenci1=Ogrenci("Furkan","Sen","Siyah",170,60,20,"Fen")

print(Insan1.Kilo)
print(Ogrenci1.Bolum)




class Insan:
    def __init__(self,Ad,Soyad,Dogumyıl):
        self.Ad=Ad
        self.Soyad=Soyad
        self.Dogumyıl=Dogumyıl

    def bilgi(self):
        print("Merhaba benim adım {},soyadım {}. {} yılında doğdum".
        format(self.Ad,self.Soyad,self.Dogumyıl))

    def Yas(self):
        return 2022-self.Dogumyıl


Insan1=Insan("Ahmet","Can",1997)
Insan2=Insan("Mehmet","Enayi",2002)

Insan1.bilgi()
Insan2.bilgi()

print(Insan1.Yas())
print(Insan2.Yas())



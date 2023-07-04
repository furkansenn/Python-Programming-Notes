class Memur:
    def __init__(self,Ad,Soyad,Maas):
        self.Ad=Ad
        self.Soyad=Soyad
        self.__Maas=Maas
        self.__Zam=0.20

#Eğer __ atarsam bunu gizlemiş olurum.
#Fakat get metodu kullanırsak maas kapsüllü olduğu halde bilgiyi görebilmek için kullanıyoruz
#Set metoduyla ile de kapsüllü değeri değiştirebiliyoruz.

    def zamoranı(self):
        self.__Maas=self.__Maas+self.__Maas*self.__Zam

    def getMaas(self):
        return self.__Maas

    def getZam(self):
        return self.__Zam

    def setZam(self,Yenioran):
        self.__Zam=Yenioran

Memur1=Memur("Furkan","Şen",1000)

Memur1.setZam(0.50)
Memur1.zamoranı()
print(Memur1.getMaas())
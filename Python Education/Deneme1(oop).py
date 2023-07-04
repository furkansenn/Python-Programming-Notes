# class Ogrenci:
#     def __init__(self,name,studentnumber,grade, dg):
#         self.name=name
#         self.studentnumber=studentnumber
#         self.grade=grade
#         self.dg=dg
    
#     def bilgi (self):

#         print("Benim adım {}, numaram {}, notum {}. ".
#         format(self.name,self.studentnumber,self.grade))
    
#     def yas (self):

#         return 2022-self.dg
        

# Ogrenci1=Ogrenci("hakan",150317054,95,1998)
# Ogrenci1.bilgi()

# print(Ogrenci1.yas())


# # class Memur:
# #     def __init__(self, ad,soyad,maas):

# #         self.ad=ad
# #         self.soyad=soyad
# #         self.__maas=maas
# #         self.__zam=0.20

# # class Insan(Memur):
# #     def __init__(self, ad, soyad, maas):
# #         super().__init__(ad, soyad, maas)
    
    
    


# #     def getmaas(self):
# #         return self.__maas

# #     def getzam(self):
# #         return self.__zam

# #     def setzam(self,yenioran):
# #         self.__zam=yenioran

# #     def zamorani(self):
# #        self.__maas=self.__maas+self.__maas*self.__zam


# # Memur1=Memur("Hakan","Fidan",3000)


# # Memur1.setzam(0.5)
# # Memur1.zamorani()
# # print(Memur1.getmaas())


# def kontrol(x):
    
#         if len(x)<5:
#             raise Exception("Şifreniz 5 karakterden yüksek olmalı")

#         else:
#             print("doğru yazdın")
# while True:
#     try:
#         x=input("Lütfen bir şifre giriniz")
#         kontrol(x)
#     except Exception as baba:
#         print(baba)
#     else:
#         break

# def fonksiyon1(fonksiyon):
#     def x():
#         print("Eklemek İsteiğimiz Alan")
#         fonksiyon()
#         print("Eklemek İst. Alan")
#     return x

# @fonksiyon1
# def Selam():
#     print("Merhaba")

# Selam()

def fonksiyon1():
    print("Merhabalar")
    
    def fonksiyon2():
        print("Nasılsınız")
    return fonksiyon2()

fonksiyon1()
# def toplam(x,y):
#     sonuc=x+y
#     return sonuc
# print(toplam(2,7))

#Alttaki üsttekinin kısa yoludur

toplam=lambda x,y:x+y
print(toplam(2,7))

Kare=lambda sayı:sayı**4
Liste=[1,3,5,7,9]
sonuc=list(map(Kare,Liste))

print(sonuc)
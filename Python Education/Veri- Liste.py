Bilgi=["Furkan","Recep",88]
print(Bilgi[1])

Bilgi2=["kadıköy","ıstanbul",12]

Bilgi3=[Bilgi,Bilgi2]
print(Bilgi3)

print(len(Bilgi))


#Liste Veri Tipi Örnekleri

#Ürünler İsminde Televizyon,Buzdolabı,Bilgisayar,Fırın
Ürünler=["Televizyon","Buzdolabı","Bilgisiyar","Fırın"]
print(Ürünler)

#Kaç adet ürünümüz var?
print(len(Ürünler))

#Ürünlerimizin ilk 2 ürününün adı ?
print(Ürünler[0:2])

#İlk ve Sonuncu ürünlerimiz hangisidir?
print(Ürünler[0],Ürünler[len(Ürünler)-1])

#Fırın ile Ütü değişimi olsun.
Ürünler[len(Ürünler)-1]="Ütü"
print(Ürünler)

#Ürünler listemize Çamaşır Makinesi ekleyelim.
Ürünler=Ürünler+["Çamaşır Makinesi"]
print(Ürünler)
#Ürünler listesini tersten yazdıralım.
print(Ürünler[::-1])

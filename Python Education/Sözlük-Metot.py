Bilgi={
        "Ad":"Anlaşılır",
        "Soyad":"Ekonomi",
        "DYer":"Ankara",
        "TCno":14121111111
}
# print(Bilgi.keys()) Sözlükte anahtarları yazar

# print(Bilgi.values()) Değerleri yazar
 
print(Bilgi.items())  #Hem keyi hem de valueyi eşleştirir.

# print(Bilgi.get("Ad")) Anahtarın karşılığına gelen değeri gösteriri.

# print(Bilgi.update({"Cinsiyet":"Erkek"}))
# print(Bilgi)  Ekleme yaparken kullanılır.

# Bilgi2=Bilgi.copy()
# print(Bilgi2)  kopyalar

# print(Bilgi.__len__()) Kaç adet çift var yani değer ve key

# Bilgi.pop("TCno") Anahtarı siler
# print(Bilgi) 

# Bilgi.clear()  Temizler 
# print(Bilgi)



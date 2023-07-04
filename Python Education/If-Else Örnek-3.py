İsim=str(input("Lütfen Adınızı Giriniz:"))
Yas=int(input("Lütfen Yaşınızı Giriniz:"))
Egitim=str(input("Lütfen Eğitim Durumunuzu Giriniz:"))
Egitim2=("İlkokul","Ortaokul","Lise","Üniversite")

if Egitim not in Egitim2:
    print("Lütfen Geçerli Bir Eğitim Durumu Giriniz")
elif (Yas>=18) and (Egitim=="Lise" or Egitim=="Üniversite"):
    print("Ehliyet Şartları Geçildi!!!!")
else:
    print("Ehliyet Şartları Gerçekleşmiyor!!!")
# x="Anlaşılır Ekonomi"  
# for i in x:
#     if i==" ":
#         break #Bu kısım continue olsaydı eğer ara verip boşluğu görmeden ilerlerlerdi
#     print(i)
#Yani boşluğu gördüğü an break ile duruyor
# A  
# n
# l
# a
# ş
# ı
# l
# ı
# r

Sayac=2
for i in range(0,3):

    Kullanıcı_Adı=input("Kullanıcı Adı:")
    Kullanıcı_Sif=input("Kullancı Sifre:")
    SistemKA="Anlaşılır Ekonomi"
    SistemSif="123456"

    if Kullanıcı_Adı==SistemKA and Kullanıcı_Sif==SistemSif:
        print("Giriş Başarılı, Hoş geldiniz")
        break
    elif (Kullanıcı_Adı!=SistemKA or Kullanıcı_Sif!=SistemSif) and Sayac!=0:
        print("Hatalı Giriş.Lütfen Tekrar Deneyiniz.Kalan Hakkınız {}.".format(Sayac))
        Sayac=Sayac-1
    else:
        print("Kalan Kullanım Hakkınız {} Kapatılıyor...".format(Sayac))

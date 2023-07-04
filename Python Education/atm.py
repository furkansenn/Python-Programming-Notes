print("""\t******Merhabalar XBank'e Hoşgeldiniz******
\t\tLütfen Kartınızı Takınız""")

Veritabanı={"AhmetHesap":{
    "İsim":"Ahmet",
    "Soyisim":"Candan",
    "Kartsifre":"1357",
    "HesapBakiye":5000,
    "KrediKartBorc":4200,
    "KrediKartBorcTarih":"20/11/2021"},
            "MehmetHesap":{
    "İsim":"Mehmet",
    "Soyisim":"Duyar",
    "Kartsifre":"2468",
    "HesapBakiye":6000,
    "KrediKartBorc":3800,
    "KrediKartBorcTarih":"28/11/2021"}}


TakılanKart=dict(Veritabanı["AhmetHesap"])

Hak=2
for i in range(0,3):
    Sifre=input("Lütfen 4 haneli Şifrenizi Giriniz")
    if Sifre==TakılanKart.get("Kartsifre"):
        print("""Merhaba, Hoşgeldiniz Sayın {} {}
        Lütfen yapmak istediğiniz işlemi seçiniz...""".
        format(TakılanKart.get("İsim"),TakılanKart.get("Soyisim")))
        Sec=input("""
        [1] Bakiye Sorgulama
        [2] Kredi Kartı Borcu Sorgulama
        [3] Para Çekme
        [4] Para Yatırma
        [Q] Kart İade\n""")
        break
    elif Sifre!=TakılanKart.get("Kartsifre") and Hak!=0:
        print("Hatalı Şifre Girdiniz. Kalan Hakkınız {}".format(Hak))
        Hak=-1
    elif Sifre!=TakılanKart.get("Kartsifre") and Hak==0:
        print("""Şifrenizi 3 Defa Hatalı Girdiğinizden Dolayı Kartınız Bloke Olmuştur.
        Lütfen En Yakın Şubemize Başvurunuz!!!""")
        exit()

if Sec=="1":
    print("""Hesap Bakiyeniz {} TL'dir""".format(TakılanKart.get("HesapBakiye")))
elif Sec=="2":
    print("""Kredi Kartı Borç Bakiyeniz: {} Son Ödeme Tarihli {} TL'dir.""".
    format(TakılanKart.get("KrediKartBorcTarih"),TakılanKart.get("KrediKartBorc")))
elif Sec=="3":
    Miktar1=int(input("Lütfen Çekilecek Tutarı Giriniz:"))
    if TakılanKart.get("HesapBakiye")<Miktar1:
        print("Yetersiz Bakiye")
    else:
        print("Lütfen Paranızı Kontrol Ederek Alınız...")
        YeniBakiye1=TakılanKart.get("HesapBakiye")-Miktar1
        print("Geriye Kalan Bakiyeniz {} TL'dir".format(YeniBakiye1))
elif Sec=="4":
    Miktar2=int(input("Lütfen Yatırılacak Tutarı Giriniz:"))
    print("Paranız Hesabınıza Yatırılmıştır. Teşekkür Ederiz...")
    YeniBakiye2=TakılanKart.get("HesapBakiye")+Miktar2
    print("Geriye Kalan Bakiyeniz {} TL'dir".format(YeniBakiye2))
elif Sec=="Q" or Sec=="q":
    print("Teşekkür Eder, İyi Günler Dileriz...")
    exit()
else:
    print("Lütfen Geçerli Bir Giriş Yapınız!!!")


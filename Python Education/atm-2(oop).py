class Musteri:
    def __init__(self,ad,soyad,kartsifre,hesapbakiye,kredikartborc,sonodeme):
        self.ad=ad
        self.soyad=soyad
        self.kartsifre=kartsifre
        self.hesapbakiye=hesapbakiye
        self.kredikartborc=kredikartborc
        self.sonodeme=sonodeme
Ahmethesap=Musteri("Ahmet","Candan","1357",5000,4200,"20/11/2021")
Mehmethesap=Musteri("Mehmet","Duyar","2468",6000,3800,"28/11/2021")
Takılankart=Ahmethesap
 

class ATM:
    def __init__(self,atmad):
        self.atmad=atmad
        self.giriskontrol()
        self.dongu=True

    def giriskontrol(self):
        Hak=2
        for i in range(0,3):
            Sifre=input("Lütfen 4 Haneli Şifrenizi Giriniz:")
            if Sifre==Takılankart.kartsifre:
                self.program()
            elif Sifre!=Takılankart.kartsifre and Hak!=0:
                print("Hatalı Şifre Girdiniz.Kalan Hakkınız {}".format(Hak))
                Hak-=1
            elif Sifre!=Takılankart.kartsifre and Hak==0:
                print("Şifrenizi 3 Defa Hatalı Giridiğinizden Dolayı Kartınız Bloke OLmuştur.Lütfen En Yakın Şubemize Başvurunuz!!!")
                exit()

    def program(self):
        secim=self.menu

        if secim==1:
            self.bakiye()
        if secim==2:
            self.kkborc()
        if secim==3:
            self.paracek()
        if secim==4:
            self.parayatır()
        if secim==5:
            self.cıkıs()
        
    def menu(self):
        secim=int(input("*Merhabalar {}'a Hoşgeldiniz Sayın {} {}.\n\nLütfen yapmak İstediğiniz İşlemi Seçiniz...\n\n[1]Bakiye Sorgulama\n[2]Kredi Kartı Borç Sorgulama\n[3]Para Çekme\n[4]Para Yatırma\n[5]Kart İade\n\nSeçim:".format(self.atmad,Takılankart.ad,Takılankart.soyad)))
        while secim<1 or secim>5:
            print("\n\nLütfen 1 ve 5 Arasından Geçerli Bir Değer Giriniz...\nAna Menüye Dönülüyor...")
            self.program()
        return secim

    def bakiye(self):
        print("Hesap Bakiyeniz:{} TL'dir.".format(Takılankart.hesapbakiye))
        self.dongu=False
        self.menudon()

    def kkborc(self):
        print("Kredi Kartı Borcunuz {} Son Ödeme Tarihli {} TL'dir.".format(Takılankart.sonodeme,Takılankart.kredikartborc))
        self.dongu=False
        self.menudon()

    def paracek(self):
        miktar=int(input("Lütfen Çekeceğiniz Tutarı Gİriniz:..."))
        Yenimiktar=Takılankart.hesapbakiye-miktar
        if miktar>Takılankart.hesapbakiye:
            print("Yetersiz Bakiye")
            self.menudon()
        else:
            print("Lütfen Paranızı Sayarak Alınız. Hesabınızda Kalan Tutar {} TL'dir.".format(Yenimiktar))
            self.menudon()

    def parayatır(self):
        miktar2=int(input("Lütfen Yatırılacak Tutarı Giriniz:...."))
        Yenimiktar2=Takılankart.hesapbakiye+miktar2
        print("Para Yatırma İşlemi Başarıyla Gerçekleşmiştir.Hesabınızın yeni Bakiyesi {} TL'dir.".format(Yenimiktar2))
        self.menudon()

    def cıkıs(self):
        print("Bankamızı Tercih Ettiğiniz İçin Teşekkür Eder, İyi Günler Dileriz")
        self.dongu=False
        exit

    def menudon(self):
        x=int(input("Ana Menüye Dönmek İçin Lütfen 7 tuşuna basınız.Kart İade İçin 5'e Basınız:..."))
        if x==7:
            self.program()
        elif x==5:
            self.cıkıs()

Banka=ATM("XBank")
while Banka.dongu:
    Banka.program()

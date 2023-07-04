Kullanıcı_Adı=input("Lütfen Kullanıcı Adını Giriniz")
Kullanıcı_Sifre=input("Lütfen Şifreyi Giriniz")

SistemKA="Anlaşılır Ekonomi"
SistemSif="123456"

if Kullanıcı_Adı==SistemKA and Kullanıcı_Sifre==SistemSif:
    print("Merhaba {},Hoş geldin".format(SistemKA))
elif Kullanıcı_Adı!=SistemKA and Kullanıcı_Sifre!=SistemSif:
    print("Merhaba, Kullanıcı Adı ve Şifren Hatalıdır!!")
elif Kullanıcı_Adı!=SistemKA:
    print("Merhaba,Kullanıcı adın hatalı")
else:
    print("Merhaba {},Şifren Hatalıdır".format(SistemKA))


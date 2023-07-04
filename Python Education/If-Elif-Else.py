# != bu işaret eşit değildir anlamına gelir
Kullanıcı_Adı="Anlaşılır Ekonomi"
Kullanıcı_Sifre="1234567"

if Kullanıcı_Adı=="Anlaşılır Ekonomi" and Kullanıcı_Sifre=="1234567":
    print("Giriş Başarılı, Hoş geldiniz")
elif Kullanıcı_Adı!="Anlaşılır Ekonomi" and Kullanıcı_Sifre!="1234567":
    print("Kullanıcı Adı ve Şifre hatalıdır")
elif Kullanıcı_Adı!="Anlaşılır Ekonomi":
    print("Kullanıcı Adı hatalıdır")
else:
    print("Şifre hatalıdır")


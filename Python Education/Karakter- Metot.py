#Ezberlemeye gerek yok.Önemli olan nasıl kullanıldığını ve kolaylık sağladığını bilmek.

x="Anlaşılır Ekonomi"
# y=x.lower()
# print(y)

# y=x.upper()
# print(y)

# y=x.islower() #Tamamının büyük mü küçük mü harften oluştuğunu söyler.
# print(y) #tersi isupper()

# y=x.isnumeric() #rakam değerinden mi oluşuyor
# print(y)

y=x.capitalize()  #sadece ilk harfi büyütür
print(y)

y=x.title() #Bütün karakterlerin büyük harfle başlamasını istiyorsak.
print(y)

y=x.count("o") #kelimelerin içinde kaç tane olduğunu sayar
print(y)

y=x.strip() #sağdan ve soldan karşılaştığı ilk boşluğu yok eder.Eğer parantez içine harf girilirse ilk gördüğünü siler.
print(y) 
#y=x.lstrip olursa sadece soldan yapar.
#y=x.rstrip olursa da sağdan yapar.

a="Merhaba, ben Anlaşılır Ekonomi"
z=a.split("  ")   #Bu metot da parçalama işlemi yapar.
# print(z)

#peki birleştirme işlemi de yapabiliyor muyuz? Evet.

z="**".join(z)  #yani aralarda çift yıldız olacak şekilde birleştiriyoruz.
print(z)

z=a.find("ben")
print(z)

y=x.replace("Anlaşılır","Merhaba")
print(y)   #Eski karakterin yerine yeni karakter tanımlama

Adı="Anlaşılır"
Soyadı="Ekonomi"
Görevi="Eğitmen"

Bilgiler=[Adı,Soyadı,Görevi]

print("Kişinin Adı:{},Kişinin Soyadı:{},Kişinin Görevi:{}"
.format(Bilgiler[0],Bilgiler[1],Bilgiler[2]))








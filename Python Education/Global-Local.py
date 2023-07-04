a="Merhaba2"  #Bu global değişken
def Merhaba():
    a="Merhaba"   #Bu ise yerel yani fonksiyon bittiğinde biten bir değişken
    print(a)

Merhaba()
print(a)

#Farklı bir örnek yapalım

a="Merhaba"
def Merhaba():
    global a  #İkisininde merhaba22 vermesinin nedeni global anahtarını kullandık.
    a="Merhaba22"
    print(a)

Merhaba()
print(a)

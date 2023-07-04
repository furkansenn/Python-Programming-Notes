liste=["Ahmet",23]
print(type(liste))

demet1=("Ahmet")
print(type(demet1))

demet2=("Ahmet",23)    #Demet örneği
print(type(demet2))

liste[0]="Mehmet"    #Yani listeler değiştirilebiliyor.
print(liste)

print(demet2[1])

demet2[0]="Mehmet"  #Hata alırsın.Çünkü demetler değiştirilemez
print(demet2)

#Yani üzerinde değişiklik olmayacağını düşündüğümüz verileri demet yapılarıyla kullanmalıyız.
 
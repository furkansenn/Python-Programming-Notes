#print(abs(-5)) Mutlak değerini alır.

#print(round(22/7)) Yuvarlama işlemi yapar round(22/7,3) yaparsak virgülden sonra o kadar basamak yazdırır
 
# x=[5<6,6<7,8<9] 
# print(all(x)) #Hepsi oğruysa true olarak döner fakat içinde 1 tane bile false değer varsa false döner

# x=[5<6,6<7,9<8]
# print(any(x)) #Any'de tam tersi olarak içinde 1 tane bile true ifade varsa True olarak döner.

import enum


print(ascii("\n")) #Kaçış dizisini bile bu şekilde yazdırabiliriz.

print(bool()) #İlerde lazım olacak

print(chr(25)) #Unicod sistemindeki bir tam sayının karakter karşılığını verir.

print(list())

y=set()
print(type(y))

x="Anlaşılır Ekonomi"
y=set(x)
print(y) #Tekrarlılardan kurtulur.

tuple

dict

print(float(2))
int
str

# print(dir(list)) #tüm metodları gösterir
# print(dir(str))

# print(divmod(10,6)) #bölen ve kalan kısmı yazar

#print(*enumerate(x)) #her bi karaktere numaralama işlemi tanımlar  

# for i in enumerate(x):
#     print(i) #sık kullanılan fonksiyondur

#help(dir) 

a=2
b="2"
print(id(a))
print(id(b))  #sonuç 2 farklı id numarası

#input() her zaman değeri str olarak alır önüne yazarak int vs. alabiliriz

#len uzunlukları verir

e=[1,2,3,5,4]
print(max(e))

f=["A","AB","ABC"]
print(max(f,key=len)) #sonuç ABC verir. Uzunluğu en fazla olanı yani

print(pow(2,3)) #Üs alır yani 2 üzeri 3 gibi

print("Ankara","İstanbul","İzmir",sep="--",end="...") #Sep aralara ne koyacağımızı belirler end ise sona

print(list(range(0,100))) #100 e kadar yazdırır eğer 100 ün yanına virgül atıp 5 yazsaydım 5 er 5 er sayardı

o=["A","B","C",12]
print(list(reversed(o))) #tersten yazdırır, hatırlarsan farklı bir yolu daha vardı.
print(o[::-1]) #bu yol da var

r=[1,2,3,4,5,6,7]
print(sum(r)) #toplama yapar

print(type(r)) #tipini verir tuple,list,set,str vs.

h=[1,2,3,4]
j=["a","b","c","d"]
print(*zip(h,j)) #iki listeyi birleştirir
#fakat burdaki zipin önündeki yıldız listeyi açmaya yarar





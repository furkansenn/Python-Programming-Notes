Liste=[1,2,5,"Merhaba",2.5]
# Liste.append("Anlaşılır Ekonomi") 
# print(Liste)   #En son sıraya data ekler

Liste.insert(3,"Anlaşılır Ekonomi") 
print(Liste) #istediğin sıraya ekler

# Liste.remove(2) #Soldan başlar 2 değerini ilk gördüğünde siler
# print(Liste)

# Liste.pop(2) #Belirli indeksi siler
# print(Liste)

# Liste2=Liste.copy()
# print(Liste2)

Listem=[1,3,5,7,3]
Listem2=["a","b","c","d"]
# Listem.extend(Listem2)
# print(Listem) iki listeyi birbirine ekler

# print(Listem.count(3)) Kaç adet olduğunu söyler

# Listem.sort() #Küçükten büyüğe sıralar.
# print(Listem)

# Listem.sort(reverse=True) #Büyükten küçüğe sıralar
# print(Listem)

Listem.reverse() #Listeyi tersten yazar
print(Listem)

Listem.clear()
print(Listem)  #Siler



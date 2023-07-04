def ortalama(*args):
    sonuc=0
    for i in args:
        sonuc=sonuc+i
        sonuc2=sonuc/len(args)
    return round(sonuc2,3)

print(ortalama(5,10,6))



def ortalama(*args,x):
    sonuc=0
    for i in args:
        sonuc=sonuc+i
        sonuc2=sonuc/len(args)
    if sonuc2>x:
        print("{} sayısı ortlamadan küçüktür.".format(x))
    else:
        print("{} sayısı ortalamadan büyüktür. ".format(x))
    return sonuc2

ortalama(3,4,5,x=15)




def araba(**kwargs):
    for key,value in kwargs.items():
        if value>250000:
            print("{} marka araba biraz pahalı.".format(key))
        else:
            print("{} marka araba biraz daha ucuz.".format(key))

araba(Bmw=500000,Audi=350000,Mercedes=1000000,Ford=150000,Fiat=50000)



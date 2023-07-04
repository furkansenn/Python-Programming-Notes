import numpy as np

# sıfır=np.zeros((5,5),dtype=int)
# bir=np.ones((3,4),dtype=int)

# print(sıfır)
# print(bir)

bir=np.ones((3,4),dtype=int)*10
print(bir)

a=np.full((5,5),20,dtype=int)
print(a)

b=np.eye(5) #birim matris 
print(b)

c=np.diag([1,2,3,4,5]) #köşegenlere yolluyor
print(c)

d=np.arange(0,100,5) #range methodu tarzı-_-100 dahil eğil
print(d)

e=np.linspace(0,100,5,endpoint=False) # bu metottaki fark ise kaç eleman olduğunu yazıyorsun aralık oto geliyor
print(e) #100 ü dahil eder etmek istemiyorsan endpoint

f=np.random.randint(0,10,size=(3,4)) #random matris oluşturur
print(f)
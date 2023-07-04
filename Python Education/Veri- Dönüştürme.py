# #Bu dosyada str'den int.ye, floattan int.ye, demetten kümeye vs. geçiş yapılır. 

# a=2     #int 
# b=2.6   #float
# c="24"  #str  

# print(type(c))

# d=str(a)
# print(d+c) #224
# print(type(d))

# e=float(c)
# print(e+b)
# print(type(e))

x=[1,3,5,7,9]
print(type(x))
y=tuple(x)
print(y)     #listeden demet yapısına çevirdim.

print(type(y))

z=set(x)
print(z)
print(type(z))


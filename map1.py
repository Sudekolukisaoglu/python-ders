sayilar = [11,22,3]
def carp(xx): 
    return xx*2


#  b = []
# for a in sayilar:
#     b.append(carp(a))


#  print(b)

yeniDizi = list(map(carp,sayilar))   #bir dizinin nher bir elemanına bir işlem uygular.         

print(yeniDizi)


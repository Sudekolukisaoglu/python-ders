meyveler1 = ["muz","dut","nar"]  # list turu collection
meyveler2 = ("elma","armut","kivi") # tuple turu collection
meyveler3 = ["havuç","portakal","greyfurt"]


print(meyveler1)
print(meyveler1)

print(type(meyveler1))
print(type(meyveler2))

# print(meyveler1+meyveler2)  # tipleri aynı olmadığında hata verir
# print(meyveler1+meyveler3)
meyveler1 += meyveler3
m4 = meyveler1+meyveler3
print(m4)

print(meyveler1)

meyveler1.append("karpuz")
print(meyveler1)

meyveler1.insert(1,"Bostan")  #
print(meyveler1)


             
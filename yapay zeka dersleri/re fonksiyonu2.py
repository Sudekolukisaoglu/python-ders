import re
txt1 = "Ahmet al renkli bir şal aldı."
txt2 = "Mehmet kırmızı bir top getirdi."

bulunan1 = (re.search("al", txt1))
# bulunan2(re.findall("al", txt2))
print(bulunan1)

print(type(bulunan1))
print(bulunan1.span())
print(bulunan1.start())
print(bulunan1.end())

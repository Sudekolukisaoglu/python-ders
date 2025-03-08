import re
txt1 = "Ahmet al renkli bir şal aldı."
txt2 = "Mehmet kırmızı bir top getirdi."

xxx = "Ahmet al renkli bir şal aldı."

cümleler = [txt1,txt2,xxx]

for a in cümleler:
    kelimeleri = re.split("\s", a)
    print(kelimeleri) # boşluğa göre böl
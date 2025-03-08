import re
xxx = "Sude pembe renkli bir şal aldı."

# tüm pembe ifadelerinin listesi
print(re.findall("pembe", xxx))

# şal ifadesini ara
print(re.search("şal", xxx))

# “al” a göre böl
print(re.split("pembe", xxx)) 

# Boşlukları zzz yap
print(re.sub(" ", "zzz", xxx)) 


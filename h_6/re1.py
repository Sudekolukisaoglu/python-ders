import re 
metin1 = "Bugün hava çok soğuk"
metin2 = "Bursa çok soğuk"
metin3 = "Bugün hava çok soğuk"

#aranan = "^Bu.*soğuk$"  #Başında Bu olan ve soğuk ile biten
#aranan = "^Bug.*"  #Başında Bug olanları ara
aranan = "o.*"  # Başında o ile başlayan ifadeler

print(re.search(aranan, metin1))
print(re.search(aranan, metin2))
print(re.search(aranan, metin3))

deger = re.search(aranan, metin1)


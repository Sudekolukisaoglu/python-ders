print("Bu program kaç yıl yaşadığını hesaplar")

ad = input("Adın nedir?")
a = int(input(f"{ad} doğum yılın nedir?"))
print(f"Demek {2024-a} yaşındasın {ad} . ")

if 2024-a > 50 : print("Yaşlısın.")
elif 2024-a > 30 : print("Orta yaşlısın.")
elif 2024-a > 15 : print("Gençsin.")
input()
        

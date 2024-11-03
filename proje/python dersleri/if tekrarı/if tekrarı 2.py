print("Bu program kaç yıl yaşadığını hesaplar")

ad = input("Adın nedir?")
dy = int(input(f"{ad} doğum yılın nedir?"))
print(f"Demek {2024-dy} yaşındasın {ad} . ")

if dy > 2023 or dy < 1900 : 
    print("Doğum yılı yanlış girildi.")
else:     
    yas = 2024-dy


    if yas > 50 : print("Yaşlısın.")

    elif yas > 30 : print("Orta yaşlısın.")
    elif yas > 15 : print("Gençsin.")
    elif yas > 15 : print("Çocuksun.")
    input()
    

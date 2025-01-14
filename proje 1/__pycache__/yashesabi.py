def yas_hesabi():
    print("Yaş Hesaplayıcı")
    ad = input("Adın nedir? ")
    print(f"Merhaba {ad}")
    yil = input(f"Hangi yılda doğdun {ad}? ")
    print(f"{ad}, {2024 - int(yil)} yaşındasın.")
    input("Devam etmek için bir tuşa basın...")

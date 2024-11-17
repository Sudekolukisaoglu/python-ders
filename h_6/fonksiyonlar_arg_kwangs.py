# def selamla(gelen):
#     gelen.append("Nur")
#     print(gelen)
#     for a in gelen: 
#         print("Merhaba",a)

# ogrenciler = ["Ali","Can","Cem"]        
# selamla(ogrenciler)

def selamla(*gelen):   # args=argumanlar=parametreler=fonksiyonun kullandığı değerler
    #gelen.append("Nur")
    print(gelen)
    print("gelen[1]:",gelen[1])
    for a in gelen:
        print("Merhaba",a)

selamla("Ali","Can","Cem")
urunler = [
    ["Kurşun kalem",40],
    ["Tükenmez kalem",30],
    ["Renkli kağıt",150],
]

kdvOrani = 20
# urunlerKDVli = []
# def kdvEkle(oran):
#     for u in urunler:
#         yeniUrun = [u[0],oran*100/u[1]+u[1]]
#         urunlerKDVli.append(yeniUrun)

urunlerKDVli = list(map(lambda x:[x[0],x[1]+kdvOrani],urunler))

# kdvEkle(kdvOrani)
print(urunler)       
print(urunlerKDVli) 
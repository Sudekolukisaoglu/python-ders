import matplotlib.pyplot as plt
kategoriler = ["matematik","türkçe","fen bilimleri"]
degerler = [50,60,100]

plt.title('DERS TERCİHLERİ')
plt.pie(degerler,labels=kategoriler)
plt.show()

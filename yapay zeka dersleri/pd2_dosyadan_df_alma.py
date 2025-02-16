import pandas as pd
print(pd.__version__)

# araç_satiş_verileri = {
#     "arabalar": ["BMW", "Volvo", "Ford"],
#     "satış_rakamlari" : [200,10,150]                       
# }
veriler  = pd.read_csv("ornekCSVdosyasi2.csv")

pandas_ile_olusan_dizi = pd.DataFrame(veriler)
print(pandas_ile_olusan_dizi)
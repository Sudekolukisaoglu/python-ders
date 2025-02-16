import pandas as pd
print(pd.__version__)

araç_satiş_verileri = {
    "arabalar": ["BMW", "Volvo", "Ford"],
    "satış_rakamlari" : [200,10,150]                       
}

pandas_ile_oluşan_dizi = pd.DataFrame(araç_satiş_verileri)
print(pandas_ile_oluşan_dizi)
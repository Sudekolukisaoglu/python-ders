# önce panda yükle py -m pip install pandas
import pandas as pd
# genellikle as pd olarak kullanılır.
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'miktar': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)

import pandas as pd
import numpy as np

categorical_variable={
    "Frequency": ["Never", "Rarely", "Never", "Always", "Always", "Always", "Rarely", "Rarely", "Always"]
}

cat=pd.DataFrame(categorical_variable)
cat1=cat.copy()
value={"Never":0, "Rarely":1, "Always":2}
cat["ordinal_encoding"]=cat["Frequency"].replace(value)
cat.drop("Frequency", axis=1, inplace=True)
print(cat1)
print(cat)
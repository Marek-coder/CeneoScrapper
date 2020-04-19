#import bibliotek os i glob
import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#wyświetlanie zawartości katalogu opinion_json
input_dictionary ="./opinions_json"
print(*os.listdir(input_dictionary))
product_id =input("Podaj identyfikator produktu: ")

#wczytywanie do ramki danych opinii o pojedynczym produkcie
opinions = pd.read_json(input_dictionary+"/"+product_id".json")
opinions = opinions.set_index("opinion_id")
print(opinions)
#import bibliotek os i glob
import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#wyświetlanie zawartości katalogu opinion_json
input_dictionary ='opinions_json'
print(*os.listdir(input_dictionary))
product_id =input("Podaj identyfikator produktu: ")
#wczytywanie do ramki danych opinii o pojedynczym produkcie
opinions = pd.read_json(input_dictionary+'/'+product_id+".json")
opinions = opinions.set_index("opinion_id")
pros =opinions.pros.count()
cons =opinions.cons.count()
stars =opinions.stars.value_counts().sort_index().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
recomendation =opinions.recommendation.value_counts()
# fig opisuje wykres ax osie
fig, ax=plt.subplots()
stars.plot.bar(title="Gwiazdki")
plt.ylabel("liczba opinii")
plt.xlabel("ocena")
plt.xticks(rotation=0)
# show pokazuje na podlagdzie safefig? do pliku

plt.savefig("figures_png/"+product_id+"_bar.png")
plt.show()
plt.close()


fig, ax=plt.subplots()
recomendation.plot.pie(label="",autopct="%1.1f%%",colors=["#f5c3c2", "#89cff0"])
plt.title("Rekomendacja")
plt.show()
plt.close()

opinions['purchase']= opinions['purchase_date']!=None
print(opinions['purchase'])


import pandas as pd
import json

df = pd.read_csv("gibberish.csv")

data = []
for i in df.itertuples():
    data.append({
        "original": i[1],
        "gibberish": i[2]
    })

json.dump(data, open("src/data/word_list.json", "w"))
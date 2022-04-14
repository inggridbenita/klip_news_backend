import json
import pandas as pd
import value


cols = ["title", "date", "content", "link", "poster", "category"]

df = pd.DataFrame(columns=cols)

for category in value.categories:
    with open('./res/data_berita/{}.json'.format(category), 'r') as json_file:
        data = json.load(json_file)
        for news in data:
            df_append = pd.DataFrame(
                [[news["title"], news["date"], news["content"], news["link"], news["poster"], category]],
                columns=cols
            )
            df = pd.concat([df, df_append], ignore_index=True)

df["id"] = list(range(1, len(df) + 1))
df = df[["id"] + cols]
df.to_csv("res/datasets/news.csv", index=False)

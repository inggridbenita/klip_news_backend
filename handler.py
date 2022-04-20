import pandas as pd


def get_all_news():
    df = pd.read_csv("./res/datasets/news.csv")
    list_news = []
    for i in range(0, len(df)):
        list_news.append({
            "id": str(df['id'][i]),
            "title": df['title'][i],
            "date": df['date'][i],
            "poster": df['poster'][i],
            "category": df['category'][i],
        })
    return {"news": list_news}

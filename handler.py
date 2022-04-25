import pandas as pd


def get_all_news():
    df = pd.read_csv("./res/datasets/news_preprocessed.csv")
    list_news = []
    for i in range(0, len(df)):
        list_news.append({
            "id": str(df['id'][i]),
            "title": df['title'][i],
            "date": df['date'][i],
            "weekday": df["weekday"][i],
            "poster": df['poster'][i],
            "category": df['category'][i],
        })
    return {"news": list_news}


def get_news_detail(id):
    id = int(id)
    df = pd.read_csv("./res/datasets/news.csv")
    df = df[df["id"] == id]
    news = df.iloc[0]
    news_dict = {
        "id": str(news['id']),
        "title": news['title'],
        "date": news['date'],
        "weekday": news["weekday"],
        "poster": news['poster'],
        "category": news['category'],
        "content": news['content'],
    }
    return news_dict

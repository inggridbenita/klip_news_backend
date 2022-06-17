from rake_nltk import Rake
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from domains.Rake.RakeRepository import RakeRepository
import pandas as pd


class RakeRepositoryLibrary(RakeRepository):
    @staticmethod
    def recommend(df, title, cs, indices):
        # Fungsi untuk merekomendasikan film
        recommended_news = []
        idx = indices[indices == title].index[0]
        score_series = pd.Series(cs[idx]).sort_values(ascending=False)
        top_10_indices = list(score_series.iloc[1:11].index)
        for i in top_10_indices:
            recommended_news.append(list(df['id'])[i])
        return recommended_news

    @staticmethod
    def rake_implement(x, r):
        x = x.lower()
        r.extract_keywords_from_text(x)
        return r.get_ranked_phrases()

    def get_recommendation(self, df_news, df_stopwords, news_id_arr):
        df_news["keywords"] = df_news["title"] + ". " + df_news["content"]

        df_news = df_news[['id', 'keywords']]

        stopwords = df_stopwords["stop_word"].tolist()
        r = Rake(stopwords=stopwords)
        df_news['bag_of_words'] = df_news['keywords'].apply(lambda x: self.rake_implement(x, r))
        df_news['bag_of_words'] = df_news['bag_of_words'].apply(lambda x: " ".join(x))

        count = CountVectorizer()
        count_matrix = count.fit_transform(df_news['bag_of_words'])
        cosine_sim = cosine_similarity(count_matrix, count_matrix)
        indices = pd.Series(df_news['id'])

        recommended_news = []
        for i in range(0, len(news_id_arr)):
            recommended_news = recommended_news + self.recommend(df_news, news_id_arr[i], cosine_sim, indices)
        return list(set(recommended_news))

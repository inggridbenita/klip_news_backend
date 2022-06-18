from rake_nltk import Rake
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from domains.Rake.RakeRepository import RakeRepository
import pandas as pd


class RakeRepositoryLibrary(RakeRepository):
    @staticmethod
    def recommend(df, title, cs, indices):
        # Fungsi untuk merekomendasikan film
        recommended_news_id = []
        recommended_news_score = []
        idx = indices[indices == title].index[0]
        score_series = pd.Series(cs[idx]).sort_values(ascending=False)
        top_10_indices = list(score_series.iloc[0:10].index)
        j = 0
        for i in top_10_indices:
            recommended_news_id.append(list(df['id'])[i])
            recommended_news_score.append(score_series[j])
            j = j + 1
        return recommended_news_id, recommended_news_score

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

        list_id = []
        list_score = []
        for i in range(0, len(news_id_arr)):
            temp_list_id, temp_list_score = self.recommend(df_news, news_id_arr[i], cosine_sim, indices)
            list_id.extend(temp_list_id)
            list_score.extend(temp_list_score)
        df_recommendation = pd.DataFrame({
            "id": list_id,
            "score": list_score,
        })
        df_recommendation = df_recommendation.sort_values(by='score', ascending=False)
        df_recommendation = df_recommendation.drop_duplicates(subset=['id'], keep='first')
        return list(df_recommendation["id"])

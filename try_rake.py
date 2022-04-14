from rake_nltk import Rake
import nltk
import pandas as pd
import numpy as np
import matplotlib
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('./res/datasets/dataset_custom.csv')

df['Key_words'] = ''
r = Rake()


def rake_implement(x, r):
    x = x.lower()
    r.extract_keywords_from_text(x)
    return r.get_ranked_phrases()


df['Key_words'] = df['Plot'].apply(lambda x: rake_implement(x, r))
# print(df['Plot'][0])
# print(df['Key_words'][0])
df['Director'] = df['Director'].apply(lambda x: [x.lower().replace(' ', '')])


def step_2(text):
    text = text.lower()
    list_actor = text.split(",")
    for i in range(len(list_actor)):
        list_actor[i] = list_actor[i].replace(" ", "")
    return list_actor


df['Actors'] = df['Actors'].apply(lambda x: step_2(x))
df['Genre'] = df['Genre'].apply(lambda x: step_2(x))

df['Bag_of_words'] = 'mdfn'
columns = ['Genre', 'Director', 'Actors', 'Key_words']

for index, row in df.iterrows():
    words = []
    for col in columns:
        words = words + row[col]
    df.iat[index, df.columns.get_loc('Bag_of_words')] = words

df['Bag_of_words'] = df['Bag_of_words'].apply(lambda x: " ".join(x))

df = df[['Title', 'Bag_of_words']]

count = CountVectorizer()
count_matrix = count.fit_transform(df['Bag_of_words'])
cosine_sim = cosine_similarity(count_matrix, count_matrix)
indices = pd.Series(df['Title'])


def recommend(title, cs=cosine_sim):
    recommended_movies = []
    idx = indices[indices == title].index[0]
    score_series = pd.Series(cs[idx]).sort_values(ascending=False)
    top_10_indices = list(score_series.iloc[1:11].index)

    for i in top_10_indices:
        recommended_movies.append(list(df['Title'])[i])

    return recommended_movies


recommended_movies = recommend('The Avengers')
print(recommended_movies)

from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MultiLabelBinarizer
import pandas as pd


movies = pd.read_csv("movies.csv")

movies["genres"] = movies["genres"].apply(lambda x: x.split("|"))
# print(movies["genres"])
movies["title"] = movies["title"].str[:-6]
movies["title"] = movies["title"].str.lower().str.strip()

mlt = MultiLabelBinarizer()
vector = mlt.fit_transform(movies["genres"])
# print(vector)

knn = NearestNeighbors(metric="cosine", algorithm="brute")

knn.fit(vector)


def reccomend(title, n=5):
    title = title.lower().strip()
    matched = movies[movies["title"] == title]
    if not matched.empty:
        idx = matched.index[0]

        dist, indices = knn.kneighbors([vector[idx]], n_neighbors=n+1)
        reccomendation = []
        for i in indices[0][1:]:
            reccomendation.append(movies.iloc[i]["title"]) 
        return reccomendation
    else:
        return ["Movie Not Found"]

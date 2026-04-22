import pandas as pd

from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MultiLabelBinarizer

movies = pd.read_csv("movies.csv")

movies["genres"] = movies["genres"].apply(lambda x: x.split("|"))

mlt = MultiLabelBinarizer()
vectors = mlt.fit_transform(movies['genres'])

knn = NearestNeighbors(metric="cosine", algorithm="brute")

knn.fit(vectors)


def recommend(title, n=5):
    idx = movies[movies["title"] == title].index[0]

    dist, indices = knn.kneighbors([vectors[idx]], n_neighbors=n+1)

    recomendations = []
    for i in indices[0][1: ]:
        recomendations.append(movies.iloc[i]["title"])
    
    return recomendations
       







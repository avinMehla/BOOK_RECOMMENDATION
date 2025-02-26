import numpy as np
import  pandas as pd

books = pd.read_csv("C:/Users/avinr/Desktop/Practice/book recomendation/dataset/Books.csv",encoding='latin-1')

books.head()
books.tail()
books.columns

books=books[['ISBN','Book-Title','Book-Author','Year-Of-Publication','Publisher']]

books.rename(columns = {'Book-Title' : 'title','Book-Author':'author', 'Year-Of-Publication' : 'year', 'Publisher':'publisher'},inplace=True)

books.head(2)
books.rename(columns = {'Year' : 'year'},inplace=True)

books.head()

users = pd.read_csv("C:/Users/avinr/Desktop/Practice/book recomendation/dataset/Users.csv" ,encoding='latin-1')
users.head()
users.columns
users.rename(columns = {'User-ID':'user_id','Location':'location','Age':'age'},inplace=True)
users.head()

ratings = pd.read_csv("C:/Users/avinr/Desktop/Practice/book recomendation/dataset/Ratings.csv",encoding='latin-1')
ratings.head(2)

ratings.rename(columns = {'User-ID' : 'user_id', 'Book-Rating': 'rating'},inplace=True)
ratings.head()
books.shape
users.shape
ratings.shape
abc = ratings['user_id'].value_counts()>200
abc[abc].shape
y = abc[abc].index
y
ratings=ratings[ratings['user_id'].isin(y)]
ratings.shape
ratings.head()
ratings_with_books = ratings.merge(books, on='ISBN')
ratings_with_books.shape

number_ratings = ratings_with_books.groupby('title')['rating'].count().reset_index()

number_ratings.rename(columns={'rating':'number of rating'},inplace=True)
number_ratings

final_rating = ratings_with_books.merge(number_ratings, on ='title')
final_rating

final_rating=final_rating[final_rating['number of rating']>=50]
final_rating.shape

final_rating.drop_duplicates(['user_id','title'],inplace=True)

final_rating.shape
book_pivot=final_rating.pivot_table(columns='user_id',index='title',values='rating')
book_pivot
book_pivot.fillna(0,inplace=True)

from scipy.sparse import csr_matrix
book_sparse = csr_matrix(book_pivot)
type(book_sparse)

from sklearn.neighbors import NearestNeighbors
model = NearestNeighbors(algorithm='brute')
model.fit(book_sparse)
distances , suggestions = model.kneighbors(book_pivot.iloc[0,:].values.reshape(1,-1),n_neighbors=6)
distances
suggestions
for i in range(len(suggestions)):
    print(book_pivot.index[suggestions[i]])

def recommend_book(name, number):
    distances , suggestions = model.kneighbors(book_pivot.loc[name,:].values.reshape(1,-1),n_neighbors=number)
    for i in range(len(suggestions)):       
            print(book_pivot.index[suggestions[i]])

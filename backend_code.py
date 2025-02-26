!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


books = pd.read_csv("C:/Users/harsh/Downloads/Book/Books.csv",error_bad_lines=False, encoding='latin-1')


# In[3]:


books.head()


# In[4]:


books.tail()


# In[5]:


books.columns


# In[6]:


books=books[['ISBN','Book-Title','Book-Author','Year-Of-Publication','Publisher']]


# In[7]:


books.rename(columns = {'Book-Title' : 'title','Book-Author':'author', 'Year-Of-Publication' : 'year', 'Publisher':'publisher'},inplace=True)


# In[8]:


books.head(2)
books.rename(columns = {'Year' : 'year'},inplace=True)


# In[9]:


books.head()


# In[10]:


users = pd.read_csv("C:/Users/harsh/Downloads/Book/Users.csv",error_bad_lines=False,encoding='latin-1')


# In[11]:


users.head()


# In[12]:


users.columns


# In[13]:


users.rename(columns = {'User-ID':'user_id','Location':'location','Age':'age'},inplace=True)


# In[14]:


users.head()


# In[15]:


ratings = pd.read_csv("C:/Users/harsh/Downloads/Book/Ratings.csv",error_bad_lines=False,encoding='latin-1')


# In[16]:


ratings.head(2)


# In[17]:


ratings.rename(columns = {'User-ID' : 'user_id', 'Book-Rating': 'rating'},inplace=True)


# In[18]:


ratings.head()


# In[19]:


books.shape


# In[20]:


users.shape


# In[21]:


ratings.shape


# In[22]:


abc = ratings['user_id'].value_counts()>200


# In[23]:


abc[abc].shape


# In[24]:


y = abc[abc].index
y


# In[25]:


ratings=ratings[ratings['user_id'].isin(y)]


# In[26]:


ratings.shape


# In[27]:


ratings.head()


# In[28]:


ratings_with_books = ratings.merge(books, on='ISBN')


# In[29]:


ratings_with_books.shape


# In[30]:


number_ratings = ratings_with_books.groupby('title')['rating'].count().reset_index()


# In[31]:


number_ratings.rename(columns={'rating':'number of rating'},inplace=True)


# In[33]:


number_ratings


# In[34]:


final_rating = ratings_with_books.merge(number_ratings, on ='title')


# In[35]:


final_rating


# In[36]:


final_rating=final_rating[final_rating['number of rating']>=50]


# In[37]:


final_rating.shape


# In[38]:


final_rating.drop_duplicates(['user_id','title'],inplace=True)


# In[39]:


final_rating.shape


# In[40]:


book_pivot=final_rating.pivot_table(columns='user_id',index='title',values='rating')


# In[41]:


book_pivot


# In[42]:


book_pivot.fillna(0,inplace=True)


# In[43]:


from scipy.sparse import csr_matrix
book_sparse = csr_matrix(book_pivot)


# In[44]:


type(book_sparse)


# In[45]:


from sklearn.neighbors import NearestNeighbors
model = NearestNeighbors(algorithm='brute')


# In[46]:


model.fit(book_sparse)


# In[55]:


distances , suggestions = model.kneighbors(book_pivot.iloc[0,:].values.reshape(1,-1),n_neighbors=6)


# In[56]:


distances


# In[57]:


suggestions


# In[58]:


for i in range(len(suggestions)):
    print(book_pivot.index[suggestions[i]])


# In[76]:


def recommend_book(name, number):
    distances , suggestions = model.kneighbors(book_pivot.loc[name,:].values.reshape(1,-1),n_neighbors=number)
    for i in range(len(suggestions)):
        if suggestions[i]==name:
            continue
        else:
            print(book_pivot.index[suggestions[i]])


# In[77]:


recommend_book('The Cradle Will Fall',8)


# In[ ]:







import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from datetime import datetime

df = pd.read_csv("1000_books_final.csv")

# clean the titles

def clean_title(i):
    sep = '('
    stripped = i.split(sep, 1)[0]
    return stripped
df.title = df.title.apply(clean_title)

# clean the years
year = []

def clean_year(df):
    for i in df:
        if len(i) > 10:
            year.append(i[-4:])
        elif len(i) < 5:
            year.append(i)
        elif i == 'not found':
            year.append('not found')
        else:
            year.append(datetime.strptime(i, '%b-%y').year)
            year
#df.opub_year = df.opub_year.apply(clean_year)
        #print(year)
#clean_year(df,'opub_year')
pub_year = pd.DataFrame({'year': year})

pub_year.to_csv('year.csv',index=False)

df = df.replace(['not found'],'0')

#
def min_max_norm_rating(book, x):
        max_rating = book[x].max()
        min_rating = book[x].min()
        range_of_ratings = max_rating - min_rating
        book['minmax_norm_ratings'] = round(1 + 9*((book[x] - min_rating)/range_of_ratings) , 3)
        mean_rating = df['avg_rating'].mean()
        book['mean_norm_ratings'] = round(1 + 9*((book[x] - mean_rating)/range_of_ratings) , 3)
        return book

min_max_norm_rating(df, 'avg_rating')

#
def nrt(data, rt):
        if rt is not None:
            data[rt] = data[rt].str.replace(',', '').astype(float)
            
            return data
        else:
            return np.NaN

#nrt(df, 'num_ratings')
#nrt(df, 'num_reviews')
nrt(df, 'num_pages')



import streamlit as st

### STREAMLIT


st.markdown('''
# **Best Epic Fantasy (Fiction) books Analysis**

##### This analysis looks at some variables of interest to assist in finding the best Authors for our publishing company.
1000 books of data gathered from Goodreads.com

#### Variables of interest
''')

st.sidebar.image('books_pic.JPG',width=300)

col1, col2, col3 = st.columns(3)
with col1:
    st.write("* authors")
    st.write("* awards")
    st.write("* average ratings")
with col2:
    st.write("* number of pages")
    st.write("* number of ratings")
    st.write("* number of reviews")
with col3:
    st.write("* series")
    st.write("* published year")


st.markdown('#### Histogram of xxxx') 


st.markdown('#### Most awards won')


st.markdown('### Best 50 books to stock up')
def trial(df):
    sb.set_theme(style="darkgrid")
    sb.set(rc = {'figure.figsize':(15,8)})
    # top 50 by avg rating
    df3 = df.sort_values('avg_rating',ascending = False).head(50)
    #top 50 by awards
    df4 = df.sort_values('awards',ascending = False).head(50)

    fig, ax =plt.subplots(1,3)
    sb.countplot(data = df3, x='series', ax=ax[0])
    sb.countplot(data = df4, x='series', ax=ax[1])
    sb.countplot(data = df, x='series', ax=ax[2])
    st.pyplot(fig)

trial(df)


st.markdown('#### random')
def get_plot_awvsar(data):
    fig, ax = plt.subplots()
    data.plot(df.awards )
    plt.xticks(rotation = 45)
    st.pyplot(fig)

get_plot_awvsar(df.head(10))

st.markdown('#### Actual ratings vs number of ratings')

def get_plot_nrvsar(df):
    fig, ax = plt.subplots()

    g = plt.scatter(df.avg_rating,df.num_ratings, c= df.num_ratings)
    plt.xlabel('No. Of Ratings')
    plt.ylabel('Actual Ratings')
    plt.colorbar(g)
    st.pyplot(fig)

get_plot_nrvsar(df)

def trial_2(df):
    fig = plt.figure(figsize = (15,8))
    df2 = df.groupby(['opub_year']).mean()
    #df2.head()
    chart = sb.lineplot(data=df2, x='opub_year', y='avg_rating')
    #GB=DF.groupby([(DF.index.year),(DF.index.month)]).sum()
    chart.set_xticklabels(
        chart.get_xticklabels(), 
        rotation=45, 
        horizontalalignment='right',
        fontweight='light',
        fontsize='x-large')
    None
    st.pyplot(fig)
trial_2(df)
'''arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

df1 = df.sort_values('awards',ascending = False).head(10)
awards = print(df1[['author','awards','avg_rating']])
st.dataframe(awards.style.highlight_max(axis=0))

#st.bar_chart(data=None, width=0, height=0, use_container_width=True)
st.markdown('#### Best year according to average ratings')
#group by og pub year and get mean of the ratings for the year groups - see which year did best
st.markdown('#### Author with highest ratings')
#show author with highest ratings (top 10)
st.markdown('#### Top 50 books worth stocking up - Series vs. non-serial')
# Which 50 books should i stock up as a bookstore and should it be part of a series or no series?

df4 = df.sort_values('awards',ascending = False).head(50)
sb.countplot(data = df4, x='series')

fig = plt.figure(figsize=(10, 4))
sb.countplot(data = df4, x='series')
st.pyplot(fig)

st.markdown('#### Number of ratings vs. actual rating')
#Do the number of ratings affect the actual rating provided? Can this be used to make the decision to read a book or not?
st.markdown('#### Author analysis - award count vs. average rating')
#Do the number of awards actually mean that the book got a higher rating? Do it on author by author basis as well!


st.markdown('### Our Recommendations')
# top 5 authors dependent on whats important to you? create a scroll that outputs top 5 authors based on input you give or show
# the graphs next to each other of top authors eg according to number of pages or awards or ratings etc

'''

'''

# insert top 10 books with most awards
df1 = df.sort_values('awards',ascending = False).head(10)

#group by og pub year and get mean of the ratings for the year groups - see which year did best
# Mean of minmax_norm_ratings for every year of publishing
df.groupby('opub_year').agg({"minmax_norm_ratings": [lambda x: np.mean(x)]})

#show author with highest ratings (top 10)
df2 = df.sort_values('avg_rating',ascending = False).head(5)
df2
#sb.countplot(data = df2, x='author')

# show distribution of num reviews
plt.hist(data=df, x= 'num_reviews', bins =1000)
plt.show()

#Which 50 books should i stock up as a bookstore and should it be part of a series or no series?
#top 50 books by ratings

df3 = df.sort_values('avg_rating',ascending = False).head(50)
#df3[["title", "avg_rating","series"]]
# percentage of top 50 books that are series and those that are not
sb.countplot(data = df3, x='series')

# top 50 books by awards
df4 = df.sort_values('awards',ascending = False).head(50)
sb.countplot(data = df4, x='series')

# whole dataset series vs no series
sb.countplot(data = df, x='series')

# authors that occured more than once and what are their ratings? awards?
df_author =df.author.value_counts()
df_author.head(5)
#df_author.head(10)
#df[['author', 'title']]
#df3[["title", "avg_rating","series"]]

def get_plot_nrvsar(data):

    g = plt.scatter(data.num_ratings, data.avg_rating, c= data.num_ratings)
    plt.xlabel('No. Of Ratings')
    plt.ylabel('Actual Ratings')
    plt.colorbar(g)

get_plot_nrvsar(df)

# number of pages over the years
plt.figure(figsize = (15,8))
ax = sb.lineplot(data=df, x='opub_year', y='num_pages')
ax.set_xticklabels(ax.get_xticklabels(),rotation = 30)
#df.groupby('opub_year')['num_pages'].plot(legend=True)
None

plt.figure(figsize = (15,8))
df2 = df.groupby(['opub_year']).mean()
#df2.head()
chart = sb.lineplot(data=df2, x='opub_year', y='num_pages')
#GB=DF.groupby([(DF.index.year),(DF.index.month)]).sum()
chart.set_xticklabels(
    chart.get_xticklabels(), 
    rotation=45, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='x-large')
None
'''
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

import requests
page = requests.get("https://www.goodreads.com/list/show/50.The_Best_Epic_Fantasy_fiction_")
soup = BeautifulSoup(page.content, 'html.parser')

url = []
title = []
author = []
num_reviews = []
num_ratings = []
avg_rating = []


# gather urls
url = []
book_urls = soup.find_all('tr', itemtype='http://schema.org/Book')
for i in range(len(book_urls)):
  address = 'https://www.goodreads.com' + book_urls[i].a['href']
  url.append(address)

#print(len(url))


# gather titles
book_title = soup.find_all('tr', itemtype="http://schema.org/Book")
for i in book_title:
    name = i.find('span').text
    title.append(name)


# gather authors
author_name = soup.find_all('tr', itemtype="http://schema.org/Book")
for i in author_name:
    name = i.find('a', class_ = "authorName").text
    author.append(name)


# OTHER PAGE ('page 2') IS USED TO GATHER REVIEWS AND RATINGS


# gather average ratings
for i in url:
        page2 = requests.get(i)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        avge = soup2.find(itemprop="ratingValue")
        if avge:
                avg_rating.append(avge.text.strip())
        else:
            avg_rating.append('not found')
        sleep(randint(2, 5))


# gather number of reviews and number of ratings


for i in url:
        page2 = requests.get(i)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        ratings = soup2.find(itemprop="ratingCount")
        if ratings:
                num_ratings.append(ratings.get('content'))
        else:
            num_ratings.append('not found')
        #num_ratings.append(ratings)
        reviews = soup2.find(itemprop="reviewCount")
        if reviews:
                num_reviews.append(reviews.get('content'))
        else:
            num_reviews.append('not found')
        #num_reviews.append(reviews)
        sleep(randint(2, 5))






#scrape other pages up to 10 so we can get to 1000

#scrape 900 urls, titles and authors

page = 2
url_page = f"https://www.goodreads.com/list/show/50.The_Best_Epic_Fantasy_fiction_?page={page}"
page_all = requests.get(url_page)
soup_all = BeautifulSoup(page_all.content, 'html.parser')


#scrape 900 urls, titles and authors
while page != 11:
    # gather urls
    book_urls = soup_all.find_all('tr', itemtype='http://schema.org/Book')
        #print(book_urls[1].a['href'])
    for i in range(len(book_urls)):
        address = 'https://www.goodreads.com' + book_urls[i].a['href']
        url.append(address)
      # gather titles
    book_title = soup_all.find_all('tr', itemtype="http://schema.org/Book")
    for i in book_title:
        name_bt = i.find('span').text
        title.append(name_bt)
        #gather author names
    author_name = soup_all.find_all('tr', itemtype="http://schema.org/Book")
    for i in author_name:
        name_a = i.find('a', class_ = "authorName").text
        author.append(name_a)
    page = page + 1


# scrape 900 avge ratings
avg_rating = []
page = 2
while page != 5:
      url_page = f"https://www.goodreads.com/list/show/50.The_Best_Epic_Fantasy_fiction_?page={page}"
      page_all = requests.get(url_page)
      soup_all = BeautifulSoup(page_all.content, 'html.parser')
      url_all = []
      book_urls = soup_all.find_all('tr', itemtype='http://schema.org/Book')
      #print(book_urls[1].a['href'])
      for i in range(len(book_urls)):
            address = 'https://www.goodreads.com' + book_urls[i].a['href']
            url_all.append(address)
      #print(url_all)

      for i in url_all:
            page2 = requests.get(i)
            soup2 = BeautifulSoup(page2.content, 'html.parser')
            avge = soup2.find(itemprop="ratingValue")
            if avge:
                  avg_rating.append(avge.text.strip())
            else:
                  avg_rating.append('not found')
            sleep(randint(2, 6))
            #print(avg_rating)
      page = page + 1


'''

#creating the dataframe
df = pd.DataFrame({'url':url,'title':title,'author':author,'avg_rating':avg_rating})#,'num_ratings':num_ratings,'num_reviews':num_reviews})
#df.head()

# save to csv 
df.to_csv('best_fantasy_books.csv',index=False)'''
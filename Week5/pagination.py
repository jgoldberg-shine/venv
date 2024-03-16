from bs4 import BeautifulSoup
import requests
import pandas as pd

# title_collection = []
# price_collection = []
# rating_collection = []

# for i in range(1,10):
#     html_text = requests.get(f'http://books.toscrape.com/catalogue/page-{i}.html').text

#     soup = BeautifulSoup(html_text, 'lxml')

#     titles = soup.find_all('h3')

#     rating_to_int = {
#         "One" : 1,
#         "Two" : 2,
#         "Three" : 3,
#         "Four" : 4,
#         "Five" : 5,
#     }



#     for book_title in titles:
#         print("Title : ", book_title.find('a').get('title').strip())
#         title_collection.append(book_title.find('a').get('title').strip())
#         price = book_title.find_next('p', class_="price_color")
#         print("Price: ", price.text.strip('Â'))
#         price_collection.append(float(price.text.strip('Â£')))
#         rating = book_title.find_previous('p', class_='star-rating').get('class')[1]
#         print(rating_to_int.get(rating))
#         rating_collection.append(rating_to_int.get(rating))

# df = pd.DataFrame({
#     "Title" : title_collection,
#     "Price": price_collection,
#     "Rating / 5" : rating_collection
# })


# df.to_excel("Books.xlsx", index=False)


#activity 2

df = pd.read_excel("Books.xlsx")

max_price = df["Price"].max()

print(f"Max price is {max_price}")

book_ratings = df.query("`Rating / 5` == 4")

print(f"The number of books over 4 stars is {book_ratings.shape[0]} ")

mean_price = df["Price"].mean()

print(f"The mean book price is {mean_price}")

#pip freeze > requirements.txt
#create new file called .gitignore 
#>>>>>> /env etc
# git init
# git add .
# git commit -m "first commit
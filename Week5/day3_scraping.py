from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text = requests.get("https://www.scrapethissite.com/pages/simple/")
print(html_text)
print(dir(html_text))


souped_html = BeautifulSoup(html_text.text, 'lxml')
countries = souped_html.find_all('h3')

print(countries)

for country in countries:
    print(country.text.strip())

print ([country.text.strip() for country in countries])

df = pd.DataFrame([country.text.strip() for country in countries])
print(df)
    
file_name = 'CountryNames.xlsx'

df.to_excel(file_name)

country_capitals = souped_html.find_all('span', class_="country-capital")

for capital in country_capitals:
    print(capital.text)
    

country_population = souped_html.find_all('span', class_="country-population")

for population in country_population:
    print(population.text)

df = pd.DataFrame([population.text.strip() for population in country_population])
print(df)

df.to_excel(file_name)

# df = pd.DataFrame({'Country': countries, 'Capital': country_capitals})

# # Saving to Excel
# file_name = 'CountryNames.xlsx'
# df.to_excel(file_name, index=False)

from bs4 import BeautifulSoup
import requests
import pandas as pd

# # Activity 1
html_text = requests.get("https://www.scrapethissite.com/pages/simple/")

souped_html = BeautifulSoup(html_text.text, "lxml")

countries = souped_html.find_all("h3")

country_capitals = souped_html.find_all(class_="country-capital")

country_population = souped_html.find_all("span", class_="country-population")

df = pd.DataFrame({
    "Country": [country.text.strip() for country in countries],
    "Capital": [capital.text for capital in country_capitals],
    "Population": [population.text for population in country_population]
})

df = df.set_index("Country")

# df.to_excel("country_output.xlsx")

# print(df)


# # Activity 2
my_file = open("index.html", "r")

souped_html = BeautifulSoup(my_file, "lxml")

print(my_file)

categories = souped_html.find_all("h2")
first_fav = souped_html.find_all(class_="gold")

print(categories)

df = pd.DataFrame({
    "Category": [ category.text for category in categories],
    "First": [ first.text  for first in first_fav]
})

print(df)
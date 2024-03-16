from bs4 import BeautifulSoup
import requests
import pandas as py

html_text = requests.get('https://wearecodenation.com').text
soup = BeautifulSoup(html_text, 'lxml')

h5s = soup.find_all("h5")
h6s = soup.find_all("h6")

# for h5 in h5s:
#     print(h5.text, class_='elementor-heading-title elementor-size-default')

for h5 in h5s:
    if ":" in h5.text:
        print(h5.text)

for h6 in h6s:
    if ":" in h6.text:
        print(h6.text)

months = [
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"

]

# course_dates = []
# for h6 in h6s:
#     for month in months:
#         if month in h6.text:
#             print(h6.text)
#             course_dates.append(h6.text)

# print(course_dates)

dates_dictionary = {}

for h5 in h5s:
    if ":" in h5.text:
        print(h5.text)
        h6_match = h5.find_next('h6')
        for single_date in h6_match.strings:
            print(single_date)
            dates_dictionary.append()
            dates_dictionary[course_name] = dates
            print(dates_dictionary)

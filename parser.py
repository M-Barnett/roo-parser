"""
Proof of concept parser to enter each webpage
"""
import requests
import re
import time
import csv
from bs4 import BeautifulSoup


source_url = "https://deliveroo.co.uk/sitemap"

def restaurant_finder():
    """ Function to find each restaurant link on the main sitemap page """
    href_links = []
    source_code = requests.get(source_url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    for a in soup.findAll('a'):
        if 'menu' in a['href']:
            href_links.append(a)
    print("href_links are: ")
    print(href_links[0:6])
    return href_links

def restaurant_checker(word, href_links):
    """ Function to check if the word is in each restaurant's page """
    pages_with_word = []
    for item in href_links[0:3]: # remove limiting indices
        restaurant_url = item['href']
        restaurant_name = str(item.string)
        total_url = "https://deliveroo.co.uk" + str(restaurant_url)
        restaurant_source_code = requests.get(total_url).text
        soup2 = BeautifulSoup(restaurant_source_code, 'html.parser')
        restaurant_text = soup2.get_text()
        print("restaurant_text found for " + restaurant_name)
        page_check = text_checker(word, restaurant_text) # change this for the word you want
        if page_check == True:
            pages_with_word.append(restaurant_name)
#            time.sleep(2)
    return pages_with_word

def text_checker(word, text):
    """ Function to check for a specific word in the text """
    word_list = re.findall(word, text, flags=re.IGNORECASE)
    if len(word_list) >= 1:
        result = True
    else:
        result = False
    return result

############### main stuff #####################
def main():
    test_word = "chicken"
    restaurant_html = restaurant_finder()
    result = restaurant_checker(test_word, restaurant_html)
    print("RUN SUCCESSFUL")
    print("Pages with " + test_word + " are:")
    print(result)




main()

"""
Proof of concept parser to enter each webpage and check for a specific word
"""
import requests
import re
import time
import csv
import sys
from bs4 import BeautifulSoup

source_url = "https://deliveroo.co.uk/sitemap"

########## Functions for crawling, scraping, parsing ############
def restaurant_finder():
    """ Function to find each restaurant link on the main sitemap page """
    href_links = []
    
    # use request to retrieve html source code, then BeautifulSoup to parse
    source_code = requests.get(source_url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    
    # restaurants are stored in <a> blocks and include 'menu' string in href
    for a in soup.findAll('a'):
        if 'menu' in a['href']:
            href_links.append(a)

    # print statements here are just to show the retrieved urls look right
    print("href_links are: ")
    print(href_links[0:6])
    print("") 

    return href_links

def restaurant_checker(word, href_links):
    """ Function to check if the word is in each restaurant's page """
    pages_with_word = []
    
    for link in href_links[0:3]: # change/remove indices to parse more restaurants
        # need to convert and extract info from links
        restaurant_url = link['href']
        restaurant_name = str(link.string)

        # parse each restaurants individual url
        total_url = "https://deliveroo.co.uk" + str(restaurant_url)
        # use request to retrieve html source code, then BeautifulSoup to parse
        restaurant_source_code = requests.get(total_url).text
        soup2 = BeautifulSoup(restaurant_source_code, 'html.parser')
        # we want the text from the restaurant's page
        restaurant_text = soup2.get_text()
        print("Text found for " + restaurant_name)
        
        # check if the text of the restaurant's page contains the word we want
        page_check = text_checker(word, restaurant_text) 
        if page_check == True:
            pages_with_word.append(restaurant_name)
    return pages_with_word

def text_checker(word, text):
    """ Function to check for a specific word in the text """
    # using regex to find if the word is in the text, do not care about case
    word_list = re.findall(word, text, flags=re.IGNORECASE)
    if len(word_list) >= 1:
        result = True
    else:
        result = False
    return result

############### Run Management #####################


def main():
    if len(sys.argv) == 1:
        test_word = "chicken" # change this to whatever word you want as your default
        print("Default option selected, running with test word \"" + test_word + "\"...\n")
    elif len(sys.argv) == 2:
        try:
            test_word = str(sys.argv[1])
            print("Running with test word \"" + test_word + "\"...\n")
        except:
            print("Something was wrong with your input, proceeding with default")
            print("Default option selected, running with test word \"" + test_word + "\"...\n")
    else:
        print("Something is wrong with your input, proceeding with default")
        print("Default option selected, running with test word \"" + test_word + "\"...\n") 

    restaurant_html = restaurant_finder()
    result = restaurant_checker(test_word, restaurant_html)
    
    print("\nPages with " + test_word.lower() + " are:")
    print(result)




main()

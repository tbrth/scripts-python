from bs4 import BeautifulSoup
import requests
# import pandas as pandas
# from datetime import date, datetime

url = 'https://www.apple.com/newsroom/archive/iphone/'
newsroom_url_pages = []

def generate_urls():

    newsroom_main_page = requests.get(url, timeout=5)
    
    soup_newsroom_main_page = BeautifulSoup(newsroom_main_page.content, "html.parser")
    
    total_pages = int((soup_newsroom_main_page.find('span', attrs={"class":"pagination-ctrl__info__text pagination-ctrl__info--total"})).text)
    
    for page_increment in range(1, (total_pages + 1)):
        newsroom_url_pages.append('{}?page={}'.format(url, page_increment))
    
    return newsroom_url_pages

def generate_press_release_urls(newsroom_url_pages):
    for page_url in newsroom_url_pages:
        
        response = requests.get(page_url, timeout=5)

        soup = BeautifulSoup(response.content, "html.parser")

        press_releases_found = soup.find_all('span', attrs={'class':'category category_release'})

        print('\nNewsroom Page: {} of {}'.format(newsroom_url_pages.index(page_url)+1, len(newsroom_url_pages)))
        print('Newsroom Page URL: {}'.format(page_url))
        print('Press Releases Found: {}'.format(len(press_releases_found)))

        for press_release in press_releases_found:
            
            parent_anchor_tag = press_release.parent.parent
            
            constructed_link = 'https://www.apple.com/' + parent_anchor_tag['href']
            
            press_release_heading = parent_anchor_tag.find('h3').text.rstrip()

            print('----')
            print('Press Release: {}'.format(press_release_heading))
            print('URL: {}'.format(constructed_link))

if __name__ == "__main__":

    generate_press_release_urls(
        generate_urls()
    )

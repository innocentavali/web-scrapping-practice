from bs4 import BeautifulSoup
import requests
import urllib
import os

# def get_original_photo_url(mid_photo_url):
#     '''
#
#     :param mid_photo_url:
#     :return: The url of the original photo
#     '''
#     mid_directory, photo_name = os.path.split(mid_photo_url)
#     if photo_name.endswith('.webp'):
#         photo_name = photo_name[:len(photo_name) - 5]
#     return ORIGINAL_DIR + photo_name + '.jpg'

source = requests.get('https://movie.douban.com/celebrity/1041025/photos/').text
SOURCE1 = 'douban'

soup = BeautifulSoup(source, 'lxml')

photo_src = soup.find('div', class_='cover').a.img['src']

print(photo_src)

urllib.urlretrieve(photo_src, "3.jpg")

def get_celebrities_photos_url(source):
    '''
    :return: a dictionary, each key with a list of
    '''
    # TODO

    pass

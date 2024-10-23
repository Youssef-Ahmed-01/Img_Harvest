import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

def scrape_images():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    with open('responseImgScraping.html', 'w', encoding='utf-8') as f:
        f.write(response.text)

    images = []
    for img in soup.find_all('img'):
        img_url = img.get('src')
        if img_url:
            img_url = urljoin(url, img_url)
            images.append(img_url)
    return images

def download_image(img_url, folder):
    img_data = requests.get(img_url).content
                #https://example.com/images/picture.jpg -->>>> ['https:', '', 'example.com', 'images', {'picture.jpg'}-1]
    img_name = img_url.split('/')[-1]
    img_path = os.path.join(folder, img_name)
    with open(img_path, 'wb') as img_file:
        img_file.write(img_data)
    print(f"responsed {img_url}")



folder = 'result_img_scraping'
if not os.path.exists(folder):
    os.makedirs(folder)
images = scrape_images()
for img_url in images:
    download_image(img_url, folder)
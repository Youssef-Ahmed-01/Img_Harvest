import os
import requests
from fp.fp import FreeProxy

proxy = FreeProxy(country_id=['US'], timeout=0.3, rand=True).get()
print(f"Using proxy: {proxy}")

url = 'https://www.searchpeoplefree.com/address//fl/opa-locka/nw-139th-st/2381'
proxies = {
    "http": os.environ.get('http_proxy', proxy),
    "https": os.environ.get('https_proxy', proxy),
}

try:
    response = requests.get(url, proxies=proxies, timeout=10)
    response.raise_for_status()

    with open('response.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
    print("Response saved to response.html")

except requests.exceptions.RequestException as e:
    print(f'An error occurred: {e}')

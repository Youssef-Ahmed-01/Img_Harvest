# Image Scraping

## Overview

This python script downloads all images from a given url to scrape images from a website.
make sure that url is working with no need of VPN or proxies


## Usage

1. **Clone the repo and make sure you have python and pip on you system**

2. **Set the URL in the script:**
open imgScraping.py on line 7, replace the default url (BBC url) with the url of the website you want to scrape images from.

3. **run the venv and install requirements**
    ```terminal/bash
    python3 -m venv env
    source venv/bin/activate
    pip install -r requirements.txt
4. **then run using python or python3**  
    ```terminal/bash
    python3 imgScraping.py
5. **to deactivate the venv**  
    ```terminal/bash
    deactivate
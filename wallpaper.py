import os
import ctypes
import requests
from bs4 import BeautifulSoup as bs

SPI_SETDESKWALLPAPER = 20

url = "https://apod.nasa.gov/apod/astropix.html"
res = requests.get(url)
if res.status_code == 200:
    soup = bs(res.text,'html.parser')
    image = soup.find("img")["src"]
    image_url=url[:27]+image
    if not os.path.exists('wps'):
        os.makedirs('wps')
    os.chdir('wps')
    response = requests.get(image_url)
    if response.status_code == 200:
        img_name = image[11:len(image)-4] + ".jpg"
        with open(img_name, 'wb') as f:
            f.write(requests.get(image_url).content)
            f.close()
            print("downloaded the wallpaper: " + img_name)
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, img_name, 0)
        print("wallpaper changed!")
    else:
        print("Error while downloading wallpaper.")
    
else:
    print("Site not reachable/connection broken. Try after sometime...")




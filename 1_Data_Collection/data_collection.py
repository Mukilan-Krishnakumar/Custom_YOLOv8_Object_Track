import time
import os
from selenium import webdriver
import bs4
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# creating a directory to save images
folder_name = '../2_Data_Annotation/images'
if not os.path.isdir(folder_name):
    os.makedirs(folder_name)


def download_image(url, folder_name, num):
    # write image to file
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(folder_name, str(num) + ".jpg"), 'wb') as file:
            file.write(response.content)

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def scrape_images(search_term, number_of_images, starting_number):
    SEARCH_URL = f"https://www.google.com/search?q={search_term}&source=lnms&tbm=isch"
    driver.get(SEARCH_URL)

    a = input("Waiting...")

    # Scrolling all the way up
    driver.execute_script("window.scrollTo(0, 0);")

    page_html = driver.page_source
    pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
    containers = pageSoup.findAll('div', {'class': "isv-r PNCib MSM1fd BUooTd"})

    len_containers = len(containers)
    print(f'Found {len_containers} containers')

    driver.find_element(By.XPATH, """//*[@id="islrg"]/div[1]/div[3]""").click()
    count = starting_number
    end = count + number_of_images + 1
    for i in range(1, len_containers):
        if i % 25 == 0 or count == end:
            continue
        else:
            xPath = f"""//*[@id="islrg"]/div[1]/div[{i}]"""

            # URL of the small preview image
            previewImageXPath = f"""//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img"""
            previewImageElement = driver.find_element(By.XPATH, previewImageXPath)
            previewImageURL = previewImageElement.get_attribute("src")

            driver.find_element(By.XPATH, xPath).click()

            timeStarted = time.time()
            while True:
                imageElement = driver.find_element(By.XPATH,
                                                   """//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img""")
                imageURL = imageElement.get_attribute("src")

                if imageURL != previewImageURL:
                    break

                else:
                    # timeout functionality
                    current_time = time.time()

                    if current_time - timeStarted > 10:
                        print("Timeout will move on to next image")
                        break
            # Downloading image
            try:
                download_image(imageURL, folder_name, count)
                count += 1
                print("Downloaded element %s out of %s total. URL: %s" % (i, len_containers + 1, imageURL))
            except:
                print("Couldn't download an image %s, continuing downloading the next one" % (i))

scrape_images("bengal+tiger", 100, 0)
scrape_images("indian+elephant", 100, 100)
scrape_images("indian+rhinoceros",100,200)
scrape_images("indian+bison",100,300)
scrape_images("indian+leopard",100,400)
scrape_images("asiatic+lion",100,500)
time.sleep(10)
driver.quit()
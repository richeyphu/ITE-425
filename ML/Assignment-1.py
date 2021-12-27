# AI Assignment I

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import urllib.request
import os
import sys


def get_driver():
    path = 'chromedriver'
    driver = webdriver.Chrome(executable_path=path)
    driver.get(f'https://www.google.com/search?q={keyword}&tbm=isch')

    for i in range(0, 7):
        driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
        try:
            # for clicking show more results button
            driver.find_element_by_xpath(
                '//*[@id="islmp"]/div/div/div/div/div[2]/div[2]/input').click()
        except Exception as e:
            pass
        time.sleep(3)
    return driver


def download_images(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # print(soup)

    img_tags = soup.find_all('img', class_='rg_i')
    length = len(img_tags)

    # get pic and download
    for i, v in enumerate(img_tags):
        try:
            # print(v['src'])
            # print('\n ----------- \n')
            loading_bar(i + 1, length)

            urllib.request.urlretrieve(
                v['src'], f"./downloads/{keyword}/{str(i + 1)}.jpg")
        except Exception as e:
            pass
    print()


def loading_bar(n, l):
    print("\rDownloading : {} ({:.2f}%)".format(
        "█" * round(n / l * 100 / 2), n / l * 100), end="")


def create_dir():
    try:
        os.makedirs('downloads/{}'.format(keyword))
    except Exception as e:
        print(e)


def main():
    global keyword

    args = sys.argv
    if len(args) == 1:
        keyword = input('Enter Keyword : ')
    else:
        keyword = args[1]
        print(f'{keyword=}')

    create_dir()
    driver = get_driver()
    print('=' * 100)
    download_images(driver)
    print('=' * 100)
    print('Done!')


if "__main__" == __name__:
    main()

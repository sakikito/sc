import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request


BASE_DIR = os.path.dirname(__file__)


def get_output_dir_path():
    """アウトプットディレクトリの絶対パスを取得
    Returns (str): アウトプットディレクトリの絶対パス
    """
    output_dir_path = os.path.join(BASE_DIR, "output")

    # outputディレクトリが存在しない場合
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)

    return output_dir_path


# Chromeの起動
driver = webdriver.Chrome()

# 目的webへのリンクを取得する
driver.get("https://free-materials.com/tag/%E9%87%8E%E8%8F%9C/")

# class name
elems_vegetable = driver.find_elements(By.CLASS_NAME, "post-list-thumb")

# urlの配列
urls = []

for vegetable in elems_vegetable:

    # img tag
    tag_vegetable = vegetable.find_element(By.TAG_NAME, 'img')

    # src img link
    src = tag_vegetable.get_attribute('src')

    urls.append(src)

# outputディレクトリのパスを取得
output_dir_path = get_output_dir_path()
index = 1

for url in urls:
    savename = f"vegetable_{str(index)}.jpg"
    index += 1
    vegetable = urllib.request.urlopen(url).read()

    save_file_path = os.path.join(output_dir_path, savename)

    with open(save_file_path, mode="wb") as f:
        f.write(vegetable)

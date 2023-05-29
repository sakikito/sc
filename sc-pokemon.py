from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.request
import os

# Pythonで実行中のファイルの場所(パス)を取得する
BASE_DIR = os.path.dirname(__file__)

def get_output_dir_path():

    # パスを結合する
    output_dir_path = os.path.join(BASE_DIR, "output_pokemon")

    if not os.path.exists(output_dir_path):

        os.makedirs(output_dir_path)

    return output_dir_path

# Chromeの起動
driver = webdriver.Chrome()
driver.get("https://vercel-pokedex-gnticcdqg-kkml4220.vercel.app/")

urls = []
for page in range(5):

    # cardを取得
    elems_pokemon = driver.find_elements(By.CLASS_NAME, "card")

    for pokemon in elems_pokemon:
                  
        # imgタグの取得
        tag_pokemon = pokemon.find_element(By.TAG_NAME, "img")

        # imgのリンクを取得
        src = tag_pokemon.get_attribute('src')

        # urlを配列に格納
        urls.append(src)

    if page != 4:
        # 次ページに遷移
        elems_link = driver.find_elements(By.CLASS_NAME, "page-link")
        elems_link[-1].click()
        time.sleep(5)

output_dir_path = get_output_dir_path()
index = 1

for url in urls:

    savename = f"pokemon_{str(index)}.jpg"
    index += 1
    pokemon = urllib.request.urlopen(url).read()

    save_file_path = os.path.join(output_dir_path, savename)

    with open(save_file_path, mode="wb") as f:
        f.write(pokemon)

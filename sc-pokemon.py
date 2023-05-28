from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.request

# Chromeの起動
driver = webdriver.Chrome()
driver.get("https://vercel-pokedex-gnticcdqg-kkml4220.vercel.app/")

url = []
for page in range(5):

    # cardを取得
    elems_pokemon = driver.find_elements(By.CLASS_NAME, "card")

    for pokemon in elems_pokemon:
                  
        # imgタグの取得
        tag_pokemon = pokemon.find_element(By.TAG_NAME, "img")

        # imgのリンクを取得
        src = tag_pokemon.get_attribute('src')

        # urlを配列に格納
        url.append(src)

    if page != 4:
        # 次ページに遷移
        elems_link = driver.find_elements(By.CLASS_NAME, "page-link")
        elems_link[-1].click()
        time.sleep(5)

for i in range(len(url)):

    savename =  "C:/python_workspace/scraping/pokemon_image/" + "pokemon" + str(i) + ".png"
    pokemon = urllib.request.urlopen(url[i]).read()

    with open(savename, mode="wb") as f:
        f.write(pokemon)
        print("保存しました")

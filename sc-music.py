import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request

driver = webdriver.Chrome()

# 5月29日時点のランキング(更新する必要あり)
driver.get("https://www.oricon.co.jp/music/rankinglab/dis/2023-05-29/")

detail_music = driver.find_elements(By.CLASS_NAME, "media-information")

for music in detail_music:

    # 名前を取得
    music_name = music.find_element(By.CLASS_NAME, "media-title").text

    # 価格を取得
    music_artist = music.find_element(By.CLASS_NAME, "media-artist").text

    # 内容
    music_addinformation = music.find_element(By.CLASS_NAME, "add-information")
    music_startday = music_addinformation.find_element(By.CLASS_NAME, "media-release").text

    music_object = {
        "name": music_name,
        "price": music_artist,
        "startday": music_startday,
    }

    print(music_object)

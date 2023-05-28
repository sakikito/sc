from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request

# Chromeの起動
driver = webdriver.Chrome()

# 目的webへのリンクを取得する
driver.get("https://free-materials.com/tag/%E9%87%8E%E8%8F%9C/")

# class name
elems_vegetable = driver.find_elements(By.CLASS_NAME, "post-list-thumb")

# urlの配列
url = []

for vegetable in elems_vegetable:

    # img tag
    tag_vegetable = vegetable.find_element(By.TAG_NAME, 'img')

    # src img link
    src = tag_vegetable.get_attribute('src')

    url.append(src)

for i in range(len(url)):

    savename =  "C:/python_workspace/image-folder/complete-image/" + "vegetable" + str(i) + ".jpg"
    vegetable = urllib.request.urlopen(url[i]).read()

    with open(savename, mode="wb") as f:
        f.write(vegetable)
        print("保存しました")

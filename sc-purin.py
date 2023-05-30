import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request

BASE_DIR = os.path.dirname(__file__)

def get_output_dir_path():

    output_dir_path = os.path.join(BASE_DIR, "output_purin")

    if not os.path.exists(output_dir_path):

        os.makedirs(output_dir_path)

    return output_dir_path

driver = webdriver.Chrome()

driver.get("https://www.shop.puddinglaboratory.jp/shopbrand/all/")

image_purin = driver.find_elements(By.CLASS_NAME, "M_cl_imgWrap")

urls = []

for purin in image_purin:

    # 画像のURLを配列urlsに格納する
    tag_purin = purin.find_element(By.TAG_NAME, "img")
    src = tag_purin.get_attribute('src')
    urls.append(src)

detail_purin = driver.find_elements(By.CLASS_NAME, "M_cl_detail")

for purin in detail_purin:

    # 商品の詳細をスクレイピングする
    # 名前を取得
    purin_name = purin.find_element(By.CLASS_NAME, "M_cl_name").text

    # 価格を取得
    purin_price = purin.find_element(By.CLASS_NAME, "M_cl_price").text

    # プリンの内容
    purin_content = purin.find_element(By.CLASS_NAME, "M_cl_content")

    purin_object = {
        "name": purin_name,
        "price": purin_price,
        "content": purin_content,
    }

    print(purin_object)

output_dir_path = get_output_dir_path()
index = 1

for url in urls:

    savename = f"purin_{str(index)}.jpg"
    index += 1
    purin = urllib.request.urlopen(url).read()

    save_file_path = os.path.join(output_dir_path, savename)

    with open(save_file_path, mode ="wb") as f:
        f.write(purin)
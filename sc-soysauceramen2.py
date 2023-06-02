from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import os

BASE_DIR = os.path.dirname(__file__)

def get_output_dir_path():

    output_dir_path = os.path.join(BASE_DIR, "output_soysauceramen2")

    if not os.path.exists(output_dir_path):

        os.makedirs(output_dir_path)

    return output_dir_path

driver = webdriver.Chrome()

# 醤油ラーメン
driver.get("https://www.photo-ac.com/main/search?q=%E9%86%A4%E6%B2%B9%E3%83%A9%E3%83%BC%E3%83%A1%E3%83%B3&srt=dlrank&qt=&p=2")

image_ramen = driver.find_elements(By.TAG_NAME, "figure")

urls = []

for ramen in image_ramen:

    # 画像のURLを配列urlsに格納する
    tag_ramen = ramen.find_element(By.TAG_NAME, "img")
    src = tag_ramen.get_attribute('src')
    urls.append(src)

output_dir_path = get_output_dir_path()
index = 1

for url in urls:

    savename = f"ramen_{str(index)}.jpeg"
    index += 1
    ramen = urllib.request.urlopen(url).read()

    save_file_path = os.path.join(output_dir_path, savename)

    with open(save_file_path, mode ="wb") as f:
        f.write(ramen)


# excelファイルにラーメンの名前を書き込む

detail_ramen = driver.find_elements(By.TAG_NAME, "figure")

names = []

for ramen in detail_ramen:

    # 画像のURLを配列urlsに格納する
    tag_ramen = ramen.find_element(By.TAG_NAME, "img")
    title = str(tag_ramen.get_attribute('title'))
    names.append(title)

# excelファイルに書き込む

tmp_num = len(detail_ramen)
 
##以下、エクセル出力に関する部分
import openpyxl
 
wb = openpyxl.Workbook() #エクセルファイルを新規作成
sheet = wb.active
sheet.title = 'ramen' 
 
sheet["A1"].value = 'ラーメン'
 
for i in range(1, tmp_num):
    sheet.cell(column=1, row = i+1, value=names[i-1])

wb.save('soysauceramen_excel2.xlsx')
wb.close()
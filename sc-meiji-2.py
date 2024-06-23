from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome()
# 2023年6月末から2023年12月末まで
driver.get("https://www.jleague.jp/match/search/?category%5B%5D=j1&club%5B%5D=sapporo&club%5B%5D=kashima&club%5B%5D=urawa&club%5B%5D=kashiwa&club%5B%5D=ftokyo&club%5B%5D=tokyov&club%5B%5D=machida&club%5B%5D=kawasakif&club%5B%5D=yokohamafm&club%5B%5D=shonan&club%5B%5D=niigata&club%5B%5D=iwata&club%5B%5D=nagoya&club%5B%5D=kyoto&club%5B%5D=gosaka&club%5B%5D=cosaka&club%5B%5D=kobe&club%5B%5D=hiroshima&club%5B%5D=fukuoka&club%5B%5D=tosu&year=2023&month%5B%5D=07&month%5B%5D=08&month%5B%5D=09&month%5B%5D=10&month%5B%5D=11&month%5B%5D=12&section=")

detail_soccer = driver.find_elements(By.CLASS_NAME, "gameTable")

homes = []
aways = []
hscores = []
ascores = []
for soccer in detail_soccer:

    home_team = soccer.find_element(By.CSS_SELECTOR, ".clubName.leftside").text
    homes.append(home_team)

    away_team = soccer.find_element(By.CSS_SELECTOR, ".clubName.rightside").text
    aways.append(away_team)

    home_score = soccer.find_element(By.CSS_SELECTOR, ".point.leftside").text
    hscores.append(home_score)

    away_score = soccer.find_element(By.CSS_SELECTOR, ".point.rightside").text
    ascores.append(away_score)

filename = './output/meiji_j1_2.csv'
with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['HOME', 'AWAY', 'HSCORE', 'ASCORE'])
    for i in range(len(homes)):
        writer.writerow([homes[i], aways[i], hscores[i], ascores[i]])
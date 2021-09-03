from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys

# windowsの場合 (Cドライブ直下にchromedriver.exeがある前提)
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe") # Macの方はこの行をコメントアウト

### 1.Webサイトにアクセスする
driver.get("https://aiacademy.jp/")

print(driver.title)
print("test")
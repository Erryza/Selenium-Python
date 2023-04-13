from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

webPage = ["tiket", "tokopedia", "orangsiber",
           "demoqa", "automatetheboringstuff"]

for i in webPage:
    driver.get(f"http://www.{i}.com")
    print(f"{i} -", driver.title)
driver.close()

# importujemy selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
# ścieżka do sterownika, w tym przypadku Google Chrome
PATH = "CODE/chromedriver"
driver = webdriver.Chrome(PATH)

print("kron0s")
print("NewtonPL 2022")
print("natangrygiel.pl")
print("=================")
print("sesja:")
print("(1) nowa, (2)niezakończona")
sesyja = int(input())
print("=================")

#wczytujemy bazę słówek, w CODE/instaling_n.config
baza = {}
with open('CODE/instaling_n.config', encoding="utf-8") as f:
    for line in f:
        key, value = line.split("=")
        baza[key.strip()] = value.strip(" \"\n")

print("wczytano słówka z pliku config")
#otwieramy instaling
driver.get("https://instaling.pl/teacher.php?page=login")
print("wczytano instaling")
#logujemy się
nazwa = driver.find_element(By.ID, "log_email")
nazwa.send_keys("nick")

haslo = driver.find_element(By.ID, "log_password")
haslo.send_keys("haslo")
haslo.send_keys(Keys.RETURN)

sesja = driver.find_element(By.CLASS_NAME, "sesion")
sesja.click()
print("zalogowano")
#zależy czy masz otwartą sesję
if sesyja == 1:
    strt = driver.find_element(By.ID, "start_session_button")
else:
    strt = driver.find_element(By.ID, "continue_session_button")
strt.click()
time.sleep(2)
licznik = 0
#wypełniamy pole [slowa] razy
for i in range(10):
    #wyszukujemy słowo
    word = driver.find_element(By.CLASS_NAME, "translations").text
    #wpisujemy odpowiedź z bazy danych
    odp = driver.find_element(By.ID, "answer")
    odp.send_keys(baza[word])
    #sprawdzamy
    spr = driver.find_element(By.ID, "check")
    spr.click()
    licznik = licznik + 1
    print(licznik, " słowo wpisane")
    time.sleep(1)
    #kolejne słówko
    kolejne = driver.find_element(By.ID, "next_word")
    kolejne.click()
    time.sleep(1)
print("sesja zrobiona, zamykanie")
driver.quit()

# kron0s
Zautomatyzowane sesje do Insta.ling.

## Instalacja
<h2>Metoda 1 (zalecana):</h2>
Użyj podanych skryptów aby zainstalować Pythona 3 oraz wymagane paczki:


Windows(jako administrator) `kron0s_setup_win.ps1`


Linux(pacman & sudo) `kron0s_setup_linux.sh`
 
 

w przypadku innych dystrybucji, zamień pacmana na swój ulubiony menedżer paczek, oraz zamień sudo na doas, gdy go używasz.


<h2>Metoda 2:</h2>
Pobierz Pythona i użyj pip by pobrać wymagane paczki.


[pip](https://pip.pypa.io/en/stable/) się pobiera samemu na systemach Windows, jednak na systemach typu Linux musi on być zainstalowany manualnie (zobacz wiki swojej dystrybucji).

Instalacja:
```bash
pip install selenium
pip install tkinter
```

## Poradnik
Najpierw wpisz dane logowania
```python
#logujemy się
nazwa = driver.find_element(By.ID, "log_email")
nazwa.send_keys("TU WPISZ LOGIN")

haslo = driver.find_element(By.ID, "log_password")
haslo.send_keys("TU WPISZ HASŁO")
```
potem załaduj bazę danych, wystarczy tylko wrzucić plik do folderu CODE pod nazwą:


`instaing_a.config` - język angielski


`instaling_n.config` - język niemiecki
## Kontrybucje
Masz pomysł na ulepszenie programu? droga wolna!
## Licencja
[MIT](https://choosealicense.com/licenses/mit/)

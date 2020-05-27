# Zadania dla uczestników demonstracji pt. Okienkowy menadżer uruchamiania skryptów i aplikacji w systemie Linux.

### Wymagania
Python w wersji 3.5+ (rekomendowany 3.7)

Biblioteka PyQt5

Biblioteka PyQt5-sip


```
pip install PyQt5

```


# Zadania

### Zadanie 1:

* Dodaj nowe pole `description` do *ApplicationData* - uwzględnij pole w konstruktorze i funkcjach odpowiedzialnych za serializację: ***as_dict***, ***from_dict***.
* Dodaj wyświetlanie pola `description` w *ApplicationWidget*.
* Dodaj możliwość edycji pola jako QLineEdit w *ApplicationSettingsWidget*.
* Powyższe punkty można zrealizować analogicznie do pola name.


### Zadanie 2:

* Dodaj nowe okno podobne do **TopViewWindow** zwracające wynik komendy `cat /proc/meminfo`.
* Dodaj możliwosć otwarcia okna w menu _Tools_.

    
Zachęcam do korzystania z prezentacji oraz dokumentacji: PyQt5: https://doc.qt.io/qtforpython/api.html.
# JPWP
Zanim zaczniesz należy urochomić server apache oraz mysql, za pomocą którego będziesz mógł korzystać z bazy danych.  
Jeżeli korzystasz, z aplikacji XAMPP Server, postępuj zgodnie z krokami:  
**Dla systemu Windows:**  
* Uruchom serwer Apache oraz MySQL klikając przycisk start. (Przycisk Admin przy MySQL prowadzi do phpmyadmin).
* W folderze xampp/htdocs utwórz folder JPWP, tutaj będziesz zamieszczać wszystkie pliki .php.  
**Dla systemu macOS:**   
* W zakładce general kliknij przycisk Start. 
* W zakładce Network zezwól na połączenie localhost:8080 -> 80 (Over SSH)
* W zakładce Volumes kliknij przycisk Mount
* Upewnij się, że w zakładce Services Apache oraz Mysql są włączone.
* W folderze lampp/htdocs utwórz folder JPWP, tutaj będziesz zamieszczać wszystkie pliki .php.  
**Dla systemu Linux:**   
Zachęcam zainstalowanie Apache oraz MySQL z poziomu konsoli, a następnie w folderze public_html lub innym określonym jako katalog publiczny utworzyć folder JPWP.  
UWAGA: Wszystkie klasy obsługujące kod w Javie znajdują się pod adresem app/src/main/java/com/example/jpwp.  
# Zadanie 1.
W tym zadaniu zajmiemy się kodem z pliku registration.php, tak aby rejestracja na emulatorze przebiegła pomyślnie.  
Na początku wejdź w przeglądarce pod adres localhost/phpmyadmin (lub localhost:8080/phpmyadmin) utwórz nową bazę danych i nazwij ją JPWP, następnie przeklej poniższe zapytanie:    
CREATE TABLE `registration` (
      `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,  
      `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,  
      `surname` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,  
      `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL UNIQUE KEY,  
      `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL 
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;  
    
  1.a) Uzupełnij brakujące wyrażenia regularne znajdujące się w pliku registration.php.  
  Zmienna email - rozpoczyna się od identyfikatora użytkownika następnie @, domena, "." i końcówka domeny.  
  Zmienna name - same litery, użytkownik może podać więcej niż jedno imię.  
  Zmienna surname - chcemy, aby użytkownik podał TYLKO jedno słowo, które może zawierać w sobie "-".  
  PODPOWIEDŹ: Skorzystaj ze strony https://regexr.com/, aby sprawdzić, czy wyrażenia spełniają swoje zadanie.  
  1.b) Napisz odpowiednią instrukcję warunkową, która sprawdza, czy podane hasła są takie same, jeśli nie, poinformuj użytkownika np. funkcją "echo", że podane hasła się różnią.  
  
# Zadanie 2.
Twoim zadaniem, będzie obsługa panelu do logowania.  
  2.a) Stwórz plik login.php i napisz kod, który wykonuje odpowiednie zapytanie do bazy danych. W przypadku niepowodzenia, poinformuj o tym użytkownika, jeżeli logowanie przebiegnie poprawnie użytkownik powinien zobaczyć informację "Hello <imię_użytkownika>!".  
  Podpowiedź: Dla zapytania SELECT należy użyć funkcji mysqli_stmt_bind_result($stmt, $name) oraz mysqli_stmt_fetch($stmt). Reszta kodu powinna wyglądać podobnie jak w registration.php.  
  2.b) Napisz obsługę przycisku buttonLogin znajdującego się w pliku Login.java, po którego kliknięciu wywołasz napisany przez siebie kod login.php. Skorzystaj z klasy BackgroundTask i sprawdź jakie argumenty przyjmuje metoda doInBackground(). Pamiętaj, że jest to zadanie odtwórcze i możesz zainspirować się obsługą przycisku z klasy MainActivity :).

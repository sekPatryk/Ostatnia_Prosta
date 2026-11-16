# Architektura MVC – Ostatnia Prosta

Projekt **Ostatnia Prosta** jest niewielką aplikacją webową napisaną w Pythonie z użyciem Flask i SQLite. Kod został podzielony zgodnie ze wzorcem MVC (Model–View–Controller), aby oddzielić obsługę danych, logikę żądań HTTP i prezentację interfejsu.

## Model (Model)

Model znajduje się w katalogu `models/`, przede wszystkim w pliku `rezerwacja.py`.

Odpowiada za:
- pobieranie listy kaplic i rezerwacji z bazy SQLite;
- sprawdzanie dostępności kaplicy w wybranym przedziale czasu;
- dodawanie rezerwacji;
- pobieranie rezerwacji użytkownika;
- anulowanie rezerwacji należącej do danego użytkownika.

Model zawiera logikę operacji na danych. Kontrola konfliktów terminów odbywa się po stronie modelu, a nie w szablonach HTML.

## Widok (View)

Widoki znajdują się w katalogu `templates/rezerwacje/`:
- `W01_lista_kaplic.html` – lista kaplic i informacja o zajętych terminach;
- `W02_formularz_rezerwacji.html` – formularz tworzenia rezerwacji;
- `W03_moje_rezerwacje.html` – lista rezerwacji użytkownika oraz formularz anulowania;
- `baza.html` – wspólny szablon bazowy strony.

Widoki odpowiadają za prezentację danych i formularzy użytkownikowi. Nie powinny samodzielnie wykonywać zapytań SQL ani podejmować decyzji biznesowych.

## Kontroler (Controller)

Kontroler znajduje się w `controllers/rezerwacje.py`. Jest to Blueprint Flask obsługujący ścieżki związane z rezerwacjami.

Odpowiada za:
- odbieranie żądań HTTP;
- pobieranie i walidowanie danych z formularzy;
- wywoływanie odpowiednich metod modelu;
- przekazywanie danych do szablonów;
- przekierowania i komunikaty dla użytkownika.

Plik `app.py` tworzy aplikację Flask, konfiguruje ją, rejestruje Blueprint i inicjalizuje bazę danych.

## Przepływ działania

Przykładowy przepływ utworzenia rezerwacji:

1. Użytkownik otwiera formularz w przeglądarce.
2. Kontroler obsługuje żądanie i wyświetla widok formularza.
3. Użytkownik przesyła formularz.
4. Kontroler sprawdza poprawność danych.
5. Model sprawdza dostępność kaplicy i zapisuje rezerwację w SQLite, jeśli termin nie koliduje z inną aktywną rezerwacją.
6. Kontroler przekazuje komunikat i przekierowuje użytkownika do odpowiedniego widoku.

Taki podział ułatwia rozwijanie i testowanie aplikacji, ponieważ warstwa prezentacji, obsługa żądań i operacje na danych są od siebie oddzielone.

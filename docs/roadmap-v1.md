# Mapa Drogowa Wersji v1 (Roadmap v1) – Ostatnia Prosta

## 1. Cel i granice wersji v1
Celem pierwszej iteracji (v1) jest uruchomienie działającego lokalnie prototypu systemu „Ostatnia Prosta”, który umożliwia przeglądanie dostępnych kaplic/terminów, zarezerwowanie wybranego terminu ceremonii przez klienta oraz podgląd i anulowanie własnych rezerwacji.

## 2. Widoki (W01 – W03)
* **W01: Lista terminów i kaplic**
  * *Użytkownik:* Klient / Gość
  * *Opis:* Wyświetla listę dostępnych sal i kaplic pogrzebowych wraz ze statusami dostępności.
* **W02: Formularz rezerwacji ceremonii**
  * *Użytkownik:* Klient
  * *Opis:* Pola wyboru sali, daty rozpoczęcia i zakończenia, dane osoby zamawiającej oraz wybór pakietu usług.
* **W03: Panel „Moje rezerwacje”**
  * *Użytkownik:* Zalogowany klient (demo nr 1)
  * *Opis:* Zestawienie aktywnych rezerwacji użytkownika z opcją ich anulowania.

## 3. Struktura bazy danych (SQLite)
* **Tabela `uzytkownik`:**
  * `id` (INTEGER, PK)
  * `imie` (TEXT)
  * `email` (TEXT)
* **Tabela `sala` (lub `kaplica`):**
  * `id` (INTEGER, PK)
  * `nazwa` (TEXT)
* **Tabela `rezerwacja`:**
  * `id` (INTEGER, PK)
  * `uzytkownik_id` (INTEGER, FK -> uzytkownik.id)
  * `sala_id` (INTEGER, FK -> sala.id)
  * `poczatek` (DATETIME)
  * `koniec` (DATETIME)
  * `status` (TEXT)

## 4. Funkcjonalności MVP
* **F01:** Sprawdzanie dostępności sal w wybranym przedziale czasowym (uwzględniając warunek nakładania się terminów).
* **F02:** Zapis nowej rezerwacji w bazie danych SQLite.
* **F03:** Anulowanie własnej rezerwacji przez użytkownika demo (zmiana statusu rekordu).

## 5. Kierunki rozwoju na wersję v2
1. **Moduł cyfrowych epitafiów:** Dodanie tabeli `epitafium` powiązanej z rezerwacją oraz generowanie kodu QR dla nagrobka/pamiątki.
2. **Panel administracyjny:** Rozbudowa widoków o zarządzanie cennikiem dodatków (np. warianty urn/trumien, oprawa muzyczna).
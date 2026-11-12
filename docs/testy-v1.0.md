# Scenariusze testowe – Ostatnia Prosta v1.0

**Przykładowe statusy:**
- `Do wykonania` – test nie został jeszcze przeprowadzony;
- `Działa` – wynik jest zgodny z oczekiwaniem;
- `Nie działa` – wynik jest niezgodny z oczekiwaniem;
- `Zablokowany` – testu nie można wykonać z powodu innego problemu.

## Tabela scenariuszy

| ID | Funkcjonalność / scenariusz | Kroki i dane testowe | Oczekiwany rezultat | Status |
|---|---|---|---|---|
| T01 | F01 – wyświetlenie listy kaplic | Otworzyć stronę główną aplikacji lub `/rezerwacje/`. | Wyświetla się lista kaplic pobrana z bazy danych. | Działa |
| T02 | F01 – dostępność kaplicy | Wybrać kaplicę i sprawdzić prezentowane zajęte terminy. | Widok pokazuje informacje o aktywnych rezerwacjach. | Działa |
| T03 | F02 – poprawna rezerwacja | Wybrać kaplicę, przyszłą datę i poprawny przedział godzin, a następnie wysłać formularz. | Rezerwacja zostaje zapisana i pojawia się na liście użytkownika. | Działa |
| T04 | F02 – niepoprawna data | Wysłać formularz z datą w przeszłości lub niepoprawnym formatem. | Rezerwacja nie zostaje zapisana; użytkownik otrzymuje komunikat o błędzie. | Działa |
| T05 | F02 – niepoprawne godziny | Podać godzinę zakończenia wcześniejszą lub równą godzinie rozpoczęcia. | Formularz zostaje odrzucony; rezerwacja nie powstaje. | Działa |
| T06 | Konflikt terminów – nakładanie się | Dodać rezerwację, a następnie spróbować zarezerwować tę samą kaplicę w nakładającym się przedziale. | Druga rezerwacja zostaje odrzucona z komunikatem o zajętym terminie. | Działa |
| T07 | Konflikt terminów – różne kaplice | Zarezerwować ten sam przedział godzin dla dwóch różnych kaplic. | Obie rezerwacje mogą zostać zapisane. | Działa |
| T08 | Konflikt terminów – przedziały stykające się | Ustawić koniec pierwszej rezerwacji na 12:00, a początek kolejnej na 12:00 dla tej samej kaplicy. | Rezerwacje nie są traktowane jako nakładające się. | Działa |
| T09 | F03 – lista własnych rezerwacji | Otworzyć `/rezerwacje/moje`. | Wyświetlają się rezerwacje użytkownika demonstracyjnego ID 1. | Działa |
| T10 | F03 – anulowanie własnej rezerwacji | Anulować aktywną rezerwację z poziomu listy. | Status rezerwacji zmienia się na `anulowana`; rezerwacja nie jest usuwana z bazy. | Działa |
| T11 | F03 – ponowne anulowanie | Spróbować anulować rezerwację, która ma już status `anulowana`. | Operacja nie zmienia danych; użytkownik otrzymuje odpowiedni komunikat lub pozostaje na liście. | Działa |

## Wyniki testów

| Data testu | Osoba testująca | Liczba testów | Działa | Nie działa | Uwagi |
|---|---|---:|---:|---:|---|
| 11.11.2026 | Sęk Patryk | po 2+ | 12 | 0 | 12-godzinny format, brak prostego i niezawodnego rozwiązania na ten moment |

# Prompty wykorzystane przy tworzeniu MVC v1.0

> **Uwaga:** poniższe treści to uporządkowane szablony promptów (P1–P4) zgodne z wymaganiami Laboratorium 04, odzwierciedlające kolejne etapy budowy aplikacji „Ostatnia Prosta”.

## P1 – Plan MVP i mapa MVC

**Prompt:**
> Zaplanuj MVP 1.0 projektu „Ostatnia Prosta” (system rezerwacji kaplic). Cel użytkownika: sprawdzić dostępne terminy kaplic, zarezerwować termin i anulować własną rezerwację (użytkownik demo ID 1). Stos: Python 3, Flask, SQLite (`sqlite3`). Zakres:
> - F01 – wyświetlanie kaplic i sprawdzanie ich dostępności;
> - F02 – tworzenie rezerwacji z walidacją danych i kontrolą konfliktów czasowych;
> - F03 – wyświetlanie i anulowanie rezerwacji zalogowanego użytkownika.
> 
> Przygotuj plan wykorzystania kodu z podziałem na model (`models/`), widok (`templates/`) i prosty kontroler (`controllers/`). Dla każdej funkcji wskaż pliki MVC oraz warunek poprawności. Wynik: mapa plików i kolejność zmian.

**Rzeczywisty wynik:**
Uzyskano przejrzystą strukturę katalogów (`app.py`, `database.py`, `models/rezerwacja.py`, `controllers/rezerwacje.py`, `templates/rezerwacje/`) oraz przypisanie odpowiedzialności zgodne ze wzorcem MVC.

---

## P2 – Działający szkielet lub uporządkowanie kodu MVC

**Prompt:**
> Wykonaj pierwszy etap zaakceptowanego planu dla „Ostatnia Prosta”. Technologie: Python 3, Flask, SQLite (`sqlite3`). Wyodrębnij model, widoki i kontroler:
> 1. Przygotuj bazę SQLite z tabelami: `uzytkownik`, `sala` (kaplica) oraz `rezerwacja` (z kluczami PK, FK i włączonym `PRAGMA foreign_keys = ON`).
> 2. Kontroler (Flask Blueprint) ma odbierać żądania, wywoływać model i wybierać widok lub przekierowanie.
> 3. Szablony Jinja2: `baza.html`, `W01_lista_kaplic.html`, `W02_formularz_rezerwacji.html`, `W03_moje_rezerwacje.html`.
> 4. Zwróć drzewo katalogów, pełny kod plików, `requirements.txt`, `.gitignore` i instrukcję uruchomienia dla Windows w `.venv`. Kryterium: aplikacja startuje i pokazuje dane z modelu.

**Rzeczywisty wynik:**
Wygenerowano kompletny szkielet aplikacji. Po skonfigurowaniu środowiska `.venv` i instalacji Flaska serwer wystartował pod adresem `http://127.0.0.1:5000`, poprawnie inicjalizując bazę w `instance/ostatnia_prosta.db` i wyświetlając listę kaplic.

---

## P3 – Jedna funkcja MVP z przykładami wyniku (F02 – rezerwacja i konflikty)

**Prompt:**
> W aktualnym kodzie wykonaj F02 – zapis nowej rezerwacji z kontrolą konfliktów. Użytkownik: demonstracyjny ID 1. Dane wejściowe: `id_sali`, `data_rezerwacji`, `godzina_od`, `godzina_do`. 
> Reguły modelu: używaj wyłącznie zapytań parametryzowanych. Dwa przedziały kolidują dla tej samej aktywnej sali, gdy: `istniejaca.godzina_od < nowa.godzina_do AND istniejaca.godzina_do > nowa.godzina_od`.
> Przykład poprawny: sala zajęta 10:00–11:00 -> nowa rezerwacja 11:00–12:00 zostaje zapisana i pojawia się w W03.
> Przykład błędny: sala zajęta 10:00–11:00 -> nowa rezerwacja 10:30–11:30 zostaje odrzucona z komunikatem błędu.
> Zwróć zmienione pliki i kroki sprawdzenia po restarcie serwera.

**Rzeczywisty wynik:**
Zaimplementowano pełną walidację w modelu i kontrolerze. Testy potwierdziły poprawne blokowanie nakładających się terminów, akceptację terminów stykających się (np. koniec o 12:00, start o 12:00) oraz trwały zapis w bazie po restarcie aplikacji.

---

## P4 – Diagnoza i poprawka przed odbiorem

**Prompt:**
> Sprawdź komplet plików projektu pod kątem zgodności nazw endpointów, pól formularzy i obsługi błędów. 
> Zgłoszone niezgodności: 
> 1. Po zapisaniu rezerwacji przekierowanie odwołuje się do nieistniejącego endpointu `rezerwacje.moje_rezerwacje`.
> 2. Po błędzie walidacji formularza W02 resetuje się wybrana wcześniej data.
> 3. W formularzu rezerwacji pole `<input type="time">` wyświetla w niektórych przeglądarkach format 12-godzinny (AM/PM) zamiast 24-godzinnego `HH:MM`.
> Ustal przyczyny i zaproponuj najmniejsze poprawki zachowujące podział MVC.

**Poprawiony prompt i wynik (iteracja):**
- **Endpointy i data:** Poprawiono przekierowanie w kontrolerze na `url_for("rezerwacje.moje_rezerwacje_widok")` oraz dodano przekazywanie zmiennej `domyslna_data` przy ponownym renderowaniu szablonu po błędzie walidacji.
- **Format godziny:** Zdiagnozowano, że format wyświetlania `<input type="time">` zależy od ustawień lokalnych przeglądarki.
- **Przegląd końcowy:** Potwierdzono pełną zgodność z mapą MVP 1.0 (działają F01, F02 i F03, zachowane jest bezpieczeństwo anulowania tylko własnych rezerwacji).

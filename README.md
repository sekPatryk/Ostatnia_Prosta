# Ostatnia Prosta – System Zarządzania Usługami Pogrzebowymi i Pamiątkowymi

## Zespół
* **Nazwa zespołu:** Ostatnia Prosta Team (nazwa robocza)
* **Skład:** Radzka Maria, Sęk Patryk (Informatyka Ogólna)
* **Repozytorium GitHub:** [https://github.com/sekPatryk/Ostatnia_Prosta](https://github.com/sekPatryk/Ostatnia_Prosta)
* **Przestrzeń LaboChat.com:** [https://io-rs.labochat.com](https://io-rs.labochat.com)

## Idea i problem
Współczesna branża usług pogrzebowych często opiera się na tradycyjnych, papierowych formularzach i nieprzejrzystych cennikach, co w trudnych momentach życiowych stanowi dodatkowe obciążenie dla klientów. Obecny sposób zarządzania rezerwacjami terminów ceremonii, wyborem akcesoriów oraz pamiątek cyfrowych jest nieskoordynowany. Nasz projekt – Ostatnia Prosta – rozwiązuje ten problem poprzez dostarczenie intuicyjnej platformy webowej. Umożliwia ona rodzinom zdalne zaplanowanie ceremonii, personalizację zamówienia (w tym unikalne usługi dodatkowe) oraz stały dostęp do cyfrowych epitafiów. Dzięki temu klienci zyskują pełną kontrolę, transparentność kosztów oraz oszczędność czasu w bezpiecznym, cyfrowym środowisku.

## Użytkownicy i scenariusz
* **Główna grupa odbiorców:** Klienci indywidualni (organizatorzy pogrzebu) oraz administratorzy domu pogrzebowego.
* **Przykładowy scenariusz:** Klient wchodzi na stronę, wybiera wolny termin ceremonii pożegnalnej oraz pakiet usług (np. standardowy lub z przekształceniem prochowaym), dodaje cyfrowe epitafium z dostępem przez kod QR, a następnie zatwierdza rezerwację. System automatycznie blokuje termin w bazie danych, a użytkownik widzi podsumowanie na swoim koncie.

## Zakres funkcjonalny (v1 – MVP)
* **F01:** Użytkownik może przeglądać dostępne terminy ceremonii oraz harmonogram kaplic. *(MVP)*
* **F02:** Użytkownik może zarezerwować termin i wybrać podstawowy pakiet usług pogrzebowych. *(MVP)*
* **F03:** Użytkownik może zarządzać swoimi rezerwacjami i je anulować lub modyfikować przed terminem. *(MVP)*
* **F04:** Administrator może dodawać i edytować dostępne sale/kaplice oraz pakiety usług. *(Rozszerzenie v2)*
* **F05:** Generowanie unikalnego kodu QR dla cyfrowego epitafium powiązanego z rekordem zmarłego. *(Rozszerzenie v2)*

## Poza zakresem pierwszej wersji (v1)
1. Integracja z zewnętrznymi bramkami płatności online (płatności realizowane symulacyjnie).
2. Zaawansowany moduł powiadomień SMS / e-mail w czasie rzeczywistym.
## Uruchomienie aplikacji (Windows / PowerShell)

Aby uruchomić projekt lokalnie od zera, wykonaj poniższe kroki w terminalu (PowerShell) w głównym katalogu repozytorium:

1. **Utworzenie wirtualnego środowiska Python:**
   ```powershell
   python -m venv .venv
   ```

2. **Odblokowanie wykonywania skryptów w bieżącej sesji oraz aktywacja środowiska:**
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .venv\Scripts\activate
   ```

3. **Instalacja wymaganych bibliotek (Flask):**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Uruchomienie serwera aplikacji (automatycznie zainicjalizuje bazę SQLite przy pierwszym starcie):**
   ```powershell
   python app.py
   ```

Po uruchomieniu otwórz przeglądarkę i przejdź pod adres: `http://127.0.0.1:5000`.

## Organizacja współpracy
* **Podział zadań:** Podział na warstwę widoków/frontendu oraz logikę serwerową i bazodanową SQLite.
* **Komunikacja:** Bieżący kontakt przez LaboChat.com oraz platformy dedykowane.
* **Zasady commitowania:** Każda zmiana jest dokumentowana czytelnym commitem przez obie osoby w zespole.

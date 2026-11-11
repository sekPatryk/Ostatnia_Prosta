# Wybór technologii – Ostatnia Prosta v1

Do realizacji pierwszej wersji (v1) projektu „Ostatnia Prosta” wybraliśmy sprawdzony, lekki stos technologiczny, który umożliwia łatwe uruchomienie aplikacji lokalnie bez konieczności stosowania płatnych usług chmurowych.

* **Widoki (Frontend):** HTML5, CSS3, JavaScript – zapewniają prostą i responsywną strukturę formularzy oraz interfejs użytkownika zgodny ze szkicami.
* **Serwer (Backend):** Python 3 + Flask – lekki i elastyczny mikroframework idealny do obsługi żądań HTTP, routingu oraz walidacji reguł biznesowych po stronie serwera.
* **Baza danych:** SQLite (wbudowany moduł `sqlite3`) – bezserwerowa baza danych zapisująca stan w lokalnym pliku, co ułatwia testowanie i przenoszenie projektu między stacjami roboczymi członków zespołu.
* **Kontrola wersji:** Git oraz GitHub – narzędzia do śledzenia historii zmian oraz wspólnej pracy obu osób nad kodem źródłowym.


from database import get_db_connection


def pobierz_kaplice():
    """Pobiera aktywne kaplice."""

    connection = get_db_connection()

    try:
        return connection.execute("""
            SELECT *
            FROM sala
            WHERE aktywna = 1
            ORDER BY id_sali
        """).fetchall()

    finally:
        connection.close()


def pobierz_rezerwacje(data_rezerwacji, id_sali=None):
    """Pobiera aktywne rezerwacje dla wybranej daty."""

    connection = get_db_connection()

    try:
        if id_sali is not None:
            return connection.execute("""
                SELECT r.*, s.nazwa AS nazwa_sali
                FROM rezerwacja r
                JOIN sala s ON r.id_sali = s.id_sali
                WHERE r.data_rezerwacji = ?
                  AND r.id_sali = ?
                  AND r.status = 'aktywna'
                ORDER BY r.godzina_od
            """, (data_rezerwacji, id_sali)).fetchall()

        return connection.execute("""
            SELECT r.*, s.nazwa AS nazwa_sali
            FROM rezerwacja r
            JOIN sala s ON r.id_sali = s.id_sali
            WHERE r.data_rezerwacji = ?
              AND r.status = 'aktywna'
            ORDER BY r.godzina_od
        """, (data_rezerwacji,)).fetchall()

    finally:
        connection.close()


def sprawdz_dostepnosc(id_sali, data_rezerwacji,
                       godzina_od, godzina_do):
    """Sprawdza, czy wybrany termin jest wolny."""

    connection = get_db_connection()

    try:
        konflikt = connection.execute("""
            SELECT id_rezerwacji
            FROM rezerwacja
            WHERE id_sali = ?
              AND data_rezerwacji = ?
              AND status = 'aktywna'
              AND godzina_od < ?
              AND godzina_do > ?
            LIMIT 1
        """, (
            id_sali,
            data_rezerwacji,
            godzina_do,
            godzina_od
        )).fetchone()

        return konflikt is None

    finally:
        connection.close()


def dodaj_rezerwacje(id_uzytkownika, id_sali,
                     data_rezerwacji, godzina_od, godzina_do):
    """Dodaje rezerwację z kontrolą konfliktów czasowych."""

    connection = get_db_connection()

    try:
        # Blokada zapisu innych transakcji na czas operacji.
        connection.execute("BEGIN IMMEDIATE")

        uzytkownik = connection.execute("""
            SELECT id_uzytkownika
            FROM uzytkownik
            WHERE id_uzytkownika = ?
        """, (id_uzytkownika,)).fetchone()

        if not uzytkownik:
            return False, "Nie znaleziono użytkownika."

        sala = connection.execute("""
            SELECT id_sali
            FROM sala
            WHERE id_sali = ?
              AND aktywna = 1
        """, (id_sali,)).fetchone()

        if not sala:
            return False, "Wybrana kaplica nie istnieje lub jest nieaktywna."

        konflikt = connection.execute("""
            SELECT id_rezerwacji
            FROM rezerwacja
            WHERE id_sali = ?
              AND data_rezerwacji = ?
              AND status = 'aktywna'
              AND godzina_od < ?
              AND godzina_do > ?
            LIMIT 1
        """, (
            id_sali,
            data_rezerwacji,
            godzina_do,
            godzina_od
        )).fetchone()

        if konflikt:
            return False, "Wybrany termin jest już zarezerwowany."

        connection.execute("""
            INSERT INTO rezerwacja (
                id_uzytkownika,
                id_sali,
                data_rezerwacji,
                godzina_od,
                godzina_do,
                status
            )
            VALUES (?, ?, ?, ?, ?, 'aktywna')
        """, (
            id_uzytkownika,
            id_sali,
            data_rezerwacji,
            godzina_od,
            godzina_do
        ))

        connection.commit()

        return True, "Rezerwacja została zapisana."

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def moje_rezerwacje(id_uzytkownika):
    """Pobiera wszystkie rezerwacje użytkownika."""

    connection = get_db_connection()

    try:
        return connection.execute("""
            SELECT r.*, s.nazwa AS nazwa_sali
            FROM rezerwacja r
            JOIN sala s ON r.id_sali = s.id_sali
            WHERE r.id_uzytkownika = ?
            ORDER BY r.data_rezerwacji DESC, r.godzina_od DESC
        """, (id_uzytkownika,)).fetchall()

    finally:
        connection.close()


def anuluj_rezerwacje(id_rezerwacji, id_uzytkownika):
    """Anuluje aktywną rezerwację należącą do użytkownika."""

    connection = get_db_connection()

    try:
        wynik = connection.execute("""
            UPDATE rezerwacja
            SET status = 'anulowana'
            WHERE id_rezerwacji = ?
              AND id_uzytkownika = ?
              AND status = 'aktywna'
        """, (
            id_rezerwacji,
            id_uzytkownika
        ))

        connection.commit()

        if wynik.rowcount == 0:
            return False, "Nie znaleziono aktywnej rezerwacji."

        return True, "Rezerwacja została anulowana."

    finally:
        connection.close()

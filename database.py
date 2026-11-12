
import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE = os.path.join(
    BASE_DIR,
    "instance",
    "ostatnia_prosta.db"
)


def get_db_connection():
    """Tworzy połączenie z bazą SQLite."""

    os.makedirs(os.path.dirname(DATABASE), exist_ok=True)

    connection = sqlite3.connect(
        DATABASE,
        timeout=10
    )

    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")

    return connection


def init_db():
    """Tworzy tabele i dane demonstracyjne."""

    connection = get_db_connection()

    try:
        connection.executescript("""
            CREATE TABLE IF NOT EXISTS uzytkownik (
                id_uzytkownika INTEGER PRIMARY KEY AUTOINCREMENT,
                imie TEXT NOT NULL,
                nazwisko TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );

            CREATE TABLE IF NOT EXISTS sala (
                id_sali INTEGER PRIMARY KEY AUTOINCREMENT,
                nazwa TEXT NOT NULL,
                opis TEXT,
                pojemnosc INTEGER NOT NULL CHECK (pojemnosc > 0),
                aktywna INTEGER NOT NULL DEFAULT 1
                    CHECK (aktywna IN (0, 1))
            );

            CREATE TABLE IF NOT EXISTS rezerwacja (
                id_rezerwacji INTEGER PRIMARY KEY AUTOINCREMENT,

                id_uzytkownika INTEGER NOT NULL,
                id_sali INTEGER NOT NULL,

                data_rezerwacji TEXT NOT NULL,
                godzina_od TEXT NOT NULL,
                godzina_do TEXT NOT NULL,

                status TEXT NOT NULL DEFAULT 'aktywna'
                    CHECK (status IN ('aktywna', 'anulowana')),

                FOREIGN KEY (id_uzytkownika)
                    REFERENCES uzytkownik(id_uzytkownika),

                FOREIGN KEY (id_sali)
                    REFERENCES sala(id_sali),

                CHECK (godzina_od < godzina_do)
            );

            CREATE INDEX IF NOT EXISTS idx_rezerwacja_sala_data
            ON rezerwacja (
                id_sali,
                data_rezerwacji,
                status
            );

            CREATE INDEX IF NOT EXISTS idx_rezerwacja_uzytkownik
            ON rezerwacja (id_uzytkownika);
        """)

        connection.execute("""
            INSERT OR IGNORE INTO uzytkownik
            (id_uzytkownika, imie, nazwisko, email)
            VALUES (1, 'Jan', 'Kowalski', 'demo@example.com')
        """)

        connection.executemany("""
            INSERT OR IGNORE INTO sala
            (id_sali, nazwa, opis, pojemnosc)
            VALUES (?, ?, ?, ?)
        """, [
            (1, 'Kaplica Mała', 'Kameralna kaplica', 30),
            (2, 'Kaplica Główna', 'Duża kaplica ceremonii', 100),
            (3, 'Kaplica Zachodnia', 'Kaplica o średniej pojemności', 60)
        ])

        connection.commit()

    finally:
        connection.close()

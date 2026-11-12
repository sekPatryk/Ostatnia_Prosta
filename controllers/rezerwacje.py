
import re

from datetime import date, time

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from models.rezerwacja import (
    pobierz_kaplice,
    pobierz_rezerwacje,
    dodaj_rezerwacje,
    moje_rezerwacje,
    anuluj_rezerwacje
)


rezerwacje_bp = Blueprint(
    "rezerwacje",
    __name__,
    url_prefix="/rezerwacje"
)

# Użytkownik demonstracyjny.
DEMO_USER_ID = 1


def poprawna_data(data):
    """Sprawdza poprawność daty YYYY-MM-DD."""

    try:
        return date.fromisoformat(data).isoformat() == data
    except (ValueError, TypeError):
        return False


def poprawna_godzina(godzina):
    """Sprawdza poprawność godziny HH:MM."""

    if not isinstance(godzina, str):
        return False

    if not re.fullmatch(r"\d{2}:\d{2}", godzina):
        return False

    try:
        time.fromisoformat(godzina)
        return True
    except ValueError:
        return False


@rezerwacje_bp.route("/", methods=["GET"])
def lista_kaplic():
    """W01 – lista kaplic i sprawdzanie dostępności."""

    wybrana_data = request.args.get(
        "data",
        date.today().isoformat()
    )

    if not poprawna_data(wybrana_data):
        flash("Niepoprawny format daty.", "error")
        wybrana_data = date.today().isoformat()

    kaplice = pobierz_kaplice()
    rezerwacje = pobierz_rezerwacje(wybrana_data)

    return render_template(
        "rezerwacje/W01_lista_kaplic.html",
        kaplice=kaplice,
        rezerwacje=rezerwacje,
        wybrana_data=wybrana_data
    )


@rezerwacje_bp.route("/nowa", methods=["GET", "POST"])
def nowa_rezerwacja():
    """W02 – formularz dodawania nowej rezerwacji."""

    kaplice = pobierz_kaplice()

    dzisiaj = date.today().isoformat()

    if request.method == "POST":

        try:
            id_sali = int(request.form.get("id_sali", ""))
        except (ValueError, TypeError):
            id_sali = None

        data_rezerwacji = request.form.get(
            "data_rezerwacji",
            ""
        )

        godzina_od = request.form.get("godzina_od", "")
        godzina_do = request.form.get("godzina_do", "")

        dane_formularza = {
            "id_sali": id_sali,
            "data_rezerwacji": data_rezerwacji,
            "godzina_od": godzina_od,
            "godzina_do": godzina_do
        }

        if id_sali is None:
            flash("Wybierz poprawną kaplicę.")

        elif not poprawna_data(data_rezerwacji):
            flash("Podano niepoprawną datę.")

        elif data_rezerwacji < dzisiaj:
            flash("Nie można rezerwować terminów w przeszłości.")

        elif not poprawna_godzina(godzina_od):
            flash("Podano niepoprawną godzinę rozpoczęcia.")

        elif not poprawna_godzina(godzina_do):
            flash("Podano niepoprawną godzinę zakończenia.")

        elif godzina_od >= godzina_do:
            flash(
                "Godzina zakończenia musi być późniejsza "
                "od godziny rozpoczęcia."
            )

        else:
            sukces, komunikat = dodaj_rezerwacje(
                DEMO_USER_ID,
                id_sali,
                data_rezerwacji,
                godzina_od,
                godzina_do
            )

            if sukces:
                flash(komunikat, "success")

                return redirect(
                    url_for("rezerwacje.moje_rezerwacje_widok")
                )

            flash(komunikat, "error")

        return render_template(
            "rezerwacje/W02_formularz_rezerwacji.html",
            kaplice=kaplice,
            today=dzisiaj,
            dane=dane_formularza
        )

    # GET – domyślne dane formularza.
    dane_formularza = {
        "id_sali": request.args.get("id_sali", ""),
        "data_rezerwacji": request.args.get("data", dzisiaj),
        "godzina_od": "",
        "godzina_do": ""
    }

    return render_template(
        "rezerwacje/W02_formularz_rezerwacji.html",
        kaplice=kaplice,
        today=dzisiaj,
        dane=dane_formularza
    )


@rezerwacje_bp.route("/moje", methods=["GET"])
def moje_rezerwacje_widok():
    """W03 – panel rezerwacji użytkownika demonstracyjnego."""

    rezerwacje = moje_rezerwacje(DEMO_USER_ID)

    return render_template(
        "rezerwacje/W03_moje_rezerwacje.html",
        rezerwacje=rezerwacje
    )


@rezerwacje_bp.route(
    "/anuluj/<int:id_rezerwacji>",
    methods=["POST"]
)
def anuluj(id_rezerwacji):
    """F03 – anulowanie własnej rezerwacji."""

    sukces, komunikat = anuluj_rezerwacje(
        id_rezerwacji,
        DEMO_USER_ID
    )

    if sukces:
        flash(komunikat, "success")
    else:
        flash(komunikat, "error")

    return redirect(
        url_for("rezerwacje.moje_rezerwacje_widok")
    )

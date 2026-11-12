
import os

from flask import Flask, redirect, url_for
from flask_wtf.csrf import CSRFProtect

from database import init_db
from controllers.rezerwacje import rezerwacje_bp


app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY",
    "dev-only-change-this-secret-key"
)

# Ochrona formularzy POST przed CSRF.
csrf = CSRFProtect(app)

# Rejestracja kontrolera.
app.register_blueprint(rezerwacje_bp)


@app.route("/")
def index():
    """Przekierowanie na listę kaplic."""

    return redirect(
        url_for("rezerwacje.lista_kaplic")
    )


# Inicjalizacja bazy danych.
init_db()


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )

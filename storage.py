"""SQLite üzerinden kalite kontrol hata kayıtlarının yönetimi."""
import sqlite3
from datetime import datetime
from pathlib import Path

DEFAULT_DATABASE = Path(__file__).resolve().parent / "data" / "quality.db"
ERROR_TYPES = ("Çizik", "Ölçü hatası", "Renk hatası", "Montaj hatası", "Diğer")


def connect(db_path=DEFAULT_DATABASE):
    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database(db_path=DEFAULT_DATABASE):
    with connect(db_path) as connection:
        connection.execute(
            """CREATE TABLE IF NOT EXISTS defects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                error_type TEXT NOT NULL,
                description TEXT NOT NULL,
                quantity INTEGER NOT NULL CHECK (quantity >= 1),
                created_at TEXT NOT NULL
            )"""
        )


def create_defect(product_name, error_type, description, quantity, db_path=DEFAULT_DATABASE):
    product_name = product_name.strip()
    description = description.strip()
    if not product_name:
        raise ValueError("Ürün adı boş olamaz.")
    if error_type not in ERROR_TYPES:
        raise ValueError("Geçerli bir hata türü seçilmelidir.")
    if not description:
        raise ValueError("Açıklama boş olamaz.")
    if type(quantity) is not int or quantity < 1:
        raise ValueError("Hata adedi en az 1 olmalıdır.")

    initialize_database(db_path)
    with connect(db_path) as connection:
        cursor = connection.execute(
            """INSERT INTO defects (product_name, error_type, description, quantity, created_at)
               VALUES (?, ?, ?, ?, ?)""",
            (product_name, error_type, description, quantity,
             datetime.now().astimezone().isoformat(timespec="seconds")),
        )
        return cursor.lastrowid


def list_defects(db_path=DEFAULT_DATABASE):
    initialize_database(db_path)
    with connect(db_path) as connection:
        rows = connection.execute(
            """SELECT id, product_name, error_type, description, quantity, created_at
               FROM defects ORDER BY id DESC"""
        ).fetchall()
    return [dict(row) for row in rows]

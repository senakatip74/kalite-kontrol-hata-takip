"""Hata türlerine göre veritabanı tabanlı analiz."""
from storage import connect, initialize_database, DEFAULT_DATABASE


def summarize_defects(db_path=DEFAULT_DATABASE):
    """Her tür için kayıt sayısı ve toplam hata adedini getir."""
    initialize_database(db_path)
    with connect(db_path) as connection:
        rows = connection.execute(
            """SELECT error_type, COUNT(*) AS record_count,
                      SUM(quantity) AS total_quantity
               FROM defects
               GROUP BY error_type
               ORDER BY total_quantity DESC, error_type ASC"""
        ).fetchall()
    return [dict(row) for row in rows]

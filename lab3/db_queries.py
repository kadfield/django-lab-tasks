from django.db import connection, transaction


def run_sql_and_transaction_demo():
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS lab3_students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                balance INTEGER NOT NULL DEFAULT 0,
                group_code TEXT NOT NULL
            )
        """)
        cursor.execute(
            "INSERT INTO lab3_students (full_name, balance, group_code) VALUES (%s, %s, %s)",
            ["Əli Məmmədov", 100, "IT-201"]
        )
        cursor.execute("SELECT id, full_name, balance, group_code FROM lab3_students")
        rows = cursor.fetchall()

    try:
        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE lab3_students SET balance = balance - %s WHERE full_name = %s",
                    [30, "Əli Məmmədov"]
                )
                cursor.execute(
                    "UPDATE lab3_students SET group_code = %s WHERE full_name = %s",
                    ["IT-202", "Əli Məmmədov"]
                )
                raise RuntimeError("Tranzaksiya zamanı xəta baş verdi, əməliyyat geri qaytarılır.")
    except RuntimeError as exc:
        rollback_status = str(exc)

    connection.close()
    is_closed = connection.connection is None

    return {
        "rows": rows,
        "rollback_status": rollback_status,
        "connection_closed": is_closed,
    }

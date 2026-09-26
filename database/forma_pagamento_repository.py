from psycopg.rows import dict_row

from database.connection import get_connection


class FormaPagamentoRepository:

    def buscar_todas(self):

        with get_connection() as connection:

            with connection.cursor(
                row_factory=dict_row
            ) as cursor:

                cursor.execute("""
                    SELECT
                        id,
                        nome
                    FROM forma_pagamento
                    ORDER BY nome
                """)

                return cursor.fetchall()
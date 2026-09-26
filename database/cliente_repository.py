from psycopg.rows import dict_row
from database.connection import get_connection


class ClienteRepository:

    def buscar_todos(self):

        with get_connection() as connection:

            with connection.cursor(row_factory=dict_row) as cursor:

                cursor.execute("""
                    SELECT
                        id,
                        nome,
                        cpf,
                        telefone,
                        email
                    FROM cliente
                    ORDER BY nome
                """)

                return cursor.fetchall()
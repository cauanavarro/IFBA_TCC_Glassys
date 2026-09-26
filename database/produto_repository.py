from psycopg.rows import dict_row
from database.connection import get_connection


class ProdutoRepository:

    def buscar_todos(self):

        with get_connection() as connection:

            with connection.cursor(row_factory=dict_row) as cursor:

                cursor.execute("""
                    SELECT
                        p.id,
                        p.nome,
                        p.sku,
                        p.descricao,
                        p.estoque,
                        p.valor_unitario,
                        p.categoria_id,
                        c.nome AS categoria
                    FROM produto AS p
                    INNER JOIN categoria_produto AS c 
                        ON p.categoria_id = c.id
                    ORDER BY p.nome
                """)

                return cursor.fetchall()
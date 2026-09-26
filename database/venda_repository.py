from database.connection import get_connection


class VendaRepository:

    def finalizar(
        self,
        venda,
        funcionario_id,
        forma_pagamento_id
    ):

        if venda.cliente is None:
            raise ValueError(
                "Nenhum cliente selecionado."
            )

        if not venda.itens:
            raise ValueError(
                "A venda não possui produtos."
            )

        with get_connection() as connection:

            with connection.cursor() as cursor:

                cursor.execute("""
                    INSERT INTO venda (
                        valor_total,
                        desconto,
                        cliente_id,
                        funcionario_id,
                        forma_pagamento_id
                    )
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING id
                """, (
                    venda.total,
                    venda.desconto,
                    venda.cliente["id"],
                    funcionario_id,
                    forma_pagamento_id
                ))

                venda_id = cursor.fetchone()[0]

                for item in venda.itens:

                    cursor.execute("""
                        UPDATE produto
                        SET estoque = estoque - %s
                        WHERE id = %s
                          AND estoque >= %s
                    """, (
                        item.quantidade,
                        item.produto["id"],
                        item.quantidade
                    ))

                    if cursor.rowcount != 1:
                        raise ValueError(
                            f'Estoque insuficiente para '
                            f'{item.produto["nome"]}.'
                        )

                    cursor.execute("""
                        INSERT INTO produto_vendido (
                            quantidade,
                            valor_unitario,
                            produto_id,
                            venda_id
                        )
                        VALUES (%s, %s, %s, %s)
                    """, (
                        item.quantidade,
                        item.produto["valor_unitario"],
                        item.produto["id"],
                        venda_id
                    ))

                return venda_id
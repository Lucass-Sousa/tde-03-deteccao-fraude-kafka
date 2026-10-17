import psycopg


def conectar():
    conn = psycopg.connect("postgresql://tde:tde@localhost:5432/fraudes")
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS transacoes (
                id TEXT PRIMARY KEY,
                cliente_id TEXT NOT NULL,
                amount NUMERIC(12, 2) NOT NULL,
                cidade TEXT NOT NULL,
                timestamp TIMESTAMPTZ NOT NULL
            )
            """
        )
        cur.execute(
            "ALTER TABLE transacoes ADD COLUMN IF NOT EXISTS fraudes TEXT"
        )
    return conn


def salvar(conn, transacao, fraudes):
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO transacoes (id, cliente_id, amount, cidade, timestamp, fraudes)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
            """,
            (
                transacao["id"],
                transacao["cliente_id"],
                transacao["amount"],
                transacao["cidade"],
                transacao["timestamp"],
                ", ".join(fraudes) if fraudes else None,
            ),
        )

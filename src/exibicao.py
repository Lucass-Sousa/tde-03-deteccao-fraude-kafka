MOTIVOS = {
    "ALTO_VALOR": "valor maior ou igual a 10000",
    "TEMPO_60s": "4 transações deste cliente em menos de 60 segundos",
    "GEO_10m": "este cliente em outra cidade nos últimos 10 minutos",
}


def exibir(transacao, alertas=None, titulo=None):
    alertas = alertas or []
    cliente = transacao["cliente_id"]
    quando = transacao["timestamp"].replace("T", " ").replace("+00:00", " UTC")
    if titulo is None:
        titulo = f"{cliente}  ·  fraude" if alertas else f"{cliente}  ·  transação"
    else:
        titulo = f"{titulo}  ·  {cliente}"

    linhas = [
        titulo,
        f"  id:     {transacao['id']}",
        f"  valor:  {transacao['amount']:.2f}",
        f"  cidade: {transacao['cidade']}",
        f"  quando: {quando}",
    ]
    for alerta in alertas:
        linhas.append(f"  {alerta}: {MOTIVOS[alerta]}")
    print("\n".join(linhas) + "\n", flush=True)

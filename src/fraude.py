from datetime import datetime, timedelta

HISTORICO = {}
JANELA_TEMPO = timedelta(seconds=60)
JANELA_GEO = timedelta(minutes=10)


def avaliar(transacao):
    quando = datetime.fromisoformat(transacao["timestamp"])
    cliente = transacao["cliente_id"]
    recentes = [
        item
        for item in HISTORICO.get(cliente, [])
        if quando - item["timestamp"] <= JANELA_GEO
    ]

    alertas = []
    if transacao["amount"] >= 10000:
        alertas.append("ALTO_VALOR")
    na_janela = [item for item in recentes if quando - item["timestamp"] < JANELA_TEMPO]
    if len(na_janela) + 1 >= 4:
        alertas.append("TEMPO_60s")
    if any(item["cidade"] != transacao["cidade"] for item in recentes):
        alertas.append("GEO_10m")

    recentes.append({"timestamp": quando, "cidade": transacao["cidade"]})
    HISTORICO[cliente] = recentes
    return alertas

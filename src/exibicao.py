def exibir(transacao, titulo):
    quando = transacao["timestamp"].replace("T", " ").replace("+00:00", " UTC")
    print(
        f"{titulo}\n"
        f"  id:      {transacao['id']}\n"
        f"  cliente: {transacao['cliente_id']}\n"
        f"  valor:   {transacao['amount']:.2f}\n"
        f"  cidade:  {transacao['cidade']}\n"
        f"  quando:  {quando}\n",
        flush=True,
    )

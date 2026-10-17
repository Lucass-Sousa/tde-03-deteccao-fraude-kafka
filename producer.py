import json
import random
import time
from datetime import datetime, timezone
from uuid import uuid4

from confluent_kafka import Producer

CIDADES = [
    "Curitiba",
    "São Paulo",
    "Rio de Janeiro",
    "Belo Horizonte",
    "Porto Alegre",
]

CLIENTES = ["cli-17", "cli-22", "cli-8", "cli-31"]


def nova_transacao():
    return {
        "id": f"tx-{uuid4().hex[:8]}",
        "cliente_id": random.choice(CLIENTES),
        "amount": round(random.uniform(20, 15000), 2),
        "cidade": random.choice(CIDADES),
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }


def main():
    producer = Producer({"bootstrap.servers": "localhost:9092"})
    try:
        while True:
            transacao = nova_transacao()
            producer.produce(
                "transacoes",
                value=json.dumps(transacao).encode("utf-8"),
            )
            producer.flush()
            print("Publicado em transacoes:", transacao, flush=True)
            time.sleep(3)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()

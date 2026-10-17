import json

from confluent_kafka import Producer

TRANSACAO = {
    "id": "tx-1001",
    "cliente_id": "cli-17",
    "amount": 250.0,
    "cidade": "Curitiba",
    "timestamp": "2026-10-17T11:00:00",
}


def main():
    producer = Producer({"bootstrap.servers": "localhost:9092"})
    producer.produce("transacoes", value=json.dumps(TRANSACAO).encode("utf-8"))
    producer.flush()
    print("Publicado em transacoes:", TRANSACAO)


if __name__ == "__main__":
    main()

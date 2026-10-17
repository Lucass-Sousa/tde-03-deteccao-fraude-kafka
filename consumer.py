import json

from confluent_kafka import Consumer

from db import conectar, salvar


def main():
    banco = conectar()
    consumer = Consumer(
        {
            "bootstrap.servers": "localhost:9092",
            "group.id": "fraude",
            "auto.offset.reset": "earliest",
        }
    )
    consumer.subscribe(["transacoes"])

    try:
        while True:
            mensagem = consumer.poll(1.0)
            if mensagem is None:
                continue
            if mensagem.error():
                print("Erro ao ler:", mensagem.error())
                continue
            transacao = json.loads(mensagem.value().decode("utf-8"))
            salvar(banco, transacao)
            print("Transação:", transacao, flush=True)
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
        banco.close()


if __name__ == "__main__":
    main()

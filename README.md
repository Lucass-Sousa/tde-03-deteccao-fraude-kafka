# TDE 03 — Detecção de fraude com Apache Kafka

Cenário: um produtor publica transações simuladas e um consumidor detecta fraude, grava tudo no PostgreSQL e mostra alertas no console.

## Subir Kafka e PostgreSQL

Requisito: Docker com o plugin Compose.

```bash
docker compose up -d
docker compose ps
```

- Kafka escuta em `localhost:9092`
- PostgreSQL escuta em `localhost:5432` (banco `fraudes`, usuário `tde`, senha `tde`)

Para encerrar:

```bash
docker compose down
```

## Publicar transações

Com o Kafka no ar e as dependências instaladas (`python -m venv .venv && .venv/bin/pip install -r requirements.txt`):

```bash
.venv/bin/python producer.py
```

A cada 3 segundos o produtor sorteia uma transação e publica no tópico `transacoes`. Para parar, use Ctrl+C.

## Ler e gravar as transações

Em outro terminal:

```bash
.venv/bin/python consumer.py
```

Cada mensagem aparece no console e é inserida na tabela `transacoes` do banco `fraudes`. Para parar, use Ctrl+C.

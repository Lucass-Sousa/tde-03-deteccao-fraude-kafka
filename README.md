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
.venv/bin/python src/producer.py
```

A cada 3 segundos o produtor sorteia uma transação e publica no tópico `transacoes`. Para parar, use Ctrl+C.

## Ler e gravar as transações

Em outro terminal:

```bash
.venv/bin/python src/consumer.py
```

Cada mensagem é inserida na tabela `transacoes` do banco `fraudes`. Para parar, use Ctrl+C.

No console do consumidor, uma transação normal começa com `Transação`. Se alguma regra disparar, a primeira linha é `Fraude:` seguida do nome da regra. A mesma marca fica na coluna `fraudes`.

- `ALTO_VALOR`: valor maior ou igual a 10000
- `TEMPO_60s`: o mesmo cliente com 4 transações em menos de 60 segundos
- `GEO_10m`: o mesmo cliente em duas cidades diferentes dentro de 10 minutos

Para apresentar, suba o consumidor primeiro e o produtor depois. Em cerca de um minuto aparecem os três alertas, porque são poucos clientes e uma mensagem a cada 3 segundos.

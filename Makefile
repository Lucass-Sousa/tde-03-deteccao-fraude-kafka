.PHONY: up down producer consumer

up:
	docker compose up -d
	docker compose ps

down:
	docker compose down

producer:
	.venv/bin/python src/producer.py

consumer:
	.venv/bin/python src/consumer.py

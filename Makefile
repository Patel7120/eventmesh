.PHONY: up down logs shell

up:
	docker compose up --build

down:
	docker compose down

logs:
	docker compose logs -f

shell:
	docker compose exec api bash

dev:
	uvicorn src.main:app --reload
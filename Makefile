test:
	cd services && cd tasks_api && poetry run pytest tests.py

quality:
	cd services && cd tasks_api && poetry run flake8 . && poetry run black . && poetry run isort . --profile black

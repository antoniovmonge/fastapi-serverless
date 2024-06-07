test:
	cd services && cd tasks_api && poetry run pytest tests.py

black:
	cd services && cd tasks_api && poetry run black .

isort:
	cd services && cd tasks_api && poetry run isort . --profile black

flake8:
	cd services && cd tasks_api && poetry run flake8 .

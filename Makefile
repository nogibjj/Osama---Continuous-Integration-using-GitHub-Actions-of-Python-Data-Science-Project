install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main src/test_*.py
	python -m pytest --nbval src/*.ipynb

format:	
	black src/*.py
	nbqa black src/*.ipynb

lint:
	nbqa ruff src/*.ipynb
	ruff check src/*.py
deploy:
	python aircraft_analytics.py
		
all: install lint format test 

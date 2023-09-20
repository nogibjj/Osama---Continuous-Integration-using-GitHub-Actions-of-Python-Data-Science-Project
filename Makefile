install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main test_*.py
	python -m pytest --nbval src/*.ipynb

format:	
	black *.py
	nbqa black *.ipynb

lint:
	nbqa ruff *.ipynb
	ruff check *.py
deploy:
	python aircraft_analytics.py
		
all: install lint format test 

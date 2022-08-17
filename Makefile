ci:
	black egzopix/
	mypy egzopix/

test:
	python -m unittest

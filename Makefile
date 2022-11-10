test:
	pytest --cov=src tests/
	rm assets/coverage.svg
	coverage-badge -o assets/coverage.svg
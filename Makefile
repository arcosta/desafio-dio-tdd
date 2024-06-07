run:
	@uvicorn tdd_project.store.main:app --reload

precommit-install:
	@poetry run pre-commit install

test:
	@poetry run pytest

test-matching:
	@poetry run pytest -s -rx -k $(K) --pdb tdd_project ./tdd_project/tests/

# md com os comandos do arquivo **MakeFile**, logo que os comando "make" não existe no windows

## run
	uvicorn store.main:app --reload

## pre-commit
	poetry run pre-commit install

## test
	poetry run pytest

## test-matching
	poetry run pytest -s -rx -k $(K) --pdb store ./tests/
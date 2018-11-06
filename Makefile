all: test

test:
	bash test.sh

document:
	python setup.py install
	sphinx-build -b html docs/source/ docs/build

spelling:
	sphinx-build -b spelling docs/source/ docs/build/spelling

uml:
	plantuml -tsvg -o ../_static/images/ docs/source/uml/*.uml

format:
	isort -y $(find lml -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
	black -l 79 lml
	black -l 79 tests
	black -l 79 examples

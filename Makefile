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

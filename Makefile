all: test

test:
	bash test.sh

document:
	sphinx-build -b html docs/source/ docs/build

spelling:
	sphinx-build -b spelling docs/source/ docs/build/spelling


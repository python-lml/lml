all: test

test:
	bash test.sh

document:
	bash document.sh

spelling:
	sphinx-build -b spelling docs/source/ docs/build/spelling


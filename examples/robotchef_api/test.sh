pip freeze
nosetests --with-cov --cover-package robotchef_api --cover-package tests --with-doctest --doctest-extension=.rst README.rst tests docs/source robotchef_api && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long

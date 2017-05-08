pip freeze
nosetests --with-cov --cover-package robotchef_britishcuisine --cover-package tests --with-doctest --doctest-extension=.rst README.rst tests docs/source robotchef_britishcuisine && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long

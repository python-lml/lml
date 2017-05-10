pip freeze
nosetests --with-cov --cover-package robotchef_v2_cli --cover-package tests --with-doctest --doctest-extension=.rst README.rst tests docs/source robotchef_v2_cli && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long

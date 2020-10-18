pip freeze
pytest tests --cov=robotchef_cli --doctest-glob=*.rst && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long

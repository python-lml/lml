import sys

from mock import patch
from nose.tools import eq_

PY2 = sys.version_info[0] == 2

if PY2:
    from StringIO import StringIO
else:
    from io import StringIO


@patch("sys.stdout", new_callable=StringIO)
def test_peking_duck(stdout):
    arguments = ["robotchef", "Jacket Potato"]
    from robotchef_v2.main import main

    with patch.object(sys, "argv", arguments):
        main()
        eq_(stdout.getvalue(), "I can bake Jacket Potato\n")

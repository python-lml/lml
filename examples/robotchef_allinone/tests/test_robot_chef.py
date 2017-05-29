import sys
from mock import patch
from nose.tools import eq_
from io import StringIO


@patch('sys.stdout', new_callable=StringIO)
def test_peking_duck(stdout):
    arguments = ['robotchef', 'Cornish Scone']
    from robotchef_allinone.main import main
    with patch.object(sys, 'argv', arguments):
        main()
        eq_(stdout.getvalue(), 'I can bake Cornish Scone\n')

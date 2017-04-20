from mock import patch
from nose.tools import eq_

MARKER = '__test_plugins__'


@patch('pkgutil.get_importer')
def test_load_from_pyinstaller(pkgutil_get_importer):
    sample_toc = set(['pyexcel_io', 'pyexcel_xls', 'blah'])
    pkgutil_get_importer.return_value.toc = sample_toc
    from lml.plugin import scan_from_pyinstaller
    module_names = scan_from_pyinstaller('pyexcel_', 'path')
    expected = ['pyexcel_io', 'pyexcel_xls']
    eq_(sorted(list(module_names)), sorted(expected))


@patch('pkgutil.get_importer')
@patch('pkgutil.iter_modules')
@patch('lml.plugin.load_me_later')
def test_load_plugins(pre_register,
                      pkgutil_iter_modules,
                      pkgutil_get_importer):
    sample_toc = set(['pyexcel_io'])
    pkgutil_get_importer.return_value.toc = sample_toc
    pkgutil_iter_modules.return_value = [('not used', 'pyexcel_test', True)]
    from lml.plugin import scan_plugins
    scan_plugins('pyexcel_', MARKER, '.', ['pyexcel_io'])
    (info, module_name), _ = pre_register.call_args
    eq_(info.plugin_type, 'test_io')
    eq_(info.submodule, 'x')


@patch('pkgutil.get_importer')
@patch('pkgutil.iter_modules')
@patch('lml.plugin.load_me_later')
def test_load_plugins_without_pyinstaller(pre_register,
                                          pkgutil_iter_modules,
                                          pkgutil_get_importer):
    test_module_name = 'pyexcel_test'
    sample_toc = set()
    pkgutil_get_importer.return_value.toc = sample_toc
    # mock iter modules
    pkgutil_iter_modules.return_value = [('not used', test_module_name, True)]
    from lml.plugin import scan_plugins
    scan_plugins('pyexcel_', MARKER, '.', ['pyexcel_io'])
    (info, module_name), _ = pre_register.call_args
    eq_(module_name, test_module_name)
    eq_(info.plugin_type, 'test_io')
    eq_(info.submodule, 'x')


@patch('pkgutil.get_importer')
@patch('pkgutil.iter_modules')
@patch('lml.plugin.load_me_later')
def test_load_plugins_without_any_plugins(pre_register,
                                          pkgutil_iter_modules,
                                          pkgutil_get_importer):
    sample_toc = set()
    pkgutil_get_importer.return_value.toc = sample_toc
    pkgutil_iter_modules.return_value = []
    from lml.plugin import scan_plugins
    scan_plugins('pyexcel_', MARKER, '.', ['pyexcel_io'])
    assert pre_register.called is False


@patch('pkgutil.get_importer')
@patch('pkgutil.iter_modules')
@patch('lml.plugin.load_me_later')
def test_load_plugins_import_error(pre_register,
                                   pkgutil_iter_modules,
                                   pkgutil_get_importer):
    sample_toc = set(['test_non_existent_module'])
    pkgutil_get_importer.return_value.toc = sample_toc
    pkgutil_iter_modules.return_value = [('not used', 'pyexcel_xls', False)]
    from lml.plugin import scan_plugins
    scan_plugins('test_', MARKER,  '.', ['pyexcel_io'])
    assert pre_register.called is False

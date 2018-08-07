from mock import patch
from nose.tools import eq_


@patch("pkgutil.get_importer")
def test_load_from_pyinstaller(pkgutil_get_importer):
    sample_toc = set(["pyexcel_io", "pyexcel_xls", "blah", "test.dot.module"])
    pkgutil_get_importer.return_value.toc = sample_toc
    from lml.loader import scan_from_pyinstaller

    module_names = scan_from_pyinstaller("pyexcel_", "path")
    expected = ["pyexcel_io", "pyexcel_xls"]
    eq_(sorted(list(module_names)), sorted(expected))


@patch("pkgutil.get_importer")
def test_load_from_pyinstaller_with_regex(pkgutil_get_importer):
    sample_toc = set(["pyexcel_io", "pyexcel_xls", "blah"])
    pkgutil_get_importer.return_value.toc = sample_toc
    from lml.loader import scan_from_pyinstaller

    module_names = scan_from_pyinstaller("^.+cel_.+$", "path")
    expected = ["pyexcel_io", "pyexcel_xls"]
    eq_(sorted(list(module_names)), sorted(expected))


@patch("pkgutil.get_importer")
@patch("pkgutil.iter_modules")
def test_load_plugins(pkgutil_iter_modules, pkgutil_get_importer):
    test_module_name = "pyexcel_test"
    sample_toc = set(["pyexcel_io"])
    pkgutil_get_importer.return_value.toc = sample_toc
    pkgutil_iter_modules.return_value = [("not used", test_module_name, True)]
    from lml.loader import scan_plugins

    scan_plugins("pyexcel_", ".", ["pyexcel_io"])
    from lml.plugin import CACHED_PLUGIN_INFO

    info = CACHED_PLUGIN_INFO["test_io"][0]
    eq_(info.plugin_type, "test_io")
    eq_(info.absolute_import_path, "pyexcel_test.x")


@patch("pkgutil.get_importer")
@patch("pkgutil.iter_modules")
def test_load_plugins_without_pyinstaller(
    pkgutil_iter_modules, pkgutil_get_importer
):
    test_module_name = "pyexcel_test"
    sample_toc = set()
    pkgutil_get_importer.return_value.toc = sample_toc
    # mock iter modules
    pkgutil_iter_modules.return_value = [("not used", test_module_name, True)]
    from lml.loader import scan_plugins

    scan_plugins("pyexcel_", ".", ["pyexcel_io"])
    from lml.plugin import CACHED_PLUGIN_INFO

    info = CACHED_PLUGIN_INFO["test_io"][0]
    eq_(info.plugin_type, "test_io")
    eq_(info.absolute_import_path, "pyexcel_test.x")


@patch("pkgutil.get_importer")
@patch("pkgutil.iter_modules")
@patch("lml.plugin._load_me_later")
def test_load_plugins_without_any_plugins(
    mocked_load_me_later, pkgutil_iter_modules, pkgutil_get_importer
):
    sample_toc = set()
    pkgutil_get_importer.return_value.toc = sample_toc
    pkgutil_iter_modules.return_value = []
    from lml.loader import scan_plugins

    scan_plugins("pyexcel_", ".", ["pyexcel_io"])
    assert mocked_load_me_later.called is False


@patch("pkgutil.get_importer")
@patch("pkgutil.iter_modules")
@patch("lml.plugin._load_me_later")
def test_load_plugins_without_black_list(
    mocked_load_me_later, pkgutil_iter_modules, pkgutil_get_importer
):
    sample_toc = set()
    pkgutil_get_importer.return_value.toc = sample_toc
    pkgutil_iter_modules.return_value = []
    from lml.loader import scan_plugins

    scan_plugins("pyexcel_", ".")
    assert mocked_load_me_later.called is False


@patch("pkgutil.get_importer")
@patch("pkgutil.iter_modules")
@patch("lml.plugin._load_me_later")
def test_load_plugins_import_error(
    mocked_load_me_later, pkgutil_iter_modules, pkgutil_get_importer
):
    sample_toc = set(["test_non_existent_module"])
    pkgutil_get_importer.return_value.toc = sample_toc
    pkgutil_iter_modules.return_value = [("not used", "pyexcel_xls", False)]
    from lml.loader import scan_plugins

    scan_plugins("test_", ".", ["pyexcel_io"])
    assert mocked_load_me_later.called is False

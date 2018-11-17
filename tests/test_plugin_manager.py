from mock import patch
from lml.plugin import (
    PLUG_IN_MANAGERS,
    CACHED_PLUGIN_INFO,
    PluginInfo,
    PluginManager,
    _show_me_your_name,
)
from nose.tools import eq_, raises


def test_plugin_manager():
    test_plugin = "my plugin"
    manager = PluginManager(test_plugin)
    assert PLUG_IN_MANAGERS[test_plugin] == manager


def test_load_me_later():
    test_plugin = "my plugin"
    manager = PluginManager(test_plugin)
    plugin_info = make_me_a_plugin_info(test_plugin)
    manager.load_me_later(plugin_info)
    assert list(manager.registry.keys()) == [test_plugin]


@patch("lml.plugin.do_import_class")
def test_load_me_now(mock_import):
    custom_class = PluginInfo
    mock_import.return_value = custom_class
    test_plugin = "my plugin"
    manager = PluginManager(test_plugin)
    plugin_info = make_me_a_plugin_info(test_plugin)
    manager.load_me_later(plugin_info)
    actual = manager.load_me_now(test_plugin)
    eq_(actual, custom_class)
    eq_(manager.tag_groups, {"my plugin": "my plugin"})
    eq_(plugin_info, manager.registry["my plugin"][0])


@raises(Exception)
@patch("lml.plugin.do_import_class")
def test_load_me_now_exception(mock_import):
    custom_class = PluginInfo
    mock_import.return_value = custom_class
    test_plugin = "my plugin"
    manager = PluginManager(test_plugin)
    plugin_info = make_me_a_plugin_info("my")
    manager.load_me_later(plugin_info)
    manager.load_me_now("my", "my special library")


@raises(Exception)
def test_load_me_now_no_key_found():
    test_plugin = "my plugin"
    manager = PluginManager(test_plugin)
    manager.load_me_now("my", custom_property="here")


@patch("lml.plugin.do_import_class")
def test_dynamic_load_library(mock_import):
    test_plugin = "test plugin"
    custom_obj = object()
    mock_import.return_value = custom_obj
    manager = PluginManager(test_plugin)
    plugin_info = make_me_a_plugin_info(test_plugin)
    manager.dynamic_load_library(plugin_info)
    eq_(custom_obj, plugin_info.cls)


@patch("lml.plugin.do_import_class")
def test_dynamic_load_library_no_action(mock_import):
    test_plugin = "test plugin"
    manager = PluginManager(test_plugin)
    plugin_info = make_me_a_plugin_info(test_plugin)
    plugin_info.cls = object()
    manager.dynamic_load_library(plugin_info)
    assert mock_import.called is False


class TestClass:
    pass


def test_register_a_plugin():
    test_plugin = "test plugin"

    manager = PluginManager(test_plugin)
    plugin_info = make_me_a_plugin_info("my")
    manager.register_a_plugin(TestClass, plugin_info)
    eq_(plugin_info.cls, TestClass)
    eq_(manager.registry["my"][0], plugin_info)
    eq_(manager.tag_groups, {"my": "my"})


def test_get_a_plugin():
    test_plugin = "test plugin"

    manager = PluginManager(test_plugin)
    plugin_info = make_me_a_plugin_info("my")
    plugin_info.cls = TestClass
    manager.register_a_plugin(TestClass, plugin_info)
    the_plugin = manager.get_a_plugin("my")
    assert isinstance(the_plugin, TestClass)


def test_register_class():
    test_plugin = "test_plugin"
    plugin_info = make_me_a_plugin_info("my")
    CACHED_PLUGIN_INFO[test_plugin].append(plugin_info)
    manager = PluginManager(test_plugin)
    assert list(manager.registry.keys()) == ["my"]


def test_load_me_later_function():
    from lml.plugin import _load_me_later

    test_plugin = "my plugin"
    manager = PluginManager(test_plugin)
    plugin_info = make_me_a_plugin_info(test_plugin)
    _load_me_later(plugin_info)
    assert list(manager.registry.keys()) == [test_plugin]


@raises(ImportError)
def test_do_import_cls_error():
    from lml.plugin import do_import_class

    do_import_class("non.exist.class")


def test_register_a_plugin_function_1():
    PluginManager("test plugin")

    @PluginInfo("test plugin", tags=["akey"])
    class MyPlugin(object):
        pass

    MyPlugin()


def test_register_a_plugin_function_2():
    non_existent_plugin = "I have no plugin manager"

    @PluginInfo(non_existent_plugin, tags=["akey"])
    class MyPlugin(object):
        pass

    MyPlugin()
    assert non_existent_plugin in CACHED_PLUGIN_INFO


def test_primary_key():
    manager = PluginManager("test plugin2")

    @PluginInfo("test plugin2", tags=["primary key", "key 1", "key 2"])
    class MyPlugin(object):
        pass

    pk = manager.get_primary_key("key 1")
    eq_(pk, "primary key")


def test_dict_as_plugin_payload():
    manager = PluginManager("test plugin3")

    plugin = PluginInfo("test plugin3", tags=["primary key", "key 1", "key 2"])
    plugin(dict(B=1))

    instance = manager.load_me_now("key 1")
    eq_(instance, dict(B=1))


def test_show_me_your_name():
    class Test(object):
        pass

    name = _show_me_your_name(Test)
    eq_(name, "Test")

    name2 = _show_me_your_name(dict(A=1))
    assert "dict" in name2


def make_me_a_plugin_info(plugin_name):
    return PluginInfo(plugin_name, "abs_path", custom="property")

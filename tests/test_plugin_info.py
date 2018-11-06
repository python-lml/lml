import json

from lml.plugin import PluginInfo
from nose.tools import eq_


def test_plugin_info():
    info = PluginInfo(
        "renderer", abs_class_path="good.plugin.path", custom="property"
    )
    assert info.custom == "property"
    keys = list(info.tags())
    assert len(keys) == 1
    assert keys[0] == "renderer"
    assert info.module_name == "good"
    expected = {
        "path": "good.plugin.path",
        "plugin_type": "renderer",
        "custom": "property",
    }
    eq_(json.loads(info.__repr__()), expected)


def test_module_name_scenario_2():
    class TestClass2:
        pass

    info = PluginInfo("renderer", custom="property")
    info.cls = TestClass2
    eq_(info.module_name, "test_plugin_info")

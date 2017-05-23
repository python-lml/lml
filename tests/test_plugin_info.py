from lml.plugin import PluginInfo
import json
from nose.tools import eq_


def test_plugin_info():
    info = PluginInfo('renderer',
                      abs_class_path='abs import path',
                      custom='property')
    assert info.custom == 'property'
    keys = list(info.tags())
    assert len(keys) == 1
    assert keys[0] == 'renderer'
    expected = {"path": "abs import path",
                "plugin_type": "renderer",
                "custom": "property"}
    eq_(json.loads(info.__repr__()), expected)

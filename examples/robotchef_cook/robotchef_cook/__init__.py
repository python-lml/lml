from lml.plugin import PluginInfoList


PluginInfoList(__name__).add_a_plugin(
    'cuisine',
    'cook.Cook',
    tags=['bread']
)

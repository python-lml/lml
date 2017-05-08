from lml.registry import PluginList


PluginList(__name__).add_a_plugin(
    'robot',
    'cook.Cook',
    tags=['bread']
)

from lml.registry import PluginList


PluginList(__name__).add_a_plugin(
    'cuisine',
    'cook.Cook',
    tags=['bread']
)

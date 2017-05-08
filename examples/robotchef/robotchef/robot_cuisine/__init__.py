from lml.registry import PluginList


PluginList(__name__).add_a_plugin(
    'cuisine',
    'electricity.Boost',
    tags=['Portable Battery']
)

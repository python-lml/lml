from lml.registry import PluginList


PluginList(__name__).add_a_plugin(
    'robot',
    'fry.Fry',
    tags=['Fish and Chips']
).add_a_plugin(
    'robot',
    'bake.Bake',
    tags=['Cornish Scone']
)

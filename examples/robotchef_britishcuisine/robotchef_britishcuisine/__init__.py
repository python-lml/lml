from lml.plugin import PluginInfoChain


PluginInfoChain(__name__).add_a_plugin(
    'cuisine',
    'fry.Fry',
    tags=['Fish and Chips']
).add_a_plugin(
    'cuisine',
    'bake.Bake',
    tags=['Cornish Scone', 'Jacket Potato']
)

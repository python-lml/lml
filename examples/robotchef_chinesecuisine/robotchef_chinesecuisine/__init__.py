from lml.plugin import PluginInfoChain


PluginInfoChain(__name__).add_a_plugin(
    'cuisine',
    'roast.Roast',
    tags=['Peking Duck']
)

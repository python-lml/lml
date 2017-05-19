from lml.plugin import PluginInfoList


PluginInfoList(__name__).add_a_plugin(
    'cuisine',
    'roast.Roast',
    tags=['Peking Duck']
)

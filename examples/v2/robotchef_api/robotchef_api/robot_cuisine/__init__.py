from lml.plugin import PluginInfoChain


PluginInfoChain(__name__).add_a_plugin(
    "cuisine", "electricity.Boost", tags=["Portable Battery"]
)

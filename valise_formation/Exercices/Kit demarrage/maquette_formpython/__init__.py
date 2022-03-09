# (c) Auteur 2013
def classFactory(iface):
  from .main import MainPlugin
  return MainPlugin(iface)


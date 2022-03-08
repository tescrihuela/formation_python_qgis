# Module 3 : PyQGIS

Les lignes ci-dessous sont écrites car interprétées dans la console Python de QGIS.

---

### Préambule : charger iface
``` python
iface = qgis.utils.iface
```

### Lister les champs de la couche active
``` python
l = iface.activeLayer()
print('\n'.join([l.fields().field(i).name() for i in range(len(l.fields()))]))
```

### Lister toutes les couches du canevas
```python
layers = iface.mapCanvas().layers()
print('\n'.join([layers[i].name() for i in range(len(layers))]))
```


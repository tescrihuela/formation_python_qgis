ziface = qgis.utils.iface
zList = ziface.mapCanvas().layers()
for i in range(len(zList)) :
	print("%s") %(str(zList[i].metadata()))





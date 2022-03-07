__author__ = "Thomas Escrihuela"
__version__ = "1.0"

import requests
import xml.etree.ElementTree as ET
from pprint import pprint


#### Paramètres ####
getcap_url = "https://wxs.ign.fr/essentiels/wmts?request=GetCapabilities&service=WMTS&version=1.0.0"


#### Fonctions ####
def get_getcap(url):
    r = requests.get(url)
    return r.text


###############
#### MAIN #####
###############
if __name__ == '__main__':
    response = get_getcap(getcap_url)
    # print(response)
    root = ET.fromstring(response)
    # print(root.tag)
    # print(root.attrib)
    # print(root.findall('{http://www.opengis.net/wmts/1.0}Layer'))
    for a in root:
        for child in a:
            print(child.tag, child.attrib)
    # pprint(root)
    # for country in root.findall('{http://www.opengis.net/wmts/1.0}Contents'):
    #     rank = country.find('ows:Title')
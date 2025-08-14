# Handles reading and writing of XML configuration files.
import xml.etree.ElementTree as ET
from typing import Dict, Any
from parser_base import ConfigParserBase

class XMLConfigParser(ConfigParserBase):
    def load(self, path: str) -> Dict[str, Any]:
        tree = ET.parse(path)
        root = tree.getroot()
        return {child.tag: child.text for child in root}

    def save(self, path: str, config: Dict[str, Any]):
        root = ET.Element('config')
        for key, value in config.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(path)

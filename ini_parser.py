# Handles reading and writing of INI configuration files.
import configparser
from typing import Dict, Any
from parser_base import ConfigParserBase

class INIConfigParser(ConfigParserBase):
    def load(self, path: str) -> Dict[str, Any]:
        parser = configparser.ConfigParser()
        parser.read(path)
        return {section: dict(parser.items(section)) for section in parser.sections()}

    def save(self, path: str, config: Dict[str, Any]):
        parser = configparser.ConfigParser()
        for section, params in config.items():
            parser[section] = params
        with open(path, 'w') as f:
            parser.write(f)
